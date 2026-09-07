---
title: Rewriting Bun in Rust
type: source
source_type: article
url: https://bun.com/blog/bun-in-rust
fetched: 2026-09-06
---

# Rewriting Bun in Rust

Disclosure: Bun was acquired by Anthropic in December 2025. I and others on the Bun team work at Anthropic. I used a pre-release version of Claude Fable 5 for much of the Rust rewrite.

Bun started as a line-for-line port of esbuild's JavaScript & TypeScript transpiler from Go to Zig. I wrote my first line of Zig on [April 16, 2021](https://github.com/ziglang/zig/issues/8575). I bet on Zig after seeing the single-page [Zig Language Reference](https://ziglang.org/documentation/master/) on Hacker News and getting really excited about the low-level control and care for performance.

From the start, Bun's scope was massive:

* JavaScript, TypeScript, and CSS transpiler, minifier, and bundler
* npm-compatible package manager
* Jest-like test runner
* Node.js & TypeScript-compatible module resolution
* HTTP/1.1 & WebSocket client
* Node.js API implementations like `fs`, `net`, `tls`, and dozens of other modules

The initial version of Bun was written by me in 1 year, in a cramped Oakland apartment, pre-LLM, in Zig. The default outcome for ambitiously-scoped projects like Bun is joining the graveyard of dead side projects on a GitHub profile page. Zig made Bun possible. I would never have been able to build this much in 1 year if it wasn't for Zig.

Nowadays, Bun's CLI gets over 22 million monthly downloads. Popular tools like Claude Code and OpenCode bet on Bun as their runtime. Vercel, Railway, DigitalOcean and more have 1st-party support for Bun.

Bun's scope has also been a challenge for stability. Here's a small sample of bugs we fixed in Bun v1.3.14:

* heap-use-after-free crash in `node:zlib` when calling `.reset()` on a zlib, Brotli, or Zstd stream while an async `.write()` is still in progress on the threadpool
* use-after-free crash in `node:zlib` when an `onerror` callback issued a re-entrant `write()` followed by `close()` on native handles
* use-after-free crashes in `node:http2` when re-entrant JS callbacks (e.g. `session.request()` inside a timeout listener, an options getter, or a write callback) triggered a hashmap rehash, invalidating internal stream pointers
* use-after-free in `UDPSocket.send()` and `sendMany()` where user code in `valueOf()` or `toString()` callbacks could detach an `ArrayBuffer` between payload capture and the actual send
* crash and out-of-bounds read in `Buffer#copy` and `Buffer#fill` when a `valueOf` callback detaches or resizes the underlying `ArrayBuffer` during argument coercion
* heap out-of-bounds write in `UDPSocket.sendMany()` when the socket's connection state changed mid-iteration via user JS callbacks
* memory leak in `crypto.scrypt` where the callback and protected password/salt buffers were never released when the output buffer allocation failed
* `SSLWrapper.init` leaked the strdup'd passphrase on error paths
* memory leak in `tlsSocket.setSession()` where each call leaked one `SSL_SESSION` (~6.5 KB per call) due to a missing `SSL_SESSION_free` after `d2i_SSL_SESSION`
* memory leak where `fs.watch()` watchers were never garbage collected after `.close()`, caused by a reference count underflow that permanently pinned each watcher as a GC root
* double-free crash in the CSS parser when `background-clip` had vendor prefixes and multi-layer backgrounds
* `DuplexUpgradeContext` was never freed — a full leak per `tls.connect({ socket: duplex })`
* race condition crash in `MessageEvent` where the GC marker thread could observe a torn variant in `m_data` during concurrent access from a `BroadcastChannel` or `MessagePort`

We could have kept fixing these kinds of bugs one-off in perpetuity, but we owe it to our users counting on us to do better than that, and systematically prevent these kinds of bugs from recurring.

### What we were already doing[#](#what-we-were-already-doing)

* We patched the Zig compiler to add Address Sanitizer support. We run our test suite with ASAN on every commit.
* We ship Zig safety-checked ReleaseSafe builds on Windows
* We fuzz Bun's runtime APIs 24/7 using [Fuzzilli](https://github.com/googleprojectzero/fuzzilli), the JavaScript engine fuzzer used by V8 & JavaScriptCore
* We have a whole lot of end-to-end memory leak tests

This is more than many projects do.

## Just be really smart and don't make mistakes?[#](#just-be-really-smart-and-don-t-make-mistakes)

Our bugfix list felt bad and I was tired of going to sleep worrying about crashes in Bun. I don't blame Zig for that - other users of Zig don't have the bugs we had, and mixing GC with manually-managed memory is an uncommon enough thing for software to need that no language really designs for it. We wouldn't have gotten this far if not for Zig, and I'll always be grateful. Until very recently, programming language choice was a one-way decision for a project like Bun.

JavaScript is a garbage-collected language and modern JavaScript engines like JavaScriptCore (and V8) have strict rules around exception handling and the garbage collector. Zig, like C, doesn't manage memory for you and this is a tradeoff that for many projects is a great reason to use Zig. Zig does not have constructors/destructors, and most cleanup is expected to be written out explicitly at each call site with `defer`.

For Bun, correctly handling the lifetimes of garbage-collected values and manually-managed values has been a major source of stability issues - most often small memory leaks and occasionally, crashes. Every memory allocation has to be meticulously reviewed. Where do these bytes get freed? How do we ensure it only gets freed once? Did we check for JavaScript exceptions properly? Is this garbage-collected pointer visible to the conservative stack scanner? Is this garbage collected memory or manually managed memory?

For stability issues, knowing as early as possible is best. Fuzzing happens after code is merged. CI happens when code is pushed. Runtime safety checks & address sanitizer happens when code is run (hopefully in development, before CI).

One common way to reduce this class of issue is to ensure cleanup code is always run exactly once for code that needs it. Zig is designed to be a simple language with no hidden control flow, and so it prefers the explicit `defer` keyword to run code at the end of a scope over C++'s implicit ~Destructor or Rust's implicit `Drop`.

| Language | Cleanup |
| --- | --- |
| Zig | `defer`, `errdefer` |
| C++ | ~Destructor, &&Move |
| Rust | Drop |

For Zig code, when exactly should we be running the cleanup code? If we're passing the same `*T` to many different functions, how do we know when it's no longer accessible and can be cleaned up? How does it work when some functions need to continue to reference the memory after the function is called? Our current approach is a mix of:

* arena lifetimes, where the scope of when it's accessible is clear (parser state doesn't escape the calling function and so AST nodes are a good choice there)
* reference-counting
* pay really close attention

Many projects opt to answer these kinds of questions through a style guide. TigerBeetle's [TigerStyle](https://tigerstyle.dev/) is an example in Zig and Google's 31,000 word [C++ style guide](https://google.github.io/styleguide/cppguide.html) is another. The challenge with style guides is enforcement. How do you make sure the style guide is followed? Historically, code review was the answer with best-effort enforcement via linters & static analyzers.

Having a rigid style guide with clear ownership expectations explicitly spelled out in the type system was a real option for Bun. Since Zig has no operator overloading, we would likely end up with a lot of code looking something like this:

This is less ergonomic than the Zig we expect:

## What about C/C++?[#](#what-about-c-c)

About 20% of Bun's code is written in C++ and Bun embeds several C/C++ libraries:

* JavaScriptCore, the JavaScript engine that powers Safari
* uWebSockets & usockets - our HTTP/WebSocket server, and event loop
* lshpack & lsquic - `HPACK` and HTTP/3 libraries
* BoringSSL, Google's OpenSSL fork
* SQLite

C++ instead of Zig would be a reasonable choice for Bun. We would get constructors & destructors. We could delete lots of `extern "C"` wrapper code.

But, we would still be reliant on style guides enforced through code review, and even with ASAN, memory corruption and memory leaks would still happen.

## Why Rust?[#](#why-rust)

A large percentage of bugs from that list are use-after-free, double-free, and "forgot to free" in an error path. In safe Rust, these are compiler errors and RAII-like automatic cleanup with `Drop`. Compiler errors are a better feedback loop than a style guide.

Historically, rewrites are a terrible idea. Excluding comments, Bun is 535,496 lines of Zig. A rewrite in another language would take a small team of engineers a full year. It would mean freezing bugfixes, security fixes or feature development for that time. The least risky approach to getting something shippable would be a mechanical port from Zig to Rust, with the minimal number of behavioral changes, using the exact same test suite we already use for testing Bun.

Fortunately, Bun's own test suite is written in TypeScript which means it doesn't depend on the runtime's programming language.

A year of zero user-facing impact is not a realistic option we could consider. So, enforcement through code-style to fix stability issues was our best bet, and was our plan when we added Rust-inspired [smart pointers](https://github.com/oven-sh/bun/blob/3a79bd746b11601c9db970b608c73f0b9f96ac81/src/ptr/shared.zig#L569) to Bun's codebase.

But honestly, I didn't want to do it. Homegrown smart pointers offer worse ergonomics than Rust, with none of the guarantees.

What if, instead, I spend a week testing if Anthropic's new model can rewrite Bun in Rust?

At first, I didn't expect it to work. A few days in, a high % of the test suite started passing and I saw how much the new Rust code matched up with the original Zig codebase. My opinion went from "this is worth trying" to "I'm going to merge this".

## Claude, rewrite Bun in Rust.[#](#claude-rewrite-bun-in-rust)

There are a lot of ways to do a terrible job of this. For example, prompting Claude "Rewrite Bun in Rust. Don't make any mistakes." and then praying it would work is not what I did.

Think about how a person would do this. The first big question is:

Incremental rewrite? Or, everything all at once?

In my experience porting esbuild's transpiler from Go to Zig for the initial version of Bun (without LLMs), everything all at once is better. An incremental rewrite adds temporary code that you hope gets deleted eventually, and would be painful in the short-medium term.

The second big question: how?

How do we keep Bun in Rust the same Bun as before, with the same architecture, performance, and feature-set while also getting the language features of Rust like the borrow checker? How do we ensure the team can still maintain it after the rewrite?

Do the rewrite that looks like we transpiled our Zig code to Rust. We can gradually refactor it to reduce `unsafe` usage and look more like idiomatic Rust after Bun v1.4 ships.

Those are the only two big questions. Everything else is tactics.

## Loops that write & review code[#](#loops-that-write-review-code)

A lot of day-to-day engineering work as software engineers can be over-simplified into loops.

A `task` has some context associated with it (a Jira ticket, a GitHub issue, etc). The `result` is the code you wrote to fix it. Code reviewer(s) `review` the changes to check for regressions & correctness. And then you address the feedback.

I rewrote Bun in Rust using about 50 dynamic workflows in Claude Code run continuously over the course of 11 days.

Each dynamic workflow was a loop like this - a workflow for:

* Generate a porting guide mapping Zig patterns & types to Rust patterns & types
* Mechanically port every `.zig` file to a `.rs` file, matching the PORTING.md and LIFETIMES.tsv
* Fix every crate's compiler errors
* Get subcommands like `bun test` or `bun build` to work
* Get every test in Bun's entire test suite to pass
* Several large refactors and cleanup passes

For most of those 11 days (and after), I monitored workflows - manually reading the outputs to check for issues and bugs, and prompting Claude to edit the loop to fix things.

How do you review a PR with +1 million lines added? How do you start to build the confidence needed to responsibly merge large quantities of LLM-authored code?

A language-independent test suite with a million assertions, adversarial code review and when something does go wrong, fixing the process that generates the code instead of hand-fixing the code.

### Adversarial review[#](#adversarial-review)

Adversarial review asks Claude (in a separate context window) to exhaustively come up with reasons why the changes create bugs or do not work.

#### Split context windows

Usually with humans, the person reviewing the code is not the person who authored the code. The person writing the code wants to merge the code, which can bias their actions to ship before it's ready.

Claude is the same way. The Claude that wrote the code wants the code to get accepted. The Claude that reviews wants to find issues in the code.

1 implementer, 2 or more adversarial reviewers per implementer. The reviewer's only job: find bugs & reasons why the code does not work. The implementer doesn't review. The reviewer doesn't implement.

✻ claude code · dynamic workflowadversarial review3 of the many bugs adversarial review caught before merge

bug 1 of 3 · the async close▶ play

✻claudeimplementer

its context: the .zig original, the port plan, its own reasoning

✻claudeadversarial reviewer

its context: only the diff. told to assume the code is wrong.

✻

src/runtime/api/bun/js\_bun\_spawn\_bindings.rs · compiles clean

for stdio in [spawned\_stdout, spawned\_stderr] {

match stdio {

StdioResult::Buffer(mut pipe) => {

// pipe: Box<uv::Pipe> — hand it to libuv to close

pipe.close(Subprocess::on\_pipe\_close)

}

StdioResult::Fd(fd) => fd.close(),

StdioResult::Unavailable => {}

}

}

✻

uv\_close is asynchronous: libuv keeps the raw handle pointer until the next loop tick, then calls on\_pipe\_close, which frees the allocation. But `pipe` is a Box that drops at the end of this match arm — libuv is left holding freed memory, and the close callback then frees it a second time. Use-after-free, then double-free.

✻

Box::leak(pipe).close(Subprocess::on\_pipe\_close)

f0a454376c7 · win-review: js\_bun\_spawn\_bindings.rs leak Box<uv::Pipe> before async uv\_close to avoid UAF/double-free in on\_pipe\_close

✻

src/runtime/node/node\_fs.rs · compiles clean

// split f64 seconds into a timespec-style {sec, nsec}

let sec = t.trunc();

TimeLike {

sec: sec as i64,

nsec: ((t - sec) \* 1e9) as i64,

}

✻

For a negative, non-integer time — a file mtime before 1970 — trunc rounds toward zero: -1.5 becomes {sec: -1, nsec: -500\_000\_000}. A negative nsec is an invalid timespec. floor keeps nsec in [0, 1e9): {sec: -2, nsec: 500\_000\_000}.

✻

let sec = t.floor();

nsec: ((t - sec) \* 1e9).round() as i64,

7cc88f00141 · crossplat review fixes: … node\_fs win to\_sys\_time\_like floor() so nsec∈[0,1e9) for negative t …

✻

src/css/values/color.rs · compiles clean

// each side of color-mix() may omit its percentage;

// a missing one defaults to the remainder of the other side

let p1 = first.percentage.unwrap\_or(1.0 - second.percentage.unwrap());

✻

unwrap\_or evaluates its argument eagerly — second.percentage.unwrap() runs even when first.percentage is Some. So color-mix(in srgb, red 40%, blue), where only the second percentage is omitted, panics inside the argument expression before unwrap\_or ever gets to ignore it. unwrap\_or\_else takes a closure and stays lazy.

✻

let p1 = first

.percentage

.unwrap\_or\_else(|| 1.0 - second.percentage.unwrap());

90111846a14 · phase-b2: color.rs gated\_full\_impl FULLY DISSOLVED (verify: parse\_color\_mix unwrap\_or eager panic, Default CurrentColor vs transparent)

Three bugs the adversarial reviewers actually caught — every cited commit carries its review attribution in the subject line. All three compiled; all three looked plausible. The reviewer is a second Claude in its own context window: it gets the diff and nothing else — none of the implementer's reasoning — and is told to find the way it's wrong. Code is condensed from the cited commits; same bugs, same fixes.

## What does this look like?[#](#what-does-this-look-like)

If you're about to do something big and expensive, it saves time and money to de-risk it first.

### Prep work[#](#prep-work)

Before writing any code, I spent about 3 hours talking to Claude about how to map patterns from our Zig codebase closely to Rust. Claude serialized this discussion into a `PORTING.md` document, which ended up on [Hacker News](https://news.ycombinator.com/item?id=48016880).

The next question: how do you add Rust lifetimes to code that manually manages memory?

That's where I prompted Claude something like this:

Me: Let's kick off a dynamic workflow to analyze the proper lifetimes of every struct field in the codebase. This workflow should read every struct field within every single file and trace the control flow. First, look for struct fields with complex lifetimes to express in Rust, then propose a lifetime for that field, then use 2 adversarial review agents to review that lifetime, then apply any feedback and serialize into a LIFETIMES.tsv for other claudes to look at.

Then a round of adversarial reviews on the `PORTING.md` and the `LIFETIMES.tsv` together to fix any conflicting suggestions and double check everything. I also manually read over it.

### Trial run[#](#trial-run)

Before asking Claude to translate all 1,448 .zig files to .rs files, I started with just 3. For each of the 3 files, 1 implementer wrote the new `.rs` file, 2 adversarial reviewers checked the `.rs` file matched the behavior of the `.zig` file and that it followed the `PORTING.md` & `LIFETIMES.tsv`. After that, 1 fixer applied any suggestions.

### False starts[#](#false-starts)

I asked Claude to loop the workflow on all 1,448 .zig files, and about 2 minutes in, one Claude ran `git stash` before committing. Another ran `git stash pop`. And then `git reset HEAD --hard`. They were stepping on each other! And if I put each Claude into a separate worktree, I would run out of disk space because Bun's git repository is too big and eventually the changes will need to be compiled and seen together.

So, I asked Claude to edit the workflow to instruct Claude to never run `git stash` or `git reset` or any `git` command that doesn't commit a specific file at once. No `cargo` either. No slow commands at all.

Then, Claude resumed the workflows. And it was working! Too slowly, so I split it into just 4 workflow shards each with their own worktree (4 worktrees total), each running 16 claudes committing and pushing files.

### Finally writing the code[#](#finally-writing-the-code)

Thanks to all the parallelization & this prep work, at peak Claude wrote about 1,300 lines of code per minute. Every line of code was reviewed by two separate adversarial reviewers (also Claude) and went through a round of fixes before committing. Absolutely none of it worked yet.

11 days × 24 hours · PDT

6,502 commits

1695 commits/hour

12am6am12pm6pmMay 4May 4, 7am–8am PDT — 6 commits, +89,278 linesMay 4, 8am–9am PDT — 2 commits, +50,742 linesMay 4, 9am–10am PDT — 1 commit, +28,149 linesMay 4, 11am–12pm PDT — 1 commit, +39,752 linesMay 4, 12pm–1pm PDT — 3 commits, +251,616 linesMay 4, 1pm–2pm PDT — 2 commits, +161,724 linesMay 4, 3pm–4pm PDT — 3 commits, +136,381 linesMay 4, 5pm–6pm PDT — 5 commits, +895 linesMay 4, 6pm–7pm PDT — 5 commits, +17,027 linesMay 4, 7pm–8pm PDT — 1 commit, +106 linesMay 4, 9pm–10pm PDT — 13 commits, +11,661 linesMay 4, 11pm–12am PDT — 6 commits, +8,516 linesMay 5May 5, 12am–1am PDT — 9 commits, +1,381 linesMay 5, 1am–2am PDT — 7 commits, +1,577 linesMay 5, 2am–3am PDT — 4 commits, +2,035 linesMay 5, 3am–4am PDT — 4 commits, +7,808 linesMay 5, 4am–5am PDT — 1 commit, +2,796 linesMay 5, 5am–6am PDT — 2 commits, +29,370 linesMay 5, 8am–9am PDT — 2 commits, +7,076 linesMay 5, 9am–10am PDT — 2 commits, +308 linesMay 5, 11am–12pm PDT — 2 commits, +1,643 linesMay 5, 12pm–1pm PDT — 4 commits, +1,452 linesMay 5, 1pm–2pm PDT — 1 commit, +2,142 linesMay 5, 2pm–3pm PDT — 4 commits, +7,787 linesMay 5, 3pm–4pm PDT — 2 commits, +5,835 linesMay 5, 4pm–5pm PDT — 1 commit, +3,417 linesMay 5, 5pm–6pm PDT — 4 commits, +3,960 linesMay 5, 6pm–7pm PDT — 4 commits, +9,179 linesMay 5, 7pm–8pm PDT — 4 commits, +1,983 linesMay 5, 8pm–9pm PDT — 4 commits, +18,902 linesMay 5, 9pm–10pm PDT — 43 commits, +40,650 linesMay 5, 10pm–11pm PDT — 139 commits, +64,842 linesMay 5, 11pm–12am PDT — 141 commits, +34,814 linesMay 6May 6, 12am–1am PDT — 60 commits, +10,417 linesMay 6, 1am–2am PDT — 296 commits, +38,530 linesMay 6, 2am–3am PDT — 306 commits, +18,836 linesMay 6, 3am–4am PDT — 196 commits, +10,245 linesMay 6, 4am–5am PDT — 86 commits, +2,655 linesMay 6, 5am–6am PDT — 16 commits, +289 linesMay 6, 8am–9am PDT — 5 commits, +264 linesMay 6, 9am–10am PDT — 458 commits, +16,409 linesMay 6, 10am–11am PDT — 695 commits, +44,000 linesMay 6, 11am–12pm PDT — 102 commits, +21,972 linesMay 6, 12pm–1pm PDT — 19 commits, +2,891 linesMay 6, 1pm–2pm PDT — 3 commits, +56 linesMay 6, 3pm–4pm PDT — 64 commits, +3,606 linesMay 6, 4pm–5pm PDT — 264 commits, +60,132 linesMay 6, 5pm–6pm PDT — 268 commits, +40,953 linesMay 6, 6pm–7pm PDT — 281 commits, +16,283 linesMay 6, 7pm–8pm PDT — 258 commits, +26,654 linesMay 6, 8pm–9pm PDT — 327 commits, +16,599 linesMay 6, 9pm–10pm PDT — 74 commits, +8,331 linesMay 6, 10pm–11pm PDT — 17 commits, +2,200 linesMay 6, 11pm–12am PDT — 11 commits, +3,590 linesMay 7May 7, 12am–1am PDT — 17 commits, +6,577 linesMay 7, 1am–2am PDT — 22 commits, +8,718 linesMay 7, 2am–3am PDT — 21 commits, +11,392 linesMay 7, 3am–4am PDT — 53 commits, +6,476 linesMay 7, 4am–5am PDT — 31 commits, +2,356 linesMay 7, 5am–6am PDT — 9 commits, +1,787 linesMay 7, 6am–7am PDT — 4 commits, +580 linesMay 7, 7am–8am PDT — 5 commits, +181 linesMay 7, 11am–12pm PDT — 3 commits, +421 linesMay 7, 12pm–1pm PDT — 1 commit, +13 linesMay 7, 1pm–2pm PDT — 5 commits, +248 linesMay 7, 2pm–3pm PDT — 9 commits, +2,131 linesMay 7, 3pm–4pm PDT — 51 commits, +3,207 linesMay 7, 4pm–5pm PDT — 56 commits, +2,647 linesMay 7, 5pm–6pm PDT — 159 commits, +2,787 linesMay 7, 6pm–7pm PDT — 42 commits, +1,590 linesMay 7, 7pm–8pm PDT — 46 commits, +4,170 linesMay 7, 8pm–9pm PDT — 52 commits, +2,113 linesMay 7, 9pm–10pm PDT — 27 commits, +1,585 linesMay 7, 10pm–11pm PDT — 27 commits, +2,231 linesMay 7, 11pm–12am PDT — 30 commits, +4,987 linesMay 8May 8, 12am–1am PDT — 27 commits, +1,196 linesMay 8, 1am–2am PDT — 14 commits, +904 linesMay 8, 2am–3am PDT — 8 commits, +536 linesMay 8, 3am–4am PDT — 13 commits, +253 linesMay 8, 4am–5am PDT — 3 commits, +771 linesMay 8, 5am–6am PDT — 15 commits, +1,545 linesMay 8, 6am–7am PDT — 12 commits, +1,965 linesMay 8, 7am–8am PDT — 14 commits, +1,866 linesMay 8, 8am–9am PDT — 55 commits, +3,622 linesMay 8, 9am–10am PDT — 35 commits, +4,778 linesMay 8, 10am–11am PDT — 1 commit, +0 linesMay 8, 12pm–1pm PDT — 1 commit, +116 linesMay 8, 1pm–2pm PDT — 2 commits, +66 linesMay 8, 2pm–3pm PDT — 9 commits, +1,071 linesMay 8, 3pm–4pm PDT — 26 commits, +1,691 linesMay 8, 4pm–5pm PDT — 18 commits, +2,751 linesMay 8, 5pm–6pm PDT — 2 commits, +97 linesMay 8, 6pm–7pm PDT — 2 commits, +135 linesMay 8, 7pm–8pm PDT — 11 commits, +1,763 linesMay 8, 8pm–9pm PDT — 20 commits, +5,272 linesMay 8, 9pm–10pm PDT — 12 commits, +952 linesMay 8, 10pm–11pm PDT — 2 commits, +334 linesMay 8, 11pm–12am PDT — 6 commits, +2,033 linesMay 9May 9, 12am–1am PDT — 9 commits, +387 linesMay 9, 1am–2am PDT — 9 commits, +723 linesMay 9, 2am–3am PDT — 8 commits, +98 linesMay 9, 3am–4am PDT — 63 commits, +2,538 linesMay 9, 4am–5am PDT — 11 commits, +8,861 linesMay 9, 5am–6am PDT — 4 commits, +42 linesMay 9, 6am–7am PDT — 3 commits, +2,616 linesMay 9, 7am–8am PDT — 6 commits, +6,993 linesMay 9, 8am–9am PDT — 1 commit, +3,705 linesMay 9, 9am–10am PDT — 11 commits, +199 linesMay 9, 11am–12pm PDT — 1 commit, +23 linesMay 9, 12pm–1pm PDT — 4 commits, +5,012 linesMay 9, 1pm–2pm PDT — 7 commits, +2,080 linesMay 9, 2pm–3pm PDT — 6 commits, +924 linesMay 9, 3pm–4pm PDT — 5 commits, +248 linesMay 9, 4pm–5pm PDT — 17 commits, +508 linesMay 9, 5pm–6pm PDT — 2 commits, +135 linesMay 9, 6pm–7pm PDT — 4 commits, +822 linesMay 9, 7pm–8pm PDT — 1 commit, +7 linesMay 10May 10, 12am–1am PDT — 4 commits, +497 linesMay 10, 1am–2am PDT — 2 commits, +35 linesMay 10, 2am–3am PDT — 1 commit, +131 linesMay 10, 3am–4am PDT — 2 commits, +322 linesMay 10, 4am–5am PDT — 1 commit, +3 linesMay 10, 5am–6am PDT — 1 commit, +26 linesMay 10, 6am–7am PDT — 2 commits, +81 linesMay 10, 7am–8am PDT — 1 commit, +5 linesMay 10, 8am–9am PDT — 4 commits, +78 linesMay 10, 9am–10am PDT — 1 commit, +1 linesMay 10, 10am–11am PDT — 2 commits, +128 linesMay 10, 11am–12pm PDT — 1 commit, +4 linesMay 10, 12pm–1pm PDT — 2 commits, +413 linesMay 10, 1pm–2pm PDT — 1 commit, +25 linesMay 10, 2pm–3pm PDT — 5 commits, +327 linesMay 10, 3pm–4pm PDT — 6 commits, +1,172 linesMay 10, 4pm–5pm PDT — 4 commits, +752 linesMay 10, 5pm–6pm PDT — 3 commits, +227 linesMay 10, 6pm–7pm PDT — 2 commits, +242 linesMay 10, 7pm–8pm PDT — 1 commit, +306 linesMay 10, 8pm–9pm PDT — 1 commit, +54 linesMay 10, 9pm–10pm PDT — 2 commits, +75 linesMay 10, 10pm–11pm PDT — 1 commit, +134 linesMay 10, 11pm–12am PDT — 5 commits, +103 linesMay 11May 11, 12am–1am PDT — 2 commits, +150 linesMay 11, 1am–2am PDT — 4 commits, +398 linesMay 11, 2am–3am PDT — 2 commits, +364 linesMay 11, 3am–4am PDT — 3 commits, +44 linesMay 11, 4am–5am PDT — 7 commits, +9,367 linesMay 11, 6am–7am PDT — 2 commits, +43 linesMay 11, 7am–8am PDT — 2 commits, +149 linesMay 11, 8am–9am PDT — 10 commits, +2,171 linesMay 11, 9am–10am PDT — 16 commits, +2,047 linesMay 11, 10am–11am PDT — 18 commits, +3,356 linesMay 11, 11am–12pm PDT — 9 commits, +861 linesMay 11, 12pm–1pm PDT — 3 commits, +412 linesMay 11, 1pm–2pm PDT — 12 commits, +2,978 linesMay 11, 2pm–3pm PDT — 157 commits, +10,700 linesMay 11, 3pm–4pm PDT — 16 commits, +1,346 linesMay 11, 4pm–5pm PDT — 3 commits, +78 linesMay 11, 5pm–6pm PDT — 41 commits, +2,568 linesMay 11, 6pm–7pm PDT — 55 commits, +4,912 linesMay 11, 7pm–8pm PDT — 53 commits, +3,475 linesMay 11, 8pm–9pm PDT — 32 commits, +1,732 linesMay 11, 9pm–10pm PDT — 46 commits, +4,506 linesMay 11, 10pm–11pm PDT — 45 commits, +1,711 linesMay 11, 11pm–12am PDT — 52 commits, +10,850 linesMay 12May 12, 12am–1am PDT — 30 commits, +3,760 linesMay 12, 1am–2am PDT — 24 commits, +9,443 linesMay 12, 2am–3am PDT — 41 commits, +1,635 linesMay 12, 3am–4am PDT — 39 commits, +788 linesMay 12, 4am–5am PDT — 27 commits, +651 linesMay 12, 5am–6am PDT — 23 commits, +779 linesMay 12, 6am–7am PDT — 1 commit, +137,576 linesMay 12, 7am–8am PDT — 2 commits, +81 linesMay 12, 8am–9am PDT — 2 commits, +75 linesMay 12, 9am–10am PDT — 2 commits, +130 linesMay 12, 10am–11am PDT — 5 commits, +160 linesMay 12, 11am–12pm PDT — 2 commits, +20 linesMay 12, 12pm–1pm PDT — 1 commit, +2 linesMay 12, 1pm–2pm PDT — 30 commits, +2,677 linesMay 12, 2pm–3pm PDT — 41 commits, +7,022 linesMay 12, 3pm–4pm PDT — 4 commits, +200 linesMay 12, 4pm–5pm PDT — 27 commits, +1,423 linesMay 12, 5pm–6pm PDT — 19 commits, +1,055 linesMay 12, 6pm–7pm PDT — 2 commits, +380 linesMay 12, 7pm–8pm PDT — 2 commits, +84 linesMay 12, 9pm–10pm PDT — 7 commits, +273 linesMay 12, 10pm–11pm PDT — 3 commits, +230 linesMay 12, 11pm–12am PDT — 7 commits, +319 linesMay 13May 13, 12am–1am PDT — 2 commits, +133 linesMay 13, 1am–2am PDT — 14 commits, +2,177 linesMay 13, 2am–3am PDT — 12 commits, +685 linesMay 13, 4am–5am PDT — 10 commits, +657 linesMay 13, 5am–6am PDT — 1 commit, +687 linesMay 13, 6am–7am PDT — 11 commits, +380 linesMay 13, 7am–8am PDT — 12 commits, +5,247 linesMay 13, 8am–9am PDT — 14 commits, +1,051 linesMay 13, 9am–10am PDT — 7 commits, +680 linesMay 13, 10am–11am PDT — 10 commits, +412 linesMay 13, 11am–12pm PDT — 6 commits, +314 linesMay 13, 12pm–1pm PDT — 10 commits, +2,980 linesMay 13, 1pm–2pm PDT — 1 commit, +0 linesMay 13, 2pm–3pm PDT — 3 commits, +439 linesMay 13, 5pm–6pm PDT — 7 commits, +114 linesMay 13, 6pm–7pm PDT — 4 commits, +605 linesMay 13, 9pm–10pm PDT — 1 commit, +13 linesMay 13, 10pm–11pm PDT — 1 commit, +48 linesMay 13, 11pm–12am PDT — 1 commit, +8 linesMay 14May 14, 12am–1am PDT — 1 commit, +150 lines

Every commit on the port branch (merges excluded), bucketed by hour. Peak hour: 695 commits.

Notice the inconsistent timing? I forgot to increase the default IOPS on the EC2 instance this ran on. One slow `grep` command was all it took to freeze disk reads & writes for minutes.

### Compiler errors as a work queue[#](#compiler-errors-as-a-work-queue)

After writing all the code, I asked Claude to write a workflow fixing every compiler error. We went crate-by-crate.

✻ claude code · dynamic workflow

≈16,000 errors left

▶ replay phase DWed, May 6, 12:40 AM PDT

errors.txt0 fix commits

error: deref \*mut EventLoop before field access

error: js\_parser/ast/E.rs: port json\_stringify for Number/BigInt/RegExp

error: NodeHTTPResponse.rs: wire JSNodeHTTPResponse cached accessors vi

error[E0034]: multiple applicable items in scope

error: test\_command.rs: wire coverage façade to bun\_sourcemap\_jsc::code

error: bundler/ungate\_support.rs: un-gate bun\_css shim to real ::bun\_cs

error: dns.rs: implement pending\_cache\_for/get\_key/get\_or\_put\_into\_reso

error: css/css\_parser.rs: port DefineShorthand contract, parse\_bundler,

error: runtime/crypto/mod.rs: create\_crypto\_error delegates to boringss

error: bun\_core/fmt.rs: implement format\_ip reborrow (offset-based slic

error: event\_loop/EventLoopTimer.rs: port Timespec::ns from bun.zig

divvied up · 64 claudes

1 fixes2 review1 applies

→ commits land per crate

bun\_runtime0

bun\_bundler0

bun\_sql0

bun\_js\_parser0

bun\_css0

bun\_http0

bun\_interchange0

bun\_sys0

bun\_core0

bun\_string0

bun\_logger0

bun\_uws\_sys0

bun\_alloc0

bun\_collections0

bun\_ptr0

bun\_sourcemap0

bun\_safety0

bun\_glob0

bun\_dotenv0

bun\_router0

bun\_uws0

bun\_io0

bun\_ini0

bun\_lolhtml\_sys0

bun\_test\_runner0

bun\_cares\_sys0

bun\_url0

bun\_picohttp0

bun\_clap0

bun\_boringssl0

bun\_watcher0

bun\_analytics0

bun\_libarchive0

bun\_paths0

bun\_aio0

bun\_options\_types0

bun\_zlib0

bun\_crash\_handler0

bun\_js\_printer0

bun\_resolver0

bun\_http\_jsc0

bun\_install0

How phase D worked, replayed from its 1,610 real commits (May 6, PDT): cargo check wrote ≈16,000 errors to a file, grouped by crate; the workflow divvied them up among 64 Claudes — 16 loops across 4 worktrees, each one Claude fixing, two reviewing, one applying. Every chip is a batch of real commits: it lands on its actual crate and only then do the counters move. Error lines are real commit subjects.

The trickiest class of error was cyclical dependencies.

Our Zig codebase was one compilation unit (effectively one crate). I wanted to split the new Rust codebase into ~100 crates so the Rust would compile faster, but this needed to avoid cyclical dependencies while minimizing changes compared to the original Zig implementation. [My PR](https://github.com/oven-sh/bun/pull/30224) to do this immediately before starting the Rust rewrite was insufficient. Instead of starting over, I ran another workflow to classify where the code with cyclical dependencies should go and write it all down - and then another workflow to do the refactor.

Fixing the cyclical dependencies revealed about 16,000 compiler errors. A massive number for 1 human, but not a crazy number for 64 claudes at once.

To maximize parallelism, the workflow looped over each crate.

* For each crate, run `cargo check`, group the output by file and save the errors to a file
* Fix all the compiler errors within that crate
* 2 adversarial reviewers for the crate's changes
* 1 fixer applies the fixes

To prevent claudes from stepping on each other, `cargo check` only ran at the very start and like the other runs, no `git` until the end.

#### Another false start

Claude interpreted "let's get all the crates to compile" as "stub out the functions with compilation errors". Claude also started adding suspiciously long explanatory comments to document workarounds, so I added this rule for the adversarial reviewers to reject:

If you need a paragraph-long comment to justify why the workaround is OK, the code is wrong — fix the code.

One prompt edit and a few hours later, these things stopped happening.

### Smoke tests[#](#smoke-tests)

Models love saying "smoke tests"

Once `cargo check` passed, getting it to compile and run `bun --version` was next. It had linker errors. Then, it panicked immediately on start.

The next goal was to get it to run `bun test <file>`. Once that worked, we could start running tests! Time for another workflow, looping over bun CLI subcommands:

* Save each failing stacktrace to a file along with its subcommand
* For each failing stacktrace grouped by subcommand, have 1 Claude fix
* 2 adversarial reviewers
* 1 fixer applies the suggestions

### Get the test suite passing locally[#](#get-the-test-suite-passing-locally)

This workflow looped on test files.

Run about 100 random test files sharded to one of 4 worktrees by folder in the codebase. For each failing test, save the stacktrace & errors to a file, 1 implementer proposes a fix, 2 adversarial reviewers, then 1 fixer applies.

#### Even more false starts

Our test suite has lots of memory leak tests and a handful of integration tests that can take more than a minute - for example: a test that runs `next dev` and checks hot module reloading can pick up on changes 100 times. Several of these tests timeout in debug builds.

We also have stress tests that exhaust the max number of TCP sockets on the machine, tests that read & write gigabytes to disk, and tests that spawn ~10k processes.

This needed stronger isolation than "please", so we used `systemd-run` (cgroups) to limit memory & CPU usage and isolate pid namespaces. The machine ran out of disk space and crashed several times anyway.

### Get the test suite passing in CI[#](#get-the-test-suite-passing-in-ci)

Two days after the first CI run, the failing list was down from 972 test files to 23. A day and a half after that, Linux went fully green — and for the first time, it felt like this Rust rewrite was actually going to work.

✻ claude code · dynamic workflowbuildkite · the race to green, by platformWindows finished last · May 11, 6:23 AM PDT

6 / 6 platforms green

▶ replay the racebuild #54202 · Thu, May 14, 12:23 AM PDT

May 8May 9May 10May 11May 12May 13May 14

macOS x64 · 2 shardsbuild #52897: shard failuresbuild #52932: shard failuresbuild #52934: shard failuresbuild #52938: shard failuresbuild #52944: shard failuresbuild #52946: shard failuresbuild #52949: shard failuresbuild #52975: shard failuresbuild #52998: shard failuresbuild #53007: shard failuresbuild #53015: shard failuresbuild #53026: shard failuresbuild #53027: shard failuresbuild #53035: shard failuresbuild #53041: shard failuresbuild #53047: shard failuresbuild #53056: shard failuresbuild #53077: shard failuresbuild #53090: shard failuresbuild #53095: shard failuresbuild #53106: shard failuresbuild #53109: shard failuresbuild #53123: shard failuresbuild #53127: shard failuresbuild #53130: shard failuresbuild #53131: shard failuresbuild #53133: shard failuresbuild #53134: shard failuresbuild #53143: shard failuresbuild #53149: all shards passedbuild #53159: all shards passedbuild #53164: all shards passedbuild #53167: all shards passedbuild #53172: all shards passedbuild #53176: all shards passedbuild #53194: all shards passedbuild #53208: all shards passedbuild #53213: shard failuresbuild #53214: shard failuresbuild #53216: no failures (partial run)build #53222: all shards passedbuild #53229: no failures (partial run)build #53241: all shards passedbuild #53265: all shards passedbuild #53271: all shards passedbuild #53304: shard failuresbuild #53327: shard failuresbuild #53340: shard failuresbuild #53401: shard failuresbuild #53431: shard failuresbuild #53491: all shards passedbuild #53503: all shards passedbuild #53748: shard failuresbuild #53753: all shards passedbuild #53787: all shards passedbuild #53811: all shards passedbuild #53933: no failures (partial run)build #53952: all shards passedbuild #53983: shard failuresbuild #53992: shard failuresbuild #53999: shard failuresbuild #54012: all shards passedbuild #54015: all shards passedbuild #54017: all shards passedbuild #54022: shard failuresbuild #54026: shard failuresbuild #54033: all shards passedbuild #54040: all shards passedbuild #54047: shard failuresbuild #54049: shard failuresbuild #54057: shard failuresbuild #54064: all shards passedbuild #54074: all shards passedbuild #54093: all shards passedbuild #54144: no failures (partial run)build #54161: shard failuresbuild #54186: shard failuresbuild #54189: shard failuresbuild #54196: shard failuresbuild #54202: all shards passed✓

Linux arm64 · 60 shardsbuild #52934: shard failuresbuild #52938: shard failuresbuild #52944: shard failuresbuild #52969: shard failuresbuild #52975: shard failuresbuild #52980: shard failuresbuild #52988: shard failuresbuild #52996: shard failuresbuild #52998: shard failuresbuild #53007: shard failuresbuild #53013: shard failuresbuild #53014: shard failuresbuild #53015: shard failuresbuild #53026: shard failuresbuild #53027: shard failuresbuild #53031: no failures (partial run)build #53032: shard failuresbuild #53035: shard failuresbuild #53041: shard failuresbuild #53047: shard failuresbuild #53056: shard failuresbuild #53059: shard failuresbuild #53077: shard failuresbuild #53083: shard failuresbuild #53086: shard failuresbuild #53090: shard failuresbuild #53095: shard failuresbuild #53106: shard failuresbuild #53109: shard failuresbuild #53123: shard failuresbuild #53127: shard failuresbuild #53130: shard failuresbuild #53131: shard failuresbuild #53133: shard failuresbuild #53134: shard failuresbuild #53135: shard failuresbuild #53143: shard failuresbuild #53149: shard failuresbuild #53159: shard failuresbuild #53164: shard failuresbuild #53167: all shards passedbuild #53172: shard failuresbuild #53176: all shards passedbuild #53188: shard failuresbuild #53194: shard failuresbuild #53208: all shards passedbuild #53212: shard failuresbuild #53213: shard failuresbuild #53214: shard failuresbuild #53216: all shards passedbuild #53222: all shards passedbuild #53229: all shards passedbuild #53236: no failures (partial run)build #53241: all shards passedbuild #53260: all shards passedbuild #53265: all shards passedbuild #53271: all shards passedbuild #53280: no failures (partial run)build #53298: no failures (partial run)build #53304: shard failuresbuild #53327: all shards passedbuild #53340: all shards passedbuild #53360: no failures (partial run)build #53419: shard failuresbuild #53431: shard failuresbuild #53458: no failures (partial run)build #53485: shard failuresbuild #53491: shard failuresbuild #53503: shard failuresbuild #53514: no failures (partial run)build #53570: shard failuresbuild #53583: shard failuresbuild #53599: shard failuresbuild #53748: shard failuresbuild #53753: all shards passedbuild #53762: no failures (partial run)build #53787: no failures (partial run)build #53811: all shards passedbuild #53852: no failures (partial run)build #53863: shard failuresbuild #53893: shard failuresbuild #53914: all shards passedbuild #53933: all shards passedbuild #53952: all shards passedbuild #53983: shard failuresbuild #53992: shard failuresbuild #53999: shard failuresbuild #54008: no failures (partial run)build #54012: all shards passedbuild #54015: all shards passedbuild #54017: all shards passedbuild #54022: shard failuresbuild #54026: all shards passedbuild #54030: shard failuresbuild #54033: all shards passedbuild #54040: all shards passedbuild #54047: shard failuresbuild #54049: shard failuresbuild #54055: shard failuresbuild #54057: shard failuresbuild #54064: all shards passedbuild #54074: all shards passedbuild #54083: no failures (partial run)build #54093: all shards passedbuild #54144: all shards passedbuild #54161: shard failuresbuild #54186: shard failuresbuild #54189: shard failuresbuild #54196: shard failuresbuild #54202: all shards passed✓

Linux x64 · 60 shardsbuild #52934: shard failuresbuild #52938: shard failuresbuild #52944: shard failuresbuild #52969: shard failuresbuild #52975: shard failuresbuild #52988: shard failuresbuild #52996: shard failuresbuild #52998: shard failuresbuild #53007: shard failuresbuild #53013: shard failuresbuild #53014: shard failuresbuild #53015: shard failuresbuild #53026: shard failuresbuild #53027: shard failuresbuild #53032: shard failuresbuild #53033: shard failuresbuild #53035: shard failuresbuild #53041: shard failuresbuild #53047: shard failuresbuild #53056: shard failuresbuild #53059: no failures (partial run)build #53077: shard failuresbuild #53083: no failures (partial run)build #53086: shard failuresbuild #53090: shard failuresbuild #53095: shard failuresbuild #53106: shard failuresbuild #53109: shard failuresbuild #53123: shard failuresbuild #53127: shard failuresbuild #53130: shard failuresbuild #53131: shard failuresbuild #53133: shard failuresbuild #53134: shard failuresbuild #53135: shard failuresbuild #53143: shard failuresbuild #53149: shard failuresbuild #53159: shard failuresbuild #53164: shard failuresbuild #53167: all shards passedbuild #53172: all shards passedbuild #53176: all shards passedbuild #53188: shard failuresbuild #53194: all shards passedbuild #53208: all shards passedbuild #53212: shard failuresbuild #53213: shard failuresbuild #53214: shard failuresbuild #53216: all shards passedbuild #53222: all shards passedbuild #53229: all shards passedbuild #53236: no failures (partial run)build #53241: all shards passedbuild #53260: all shards passedbuild #53265: all shards passedbuild #53271: all shards passedbuild #53280: no failures (partial run)build #53304: shard failuresbuild #53327: all shards passedbuild #53340: all shards passedbuild #53360: no failures (partial run)build #53419: no failures (partial run)build #53431: shard failuresbuild #53458: no failures (partial run)build #53485: shard failuresbuild #53491: all shards passedbuild #53503: all shards passedbuild #53514: no failures (partial run)build #53570: shard failuresbuild #53583: shard failuresbuild #53599: shard failuresbuild #53748: shard failuresbuild #53753: all shards passedbuild #53759: no failures (partial run)build #53781: shard failuresbuild #53787: no failures (partial run)build #53811: all shards passedbuild #53863: shard failuresbuild #53893: shard failuresbuild #53914: all shards passedbuild #53933: shard failuresbuild #53952: all shards passedbuild #53983: shard failuresbuild #53992: shard failuresbuild #53999: shard failuresbuild #54008: no failures (partial run)build #54012: all shards passedbuild #54015: all shards passedbuild #54017: all shards passedbuild #54022: shard failuresbuild #54026: all shards passedbuild #54030: shard failuresbuild #54033: all shards passedbuild #54040: no failures (partial run)build #54047: shard failuresbuild #54049: shard failuresbuild #54055: shard failuresbuild #54057: shard failuresbuild #54064: all shards passedbuild #54074: all shards passedbuild #54083: no failures (partial run)build #54093: all shards passedbuild #54144: all shards passedbuild #54161: shard failuresbuild #54186: shard failuresbuild #54189: shard failuresbuild #54196: shard failuresbuild #54202: all shards passed✓

macOS arm64 · 4 shardsbuild #52897: shard failuresbuild #52929: shard failuresbuild #52932: shard failuresbuild #52944: shard failuresbuild #52975: shard failuresbuild #52996: shard failuresbuild #52998: shard failuresbuild #53007: shard failuresbuild #53013: shard failuresbuild #53014: shard failuresbuild #53015: shard failuresbuild #53026: shard failuresbuild #53027: shard failuresbuild #53032: shard failuresbuild #53035: shard failuresbuild #53041: shard failuresbuild #53047: shard failuresbuild #53056: shard failuresbuild #53059: shard failuresbuild #53077: shard failuresbuild #53095: shard failuresbuild #53109: shard failuresbuild #53123: shard failuresbuild #53127: shard failuresbuild #53130: shard failuresbuild #53131: shard failuresbuild #53133: shard failuresbuild #53134: shard failuresbuild #53135: shard failuresbuild #53143: shard failuresbuild #53149: shard failuresbuild #53159: shard failuresbuild #53164: shard failuresbuild #53167: shard failuresbuild #53172: shard failuresbuild #53176: shard failuresbuild #53188: shard failuresbuild #53194: shard failuresbuild #53208: shard failuresbuild #53212: shard failuresbuild #53213: shard failuresbuild #53214: shard failuresbuild #53216: shard failuresbuild #53222: shard failuresbuild #53229: no failures (partial run)build #53236: no failures (partial run)build #53241: all shards passedbuild #53265: all shards passedbuild #53271: no failures (partial run)build #53280: no failures (partial run)build #53304: shard failuresbuild #53327: no failures (partial run)build #53340: no failures (partial run)build #53360: no failures (partial run)build #53368: shard failuresbuild #53379: shard failuresbuild #53383: shard failuresbuild #53401: shard failuresbuild #53431: shard failuresbuild #53458: shard failuresbuild #53491: no failures (partial run)build #53503: shard failuresbuild #53570: shard failuresbuild #53583: shard failuresbuild #53599: shard failuresbuild #53601: shard failuresbuild #53748: shard failuresbuild #53753: all shards passedbuild #53757: no failures (partial run)build #53759: no failures (partial run)build #53787: no failures (partial run)build #53811: all shards passedbuild #53952: no failures (partial run)build #53992: shard failuresbuild #53999: shard failuresbuild #54007: no failures (partial run)build #54012: all shards passedbuild #54015: shard failuresbuild #54017: all shards passedbuild #54022: shard failuresbuild #54026: no failures (partial run)build #54030: shard failuresbuild #54033: all shards passedbuild #54040: shard failuresbuild #54047: shard failuresbuild #54049: shard failuresbuild #54055: shard failuresbuild #54057: shard failuresbuild #54064: shard failuresbuild #54074: shard failuresbuild #54093: shard failuresbuild #54161: shard failuresbuild #54186: shard failuresbuild #54189: shard failuresbuild #54196: shard failuresbuild #54202: all shards passed✓

Windows x64 · 8 shardsbuild #53090: shard failuresbuild #53094: shard failuresbuild #53095: shard failuresbuild #53106: shard failuresbuild #53109: shard failuresbuild #53123: shard failuresbuild #53127: shard failuresbuild #53130: shard failuresbuild #53131: shard failuresbuild #53133: shard failuresbuild #53134: shard failuresbuild #53135: shard failuresbuild #53143: shard failuresbuild #53149: shard failuresbuild #53159: shard failuresbuild #53164: shard failuresbuild #53167: shard failuresbuild #53172: shard failuresbuild #53176: shard failuresbuild #53188: shard failuresbuild #53194: shard failuresbuild #53208: shard failuresbuild #53212: shard failuresbuild #53213: shard failuresbuild #53214: shard failuresbuild #53216: shard failuresbuild #53222: shard failuresbuild #53229: shard failuresbuild #53236: shard failuresbuild #53241: shard failuresbuild #53260: shard failuresbuild #53265: shard failuresbuild #53271: shard failuresbuild #53280: shard failuresbuild #53298: shard failuresbuild #53304: shard failuresbuild #53327: all shards passedbuild #53340: all shards passedbuild #53360: no failures (partial run)build #53419: shard failuresbuild #53431: shard failuresbuild #53458: shard failuresbuild #53470: no failures (partial run)build #53485: shard failuresbuild #53491: no failures (partial run)build #53503: shard failuresbuild #53514: no failures (partial run)build #53565: no failures (partial run)build #53570: shard failuresbuild #53599: shard failuresbuild #53745: shard failuresbuild #53748: shard failuresbuild #53753: shard failuresbuild #53757: shard failuresbuild #53759: shard failuresbuild #53762: shard failuresbuild #53769: shard failuresbuild #53781: shard failuresbuild #53787: shard failuresbuild #53808: shard failuresbuild #53811: shard failuresbuild #53852: shard failuresbuild #53863: shard failuresbuild #53883: shard failuresbuild #53893: shard failuresbuild #53914: all shards passedbuild #53933: all shards passedbuild #53952: all shards passedbuild #53973: no failures (partial run)build #53983: shard failuresbuild #53992: shard failuresbuild #53999: shard failuresbuild #54002: no failures (partial run)build #54004: no failures (partial run)build #54007: shard failuresbuild #54008: no failures (partial run)build #54012: all shards passedbuild #54015: all shards passedbuild #54017: all shards passedbuild #54022: shard failuresbuild #54026: all shards passedbuild #54030: all shards passedbuild #54033: all shards passedbuild #54040: all shards passedbuild #54047: shard failuresbuild #54049: shard failuresbuild #54055: shard failuresbuild #54057: shard failuresbuild #54064: all shards passedbuild #54074: all shards passedbuild #54083: all shards passedbuild #54093: all shards passedbuild #54144: shard failuresbuild #54161: shard failuresbuild #54186: shard failuresbuild #54189: shard failuresbuild #54196: shard failuresbuild #54202: all shards passed✓

Windows arm64 · 8 shardsbuild #53090: shard failuresbuild #53095: shard failuresbuild #53106: shard failuresbuild #53109: shard failuresbuild #53123: shard failuresbuild #53127: shard failuresbuild #53130: shard failuresbuild #53131: shard failuresbuild #53134: shard failuresbuild #53135: shard failuresbuild #53149: shard failuresbuild #53159: shard failuresbuild #53164: shard failuresbuild #53167: shard failuresbuild #53172: shard failuresbuild #53176: shard failuresbuild #53188: shard failuresbuild #53194: shard failuresbuild #53208: shard failuresbuild #53212: shard failuresbuild #53213: shard failuresbuild #53214: shard failuresbuild #53216: shard failuresbuild #53222: shard failuresbuild #53229: shard failuresbuild #53236: no failures (partial run)build #53241: shard failuresbuild #53260: shard failuresbuild #53265: shard failuresbuild #53271: shard failuresbuild #53304: shard failuresbuild #53327: all shards passedbuild #53340: all shards passedbuild #53360: no failures (partial run)build #53419: no failures (partial run)build #53431: shard failuresbuild #53458: no failures (partial run)build #53485: shard failuresbuild #53491: no failures (partial run)build #53503: no failures (partial run)build #53599: shard failuresbuild #53748: shard failuresbuild #53753: shard failuresbuild #53757: shard failuresbuild #53759: shard failuresbuild #53762: shard failuresbuild #53787: shard failuresbuild #53808: shard failuresbuild #53811: shard failuresbuild #53852: shard failuresbuild #53863: shard failuresbuild #53883: shard failuresbuild #53893: shard failuresbuild #53914: no failures (partial run)build #53933: all shards passedbuild #53952: all shards passedbuild #53983: shard failuresbuild #53992: shard failuresbuild #53999: shard failuresbuild #54007: no failures (partial run)build #54012: all shards passedbuild #54015: all shards passedbuild #54017: all shards passedbuild #54022: shard failuresbuild #54026: all shards passedbuild #54030: no failures (partial run)build #54033: all shards passedbuild #54040: all shards passedbuild #54047: shard failuresbuild #54049: shard failuresbuild #54055: no failures (partial run)build #54057: shard failuresbuild #54064: all shards passedbuild #54074: all shards passedbuild #54083: no failures (partial run)build #54093: all shards passedbuild #54144: shard failuresbuild #54161: shard failuresbuild #54186: shard failuresbuild #54189: shard failuresbuild #54196: shard failuresbuild #54202: all shards passed✓

✓ all 6 platforms green · build #54202 → merged

Every CI build's test shards, by platform, across 135 builds that ran tests (420 mined from BuildKite). Bright green: every shard passed. Dim green: no failures, but the run was cut short (superseded). Red: at least one shard failed. Each lane is stamped when its full suite first passes — Linux's 60 shards were green almost a full day before Windows. Platforms kept wobbling red until the last failing tests fell; the final all-green build was #54202.

The rest of the time leading up to merging it was straightforward. A workflow that looped on fixing CI test failures for each platform until there were no more test failures. Several workflows for Windows-related cleanup, to deduplicate code, to reduce unsafe usage, and to generally clean up some code.

### Merging the Rust rewrite[#](#merging-the-rust-rewrite)

Once 100% of Bun's test suite passed in CI on all platforms (and I manually verified the tests were in fact running and not being skipped), I ran a bunch of commands locally to test things - and then I pressed the merge button.

Merging into `main` isn't a versioned release. At this point, I was confident enough to move forward and commit to the rewrite, but not yet confident enough to release it.

### Stats[#](#stats)

At peak, we were running 4 of these workflows at once each in a separate worktree, each with 16 Claudes per workflow. About 64 Claudes at a time.

git log · claude/phase-a-portpeak: 58 commits in one minute

+0

lines written, rewrites included

▶ replay 11 days in 30sMon, May 4, 7:05 AM PDT

first 100-file draft batchPR #30412 openedmerged

All 6,502 commits (merges excluded), replayed. Pink bars are mostly new code; cyan bars are mostly deletion. The line counter counts every rewrite along the way — the diff that landed was +1,009,272. The log is real commit messages.

#### 0 tests skipped or deleted

11 days (May 3 → merged May 14) · 6,778 commits

| Platform | expect() calls | Tests | Files |
| --- | --- | --- | --- |
| Debian 13 x64 | 1,386,826 | 60,624 | 4,174 |
| macOS 14 arm64 | 1,259,953 | 58,850 | 4,175 |
| Windows 2019 x64 | 1,007,544 | 57,337 | 4,173 |

Pre-merge, this took 5.9 billion uncached input tokens, 690 million output tokens, and 72 billion cached input token reads — around $165,000 at API pricing. By hand, I think this would've taken 3 engineers with full context on the codebase about a year, during which time we wouldn't be able to improve Node.js compatibility, fix bugs, fix security issues or implement new features. We never would've done that. The realistic alternative was to do nothing and keep fixing the bugs at the top of this post forever.

This is the bleeding edge of what's possible today. I used a pre-release version of [Claude Fable 5](https://www.anthropic.com/news/claude-fable-5-mythos-5), a Mythos-class model. Claude Code's dynamic workflows kept 64 Claudes running for 11 days (I would've had to write my own harness to pull this off otherwise).

### The work continues[#](#the-work-continues)

Since merging the Rust port, we've completed 11 rounds of security review from [Claude Code Security](https://claude.com/product/claude-security) and addressed the findings.

We've also added 24/7 coverage-guided fuzzing of every parser in Bun — JavaScript, TypeScript, JSX, CSS, JSON5, JSONC, TOML, YAML, Markdown, INI, Bun Shell scripts, semver ranges, .patch files, and CSS colors. The fuzzer automatically sends the bugs it finds to Claude to submit a PR reproducing & fixing, and humans review the PRs. So far, it's executed our parsers 100 billion times which has led to around 15 PRs.

At the time of writing, about 4% of Bun's Rust code sits inside an `unsafe` block (~13,000 `unsafe` keywords across ~27,000 lines / ~780,000 lines), and 78% of those blocks are a single line — a pointer that came from C++, or one call into a C library. I expect this number to go down over time as we refactor from a faithful Zig port (which had no greppable `unsafe` keyword) to idiomatic Rust, but we are going to continue using C & C++ libraries like JavaScriptCore so it will always have more `unsafe` than pure Rust projects.

### Porting mistakes[#](#porting-mistakes)

The focus of the Rust rewrite is stability, but it would be impossible to ship a massive change like this and introduce zero regressions.

This rewrite introduced 19 known regressions, each of which has been fixed.

Most of the regressions came from code that's syntactically identical in both languages but semantically different.

#### Side effect inside `debug_assert!`

These two snippets look similar but behave differently. Zig's `assert` is a function, so its argument runs in every build. Rust's `debug_assert!` is a macro, so in release builds the whole expression is erased, including the `insert_stale` call.

`insert_stale` adds a file to the frontend dev server's hot reload graph. In release builds it stopped running, and HMR broke in certain cases for projects with HTML routes that use React while a hot reloaded file gets invalidated: `Cannot destructure property 'isLikelyComponentType' of 'k'`. Debug builds worked. [#30678](https://github.com/oven-sh/bun/issues/30678)

#### Slices of odd length

Bun's Zig helper `reinterpretSlice(u16, bytes)` (predating builtin casts supporting slices) used `@divTrunc` and ignored a trailing odd byte. `bytemuck::cast_slice` panics on it instead. `Blob.text()` on a UTF-16 byte order mark followed by an odd number of bytes stopped returning a string and panicked the process. We went back to ignoring the odd byte: `&buf[..buf.len() & !1]`. [#31188](https://github.com/oven-sh/bun/issues/31188)

#### Bounds checks

On macOS & Linux, we compiled Bun's Zig code with `ReleaseFast`, which removes bounds checks. Rust's release builds keep them.

Bun's module resolver interns long filenames into a global list that spills into overflow blocks. The original Zig code sized each block at `count / 4`, or 2048. The port left a placeholder:

That lowered the ceiling from 8.4 million interned filenames to 270,272, which real projects hit, and made a `ptrs[4095]` off-by-one we ported from Zig reachable. Rust panicked instead of writing past the end. Zig would also panic in this case, if we used `ReleaseSafe` (we only did on Windows). [#31503](https://github.com/oven-sh/bun/issues/31503)

#### `comptime` format strings

`Output.pretty` rewrites `<r>` and `<d>` color markers into ANSI escapes. In Zig, `fmt` is `comptime`, so the markers are gone before the arguments are substituted. Rust functions don't have comptime parameters, so `Output::pretty` only ever saw the finished string, and rewrote markers over the arguments too.

`bun update -i` prints package names as [OSC 8](https://gist.github.com/egmontkob/eb114294efbcd5adb1944c9f3cb5feda) hyperlinks, terminated by `ESC \`. That backslash sits right before the `<` of the trailing `<r>`, the marker parser eats it, and the `r` prints as text.

[![](/images/update-interactive-r.png)](/images/update-interactive-r.png)it should say oxfmt, not oxfmtr

In Rust it has to be a macro: `bun_core::pretty!("<r>{}<r>", hyperlink)`. [#30693](https://github.com/oven-sh/bun/issues/30693)

## Bun is better in Rust[#](#bun-is-better-in-rust)

So far, Bun v1.4.0 fixes 128 bugs that reproduce in v1.3.14. These range from memory leaks to crashes to miscolored help text.

### Reduced memory usage[#](#reduced-memory-usage)

Rust has a powerful language-level tool for cleaning up memory: `Drop`. When `Drop` is implemented, the `drop` function is automatically called every time the value goes out of scope.

In Zig, `defer` can be used to run code at the end of a scope:

In Zig, `defer` needs to be added to every individual call site that might need cleanup. It's easy to end up forgetting to clean up (a memory leak), or to run cleanup code twice in rarely-reached error handling code (a double-free). In Rust, `Drop` runs automatically when the value is no longer accessible - trading "no hidden control flow" for preventing a common footgun.

`Drop` fixed several memory leaks in Bun related to file paths in error handling code.

#### We fixed every instrumentable memory leak

We improved Bun's [LeakSanitizer](https://clang.llvm.org/docs/LeakSanitizer.html) integration to track all [native code memory allocations](https://github.com/oven-sh/bun/pull/30875).

Here's an example: every in-process `Bun.build()` call leaked several megabytes of memory — parsed source text and AST symbol tables that outlived the build they belonged to.

In Bun v1.3.14, every build leaks about 3 MB, forever — tools like dev servers that bundle on every request eventually run out of memory. In Bun v1.4.0, memory levels off:

| Builds | Bun v1.3.14 | Bun v1.4.0 |
| --- | --- | --- |
| 500 | 1,914 MB | 526 MB |
| 1,000 | 3,506 MB | 586 MB |
| 1,500 | 5,097 MB | 608 MB |
| 2,000 | 6,745 MB | 609 MB |

A [previous attempt](https://github.com/oven-sh/bun/pull/24741) to do this in Zig was not merged because the lack of an equivalent of Drop made it more difficult to feel confident merging.

### Smaller binary size[#](#smaller-binary-size)

The initial changes in the Rust rewrite reduced binary size by 3.8 MB on Windows, 5.5 MB on macOS, and 6.8 MB on Linux. This is largely because we used too much `comptime` in our Zig code.

After that initial shrinkage, the team explored more opportunities for binary size reduction using linker optimizations like Identical Code Folding, removing unused data from ICU, and lazily decompressing small parts of libicu with a zstd dictionary on-demand.

Combined with the Rust rewrite, ICU changes, and identical code folding, **Bun's binary size shrinks by ~20%** on Linux & Windows.

| Version | Platform | Size |
| --- | --- | --- |
| Bun v1.4.0 (canary) | Windows | 76 MB |
| Bun v1.3.14 | Windows | 94 MB |
| Bun v1.4.0 (canary) | Linux | 70 MB |
| Bun v1.3.14 | Linux | 88 MB |

### Reduced stack space usage[#](#reduced-stack-space-usage)

The TOML parser, and all of the other recursive-descent parsers in Bun (JSON, YAML, JavaScript, TypeScript, and more) now use less stack space.

This caused some test failures before merging the Rust rewrite:

Rust's LLVM IR codegen emits LLVM's [`llvm.lifetime.start`](https://llvm.org/docs/LangRef.html#llvm-lifetime-start-intrinsic) and [`llvm.lifetime.end`](https://llvm.org/docs/LangRef.html#llvm-lifetime-end-intrinsic) intrinsics for stack variables when they are no longer in use, which lets LLVM reuse stack space slots. This lets large functions with nested scopes use significantly less stack space.

Previously, we manually worked around [an open issue](https://github.com/ziglang/zig/issues/23475) by [refactoring particularly large functions](https://github.com/oven-sh/bun/pull/15993) into many smaller functions.

### 2% - 5% faster[#](#2-5-faster)

Rust supports cross-language link-time optimization between C/C++ and Rust, which enables inlining across programming languages (how cool is that!!).

We benchmarked Bun v1.3.14 against Bun v1.4.0 on Linux x64 (EC2, Xeon Platinum 8488C). HTTP throughput measured with [oha](https://github.com/hatoo/oha) against hello-world servers, app workloads measured with [hyperfine](https://github.com/sharkdp/hyperfine).

**HTTP throughput (req/s, avg of 3 rounds)**

| server | Bun v1.3.14 | Bun v1.4.0 | Δ |
| --- | --- | --- | --- |
| Bun.serve | 169.6k | 177.7k | +4.8% |
| node:http | 103.8k | 108.5k | +4.5% |
| Elysia | 158.9k | 163.3k | +2.8% |
| express | 64.5k | 66.6k | +3.2% |
| fastify | 91.5k | 95.9k | +4.8% |

**Apps / CLI (hyperfine)**

| workload | Bun v1.3.14 | Bun v1.4.0 | Δ |
| --- | --- | --- | --- |
| next build | 13.62 s | 13.03 s | +4.5% |
| vite build (tsc + vite) | 1.69 s | 1.65 s | +2.2% |
| tsc -b --force | 0.94 s | 0.89 s | +4.7% |

## Production[#](#production)

Prisma launched the [Prisma Compute](https://www.prisma.io/blog/bun-rust-rewrite-prisma-compute) public beta on Bun's Rust rewrite.

"We ran into memory leaks and a connection pool that couldn't recover after a VM was paused and resumed. When the Rust rewrite appeared, we tested it against the same failure modes. It handled them perfectly." - Alexey Orlenko

Claude Code v2.1.181 (released June 17th) and later use the Rust port of Bun. Startup got 10% faster on Linux but otherwise, barely anyone noticed. Boring is good.

[![Claude Code startup time from production telemetry (Linux p50): v2.1.179 at 517ms vs v2.1.181, the first release on Rust Bun, at 464ms — 10% faster](/images/claude-code-rust-bun-startup.webp)](/images/claude-code-rust-bun-startup.webp)

## Shipping[#](#shipping)

Bun v1.3.14 was the last version of Bun written in Zig. Bun v1.4.0 will be the first version of Bun written in Rust. It's available in canary now - please report any issues you find:

## Maintainability[#](#maintainability)

For myself and the team, our new Rust codebase feels very similar to the old Zig codebase. For example, here's a snippet of the original Zig code and the new Rust code:

Anyone who understands the original Zig code understands the mechanically translated Rust code. I reviewed the original Rust rewrite PR by checking the adversarial code review agents were correctly catching discrepancies between the Zig code and the Rust code, that they were ensuring the porting guide and lifetime guide were being followed, and also manually reading a lot of the code myself side-by-side with the Zig vs Rust.

## What's next[#](#what-s-next)

Bun v1.4 makes Bun faster, smaller, use less memory and gives the team incredibly powerful tools for systematically improving stability going forward: Rust's borrow checker, Miri (which runs for a growing chunk of code in CI), LeakSanitizer, and 24/7 coverage-guided fuzzing for parsers. There's still [more to refactor](https://bun.com/bun-unsafe-audit), but things are off to a great start.

This Rust rewrite would've taken a team of engineers with full-context on the codebase a year of work. With 1 engineer using Fable & closely monitoring Claude Code, we went from start to 100% of the test suite passing on all platforms in 11 days.

One engineer can do a lot more today than a year ago.
