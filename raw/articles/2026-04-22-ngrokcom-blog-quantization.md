---
title: Quantization from the ground up
type: source
source_type: article
url: https://ngrok.com/blog/quantization
fetched: 2026-04-22
---

# Quantization from the ground up

[Qwen-3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next) is an 80 billion
parameter model **159.4GB** in size. That's roughly how much RAM you
would need to run it, and that's before thinking about long context windows.
*This is not considered a big model.* Rumors have it that frontier models have
over 1 trillion parameters, which would require at least **2TB** of RAM. The
last time I saw that much RAM in one machine was *never*.

But what if I told you we can make LLMs 4x smaller and 2x faster, enough to run very capable models on your laptop, all while losing only 5-10% accuracy.

That's the magic of quantization.

**In this post, you are going to learn:**

* How a model's parameters make it so big
* How floating point precision works and how models sacrifice it
* How to compress floats using quantization
* How to measure model quality loss after quantization

If you already know what parameters are and how floats are stored, feel free to [skip straight to
quantization](#what-is-quantization).

## What makes large language models so large?

Parameters, also called "weights," are the majority of what an LLM *is* when it's in memory or on disk. In
my [prompt caching](https://ngrok.com/blog/prompt-caching) post I wrote that LLMs are an "enormous graph of billions of carefully arranged
operations." What do those graphs look like? Let's start with the simplest example: 1 input, 1
parameter, 1 output.

It doesn't look like much, but this is the fundamental building block of modern AI.
It takes the input of `2.0`, multiplies it by the parameter `0.5`, and gets the output `1.0`.

LLMs, though, are much bigger. They have billions of these parameters in practice. One of the ways they get so big is that they have "layers." Here's how that looks.

These two nodes in the middle are a layer. They both show `1.0` because both connections have a parameter of `0.5`, and so they are the result of `2.0 * 0.5`. Every connection between two nodes gets a parameter, so we have 4 in total above. When 2 connections end at the same node, the values are added together. So to get the output of `1.5` we add together `1.0 * 1.0` and `0.5 * 1.0`.

Play with the slider next to the input below to get a feel for how it affects the output.

Use the input slider to change the input value. The output updates automatically.

Output value 2.5

This is still only 6 parameters, we're a long way from the billions seen in modern LLMs. The example below has 2 inputs, 3 layers, and 2 outputs. In total it has 64 parameters, hover or tap a node to see its parameters.

2.01.02.02.32.31.34.04.45.16.54.23.414.19.59.213.313.425.3

2.01.02.02.32.31.34.04.45.16.54.23.414.19.59.213.313.425.3

Modern LLMs have hundreds of thousands of inputs and outputs. They have many dozens of layers, each with thousands of nodes, all densely connected together. This all multiplies out to result in *billions*, sometimes *trillions* of parameters.

## How do computers store numbers?

Computers work in `1`s and `0`s, called "bits." Here's what a whole number, or
"integer," looks like when stored as bits. Drag the slider to change the value.
You can also tap on individual bits to flip them.

### unsigned int8

1286432168421

010

011

010

010

010

010

010

010

=64

Each bit represents a power-of-2 number which when summed together gives the
final answer.

Integers are nice to work with because they are *discrete*. Between 1 and 3
there is exactly one number: 2. This is great for computers, they can represent
discrete values no problem.

It gets trickier when you start thinking about decimal places. How many decimal
place numbers are there between 1 and 3? There are an infinite number of them.
This is not good for computers, because computers can't represent an infinite
number of things.

What computers do is they compromise. They promise to be accurate up to so many
significant figures, and anything after that is best-effort.

For example, 32-bit floating point numbers span the range ±3.40×1038
with 7 significant figures of accuracy. They do this by dividing the 32 bits up
into 3 parts: 1 sign bit, 8 exponent bits, and 23 significand bits. More exponent bits results in a larger range, while more significand bits results in more significant figures of accuracy.

Play with the example below. Sliding left and right explores the full range of values. The plus and minus buttons at the top jump to the next higher or lower representable number. The 7 significant figures that are promised to be accurate are underlined. Press reset to return to the default value of 1.5.

### float32

Decrement float32 bit patternIncrement float32 bit pattern

Reset float32 visualization

sexponentsignificand

010

010

011

011

011

011

011

011

011

011

010

010

010

010

010

010

010

010

010

010

010

010

010

010

010

010

010

010

010

010

010

010

1.5

Whenever you press plus, it takes you to the *next highest
representable value*. Pay attention to the digit *after* the underlined digits, it will sometimes skip over a number. This is the precision compromise in action.

Pressing plus when you're on a very small
value moves you forward a small amount. Pressing it when you're on a very large
value moves you forward a larger amount. The size of the jump changes depending on where
you are in the range, the values *are not evenly distributed*.

To illustrate this point further, below is a histogram. Each bar shows you a
slice of the 32-bit floating point range. There are over 2 billion unique values
that can be represented between -0.5 and 0.5.

### Distribution of 32-bit float values

Histogram of representable float32 values between negative ten and ten. Most finite values cluster close to zero. Use the controls below to switch the y-axis between linear and log scale and to view absolute counts or percentages.

A lot of the representable 32-bit floats are small values. This is fantastic for LLMs, because parameters also tend to be small. Small parameters have been found to result in models that generalise better to problems they haven't seen before, so models are rewarded during training for making parameters small.

Below is another histogram, and was created by downloading 6 popular open source
models and counting their parameter values. Almost all parameters
are very close to 0.

### Distribution of model parameter values

Line chart comparing parameter distributions for six models. Most parameter values cluster near zero. Use the range and value display controls to inspect different portions of the distribution.

So most model parameters sit in the range of floats that can be
most precisely represented. There *are* a very small number of outliers, though.
I'll come back to that later.

## Can we use smaller floats?

Do language models actually *need* 32-bit floats? They don't need a wide range,
as you can see from the parameter distribution histogram above, and
do they *really* need 7 significant figures of accuracy?

The answer is no, LLMs work just fine with smaller, less accurate floats. Below is an
example of a 16-bit float. It works just like the 32-bit float, except it only
has 5 exponent bits and 10 significand bits.
It can represent 3 significant figures of precision, and has a range of ±65504.
It also takes up half as much RAM and disk as a 32-bit float.

### float16

Decrement float16 bit patternIncrement float16 bit pattern

Reset float16 visualization

sexponentsignificand

010

010

011

011

011

011

011

010

010

010

010

010

010

010

010

010

1.5

We can mix and match the number of exponent and significand bits to get different precision/range tradeoffs.
For example, the Google Brain team created the `bfloat16` format, which has 8 exponent bits but only 7 significand bits. This gives it a very wide range, but only 2 significant figures of precision.

### bfloat16

Decrement bfloat16 bit patternIncrement bfloat16 bit pattern

Reset bfloat16 visualization

sexponentsignificand

010

010

011

011

011

011

011

011

011

011

010

010

010

010

010

010

1.5

Google found that 2 significant figures is sufficient for creating LLMs, and
having this extremely wide range means they don't have to worry about any
calculations overflowing, which can happen in larger LLMs using smaller floats.

Some more extreme examples that are seen less often are `float8` and `float4`. Below are just example configurations of these floats, in the wild people will mix and match the number of exponent and significand bits to suit their needs.

### float8

Decrement float8 bit patternIncrement float8 bit pattern

Reset float8 visualization

sexponentsignificand

010

010

011

011

011

011

010

010

1.5

### float4

Decrement float4 bit patternIncrement float4 bit pattern

Reset float4 visualization

sexponentsignificand

010

010

011

011

1.5

Another way to visualise the accuracy of these formats is to see how well they
approximate a sine wave. Use the zoom buttons underneath the graph below to see
how they differ.

### Different floats approximating sine

This chart compares an ideal sine wave with quantized approximations for float32, float16, bfloat16, float8, and float4. Lower-precision formats appear more step-like and drift further from the smooth curve. Use the format buttons to show or hide individual lines, and use the zoom control to inspect the same section at one, thirty, or two hundred times magnification.

━float32━float16━bfloat16━float8━float4

Let's talk about how we can use this knowledge to make models smaller.

## What is quantization?

Quantization is the process of taking values from a large range, and packing
them into a smaller range. It is a form of **lossy compression**.

When we convert between, e.g., a `float16` and a `float8`, we tend to round to
the *closest representable value*. We're taking values in the `float16` range
and mapping them to the nearest `float8` value. This is called
"round-to-nearest" and is one of many types of quantization.

Slide the vertical bar along the number lines below. As you move the bar, the
closest representable value for each float size is shown.

Float comparison slider. Use left and right arrow keys for small adjustments. Hold Shift for larger adjustments. Use Page Up and Page Down for larger jumps, and Home or End to move to the minimum or maximum.

This is a very simple way to take a value in one range and represent it inside a
smaller range. However, it's not a good idea to do this for LLMs.

Take a look at the small model below. See how the parameters and output change as you round from `bfloat16` to `float8` and `float4`.

### Quantization by rounding

Use the input slider to change the input value. The output updates automatically.

Output value 0.20

Rounding to `float8` isn't too bad, but rounding to `float4` completely breaks
the model. This is because some of the parameters are now 0.
Because there is no path from input to output that
doesn't multiply by 0, the output is always 0.

This happens because we're being inefficient about how we squish values into the 4 bits we have available. A `float4` goes from -3 to 3, but our parameters go from `-0.89` to `0.16`.

On top of that, `float4` can also represent `Infinity` and `NaN`. These aren't
useful to us when quantizing.

Let's look at how we can more efficiently use the 16 values a 4-bit number gives
us.

### Symmetric quantization

Instead of going from -3 to 3 like `float4` does, what if we used a tighter
range that better fits our data?

One of the ways we can do this is by *scaling* our data into a new range. For
example, if I had data in the range of -14 to 14, and I wanted to fit it into -7
to 7, I could divide by 2.

-1414-7-6-5-4-3-2-101234567-14-12-8-4048121414-14-7-6-5-4-3-2-101234567-14-12-8-40481214

Then to get back to my original value from the scaled value, all I need to do is
multiply it by 2. Any odd value would become unrepresentable in this scheme, as
they would have to be rounded to the nearest integer. For example, `5 / 2 = 2.5`
would round up to `3` and then dequantize to `3 * 2 = 6`. This is what makes
quantization lossy.

-1414-7-6-5-4-3-2-101234567-1451414-14-7-6-5-4-3-2-101234567-14514

We can apply this process to any set of values, we just need to find the right
scaling factor. We do by finding the largest absolute value in our dataset, and
dividing it by the largest value in our quantized range. For our parameters that
would be `0.89 / 7`. Here's what the code would look like in JavaScript.

Copy code

```
1function quantize({ values, bits }) {2	// Assuming:3	//   values = [-0.89, 0.16, 0.08, -0.13, 0.16, -0.54]4	//   bits = 45	const vmax = Math.max(...values.map(Math.abs)); // 0.896	const qmax = 2 ** (bits - 1) - 1; // 77	const scale = vmax / qmax; // 0.127142857142857148	return {9		values: values.map((v) => Math.round(v / scale)),10		scale,11	};12}13 14function dequantize({ values, scale }) {15	return values.map((v) => v * scale);16}
```

The code below applies this `quantize` function to our parameter values from the small model we saw above.

Copy code

```
1const values = [-0.89, 0.16, 0.08, -0.13, 0.16, -0.54];2const quantized = quantize({ values, bits: 4 });3// { values: [-7, 1, 1, -1, 1, -4], scale: 0.12714285714285714 }
```

Our small floats have been mapped into the quantized integer range. Here's how
that mapping looks visually:

-0.890.89-7-6-5-4-3-2-101234567-0.890.160.08-0.13-0.540.89-0.89-7-6-5-4-3-2-101234567-0.890.160.08-0.13-0.54

And then we can `dequantize` the values, multiplying them by the `scale` we got
back from `quantize`, to get back to the original floating point range:

Copy code

```
1const dequantized = dequantize(quantized);2// [-0.89, 0.1271, 0.1271, -0.1271, 0.1271, -0.5086]
```

And again, how that looks visually:

-7-6-5-4-3-2-101234567-0.890.89-0.890.12710.1271-0.1271-0.5086-7-6-5-4-3-2-1012345670.89-0.89-0.890.12710.1271-0.1271-0.5086

Comparing those values to the originals we can see that they're mostly pretty
close!

We've made our model 4x smaller, 16-bit to 4-bit, and on average the
dequantized values are off by about 18%. Not bad!

Let's have a look at how our small model performs using symmetric quantization.
Play with the slider and flip between `bfloat16` and `quantized 4-bit` and note
the differences.

### Symmetrically quantized model

Use the input slider to change the input value. The output updates automatically.

Output value 0.20

`quantized 4-bit` has the final output off by about 30%. This is a
huge improvement over the always-zero behaviour of rounded `float4`, especially
when you remember that this quantized model will require 4x less RAM than the
original.

But... we can still do better.

### Asymmetric quantization

Symmetric quantization is called that because 0 is always in the middle. We pick
a scale and squish our values around 0. Let's take a closer look at our
symmetrically quantized values.

-0.890.89-7-6-5-4-3-2-101234567-0.890.160.08-0.13-0.540.89-0.89-7-6-5-4-3-2-101234567-0.890.160.08-0.13-0.54

There's a lot of wasted space on the positive side because our maximum value is
`0.16`, whereas our minimum value is `-0.89`. Because of symmetry, the positive
range goes up to `0.89`, leaving a large gap between `0.16` and `0.89`. We
aren't efficiently using the space.

The idea behind *asymmetric* quantization is to fix this by allowing uneven
ranges. Instead of squishing around 0, asymmetric quantization squishes around
the midpoint of your data, and works out a "zero point" to offset by during
dequantization.

Copy code

```
1function quantize({ values, bits }) {2	// Assuming:3	//   values = [-0.89, 0.16, 0.08, -0.13, 0.16, -0.54]4	//   bits = 45	const vmax = Math.max(...values); // 0.166	const vmin = Math.min(...values); // -0.897	const qmax = 2 ** (bits - 1) - 1; // 78	const qmin = -(2 ** (bits - 1)); // -89	const scale = (vmax - vmin) / (qmax - qmin); // 0.0710	const zero = qmin - Math.round(vmin / scale); // 511	return {12		values: values.map((x) => Math.round(x / scale + zero)),13		scale,14		zero,15	};16}
```

Let's run our familiar parameters through this and see what we get.

Copy code

```
1values = [-0.89, 0.16, 0.08, -0.13, 0.16, -0.54];2const quantized = quantize({ values, bits: 4 });3// { values: [ -8, 7, 6, 3, 7, -3 ], scale: 0.07, zero: 5 }
```

Here's how the mapping looks visually. Our new asymmetric `quantize` function
has decided that `5` should be the zero point.

-0.890.16-8-7-6-5-4-3-2-101234567-0.890.160.08-0.13-0.540.16-0.89-8-7-6-5-4-3-2-101234567-0.890.160.08-0.13-0.54

The `dequantize` function is only slightly more complicated than the symmetric
version, this time requiring a subtraction as well as a multiplication.

Copy code

```
1function dequantize({ values, scale, zero }) {2	return values.map((x) => scale * (x - zero));3}4 5dequantize(quantized);6// [-0.91, 0.14, 0.07, -0.14, 0.14, -0.56]
```

How does this compare to the average error with symmetric quantization?

Much better! 10% less error for the same number of bits. Let's see how it does
on our model.

### Asymmetrically quantized model

Use the input slider to change the input value. The output updates automatically.

Output value 0.20

The final output is still off by around 10%, but a really nice
improvement over symmetric quantization.

This is what's happening to the parameters of models when they're
quantized down to sizes that are possible to run on your laptop. Instead of
floats, small integers are what get stored and loaded into memory. When the time
comes to use the quantized values, to generate an answer to a question for
example, the values are dequantized on the fly. You might think this sounds
slower, but we'll see later on that this actually ends up being *faster* as well
as smaller.

## How is quantization applied in practice?

Are people taking their LLMs with hundreds of billions of parameters, finding the the largest and smallest of all of them,
and quantizing the model in one go?

No.

I hinted at the reason for this earlier on. Let's take another look at that graph of parameters from 6 different open weight models, except this time let's look at the long tail of outlier values.

### Outlier parameters

Line chart comparing the outlier tails of model parameter distributions. Outliers are rare and only appear in a small number of bins. Use the range and y-axis scale controls to inspect the long tail.

All of the models have a small number of outlier parameters. Ones
that are much larger or smaller than most others. Outliers are *really bad* for
quantization. Look what happens when we try to quantize our parameters from earlier with a single outlier of `10` added to them:

-0.8910-8-7-6-5-4-3-2-101234567-0.890.160.08-0.13-0.541010-0.89-8-7-6-5-4-3-2-101234567-0.890.160.08-0.13-0.5410

Everything gets squished into a small number of buckets and average error goes through the roof. If we quantized the entire model in one go, we'd destroy it. **What's done in practice is quantization in blocks**, usually around 32-256 parameters at a time. This way, the impact of outliers is contained.

To dequantize, we need to save the `scale` value for symmetric, and the `scale` + `zero` for asymmetric. These get stored alongside each block, and are
considered overhead. Choosing a larger block size reduces this overhead, but
larger blocks have a wider range of values on average, increasing error.
It's a trade-off.

### "Why do these outliers exist?"

Expand section

It's weird, isn't it? I got *fascinated* by these values a while back, and if you want to learn more about them
I recommend reading:

tl;dr: no one conclusively knows, but a small fraction of these outliers are *very* important to model quality.
Removing even a *single* "super weight," as Apple calls them, can cause the model to output complete gibberish.

Given their importance, real-world quantization schemes sometimes do extra work to preserve these outliers. They might
do this by not quantizing them at all, or by saving their location and value into a separate table, then removing them
so that their block isn't destroyed. During dequantization this table is consulted and the outliers are restored.

## How much does quantization affect model accuracy?

In this section I'm going to show you a number of ways quality loss in LLMs can
be measured. All of these measures have pros and cons. If you're evaluating
quantized models for a critcal use-case you have, nothing beats creating your
own benchmark for the specific task you're asking the model to perform.

Disclaimers aside, all of the following tests were performed against the
[Qwen3.5 9B](https://huggingface.co/Qwen/Qwen3.5-9B) model, and I've put details about all of the commands I
ran in the [appendix](#appendix) at the end of this post.

### Perplexity

What LLMs are doing under the hood is creating probability distributions of what
the likely next "token" is for a given prompt. For example, if I prompt Qwen3.5
9B with `The answer to 2 + 2 is`, it gives me these probabilities for what it
thinks the next token should be:

It's given a high probability for the token `4`, which makes sense given that's
the correct answer. Concerning that it'll say `5` 3% of the time, but I digress.

The idea behind "perplexity" as a measurement is to collapse these probability
distributions down into a single number that's easy to reason about. Calculating
perplexity involves a little bit of math but I promise it's not too bad. For the
single prediction above, `The answer to 2 + 2 is`, we take the probability of
the *correct* token, `4`, and we do this:

Copy code

```
1pCorrect = 0.9229; // 92.28%, probability for `4`2perplexity = Math.exp(-Math.log(pCorrect)); // 1.08
```

Lower scores are better, and the way you're supposed to read this is "the model
considers there to be ~1.08 plausible tokens that complete this prompt." The
lower the perplexity, the higher the probability the model gave to the correct
token.

When I give Qwen3.5 9B the prompt `And then I`, the possibilities are more spread
out.

If we assume the correct next token is `was`, the perplexity calculation for
this probability distribution becomes:

Copy code

```
1pCorrect = 0.03; // 3%, probability for `was`2perplexity = Math.exp(-Math.log(pCorrect)); // 33.33
```

Much higher, but then again: what would *you* have predicted comes after `And then I`? It's a far more ambiguous prompt, and it makes sense for models to be
less confident predicting it.

I used [`llama.cpp`](https://github.com/ggml-org/llama.cpp)'s `llama-perplexity` tool to measure the
perplexity of Qwen 3.5 9B at different quantization levels. The way it works is
you give it a reference text, and it takes a sliding window of tokens over that
reference text as the prompt, and uses the next token in the reference text to
know what the correct token should be.

To illustrate this sliding window idea, below you can see the prompt tokens and the correct token. Use the forward→︎ and backward←︎ buttons to move the sliding window.

### Sliding prompt window

Move prompt window backward←︎Move prompt window forward→︎

Interactive sliding prompt window. Full text: Help, I'm stuck in a test dataset used for measuring the perplexity of quantized models.. Use the backward and forward buttons to move the prompt window one token at a time.

Help, I'm stuck in a test dataset used for measuring the perplexity of quantized models.

Window: Help, I'm stuck in a test dataset. Correct token: used.

Correct token: used

At each step, the `-Math.log(pCorrect)` is accumulated and then at the end we
`Math.exp` the average. If we moved this sliding window across the whole
reference text and collected the correct token probabilities at each step into
`probs`, the end calculation would look like this:

Copy code

```
1let total = 0;2for (const prob of probs) {3	total += -Math.log(prob);4}5const perplexity = Math.exp(total / probs.length);
```

The `llama.cpp` project likes to use [wikitext-2](https://github.com/ggml-org/llama.cpp/blob/master/scripts/get-wikitext-2.sh)'s test dataset as
the reference text, so I did the same. It's just the contents of the Wikipedia
page on [Robert Boulter](https://en.wikipedia.org/wiki/Robert_Boulter), I have no idea why. I wonder if he
knows he's used to benchmark quantized LLM quality...

Anyway, let's take a look at the results.

We see almost no change with 8-bit symmetric, small degradation in the 4-bit
variants, and then almost complete collapse in the 2-bit variant. Quantization
has caused the model to become less confident, considering a wider selection of
tokens on average.

Crucially, perplexity only considered the *correct* token in its calculations.
The probability of all of the other tokens is not used. As such, perplexity
doesn't capture the full picture of how quantization has affected a model.

### KL divergence

Short for "Kullback-Leibler divergence," this is a measurement that tells us how
well 2 probability distributions overlap.

Play with the slider below. Try to get the KL divergence number to 0.

Two bell-shaped distributions with the same width are overlaid. The original distribution stays centered, and the quantized distribution is currently shifted 1.500 standard deviations to the right of the reference distribution.

KL divergence: 1.125

KL divergence 1.125. Quantized distribution moved right by 1.500 standard deviations.

The only time that KL divergence is 0 is when the 2 distributions exactly
overlap. The further they are apart, the higher the KL divergence.

It's not just horizontal skew that increases KL divergence, any sort of
non-overlapping will do it.

Two bell-shaped distributions are centered at the same position. The quantized distribution is currently shifted downward, making it shorter and wider than the original distribution.

KL divergence: 0.069

KL divergence 0.069. Quantized distribution moved down to 0.750 times the original height.

This measurement can be applied to the token probability distributions output by
an LLM. The distibution below shows the probability of each digit from 0 to 9 to
follow the prompt `The answer to 2 + 2 is`. Toggle between different levels of
quantization to see how it changes, along with the KL divergence score at the
top.

Line chart comparing next-token probabilities for digits 0 through 9. The original distribution is compared against a quantized distribution. KL divergence: 0.000. Per-token comparison: token 0, original 0.25 percent, 8-bit 0.25 percent; token 1, original 0.9 percent, 8-bit 0.91 percent; token 2, original 0.85 percent, 8-bit 0.87 percent; token 3, original 1.15 percent, 8-bit 1.19 percent; token 4, original 92.3 percent, 8-bit 92 percent; token 5, original 3.23 percent, 8-bit 3.43 percent; token 6, original 0.57 percent, 8-bit 0.57 percent; token 7, original 0.21 percent, 8-bit 0.22 percent; token 8, original 0.39 percent, 8-bit 0.4 percent; token 9, original 0.09 percent, 8-bit 0.09 percent.

KL divergence: 0.000

8-bit

4-bit (asym)

4-bit (sym)

2-bit

There's sadly no intuitive way to think about the KL divergence score other than
"higher is worse." There's not even a natural maximum, e.g. we can't say "KL
divergence is always between 0 and 1." It differs based on properties of the
model. For that reason, it's only valid to compare the score between
quantizations of the same model.

The `llama-perplexity` tool can also be used to measure KL divergence by passing
a `--kl-divergence` flag, details in the [appendix](#appendix). I used
[wikitext-2](https://github.com/ggml-org/llama.cpp/blob/master/scripts/get-wikitext-2.sh) as the reference text again.

While KL divergence has the downsides of being difficult to reason about
intuitively, and only comparable between quantizations of the same model, one of
the benefits it has over perplexity is that it considers the entire probability
distribution of each prediction.

Perplexity *only* cares about the probability of the correct token. The
probability of every other token could change, but if the correct one stayed the
same the perplexity wouldn't change. With KL divergence, if the entire
distribution changed, the score would be higher. KL divergence captures a fuller
picture of how quantization has changed the model's behavior.

### Benchmarking

I wrote a [whole post](https://ngrok.com/blog/ai-benchmarks) on LLM benchmarking, and one of the ways
people measure the impact of quantization is to compare a model's score on some
benchmarks before and after quantization.

For this post I decided to run the [GPQA Diamond](https://github.com/idavidrein/gpqa) benchmark. I [wrote
about this benchmark](https://ngrok.com/blog/ai-benchmarks#gpqa-diamond) if you're interested in learning the full
details, but for this post it's enough to know that it's a set of 198 very hard
multiple choice questions in biology, chemistry, and physics. Each question has
4 answers to choose from, so random guessing should score 25% on average.
Details on how I ran this benchmark are in the [appendix](#appendix).

If you're confused by the results, don't worry. So was I. The 8-bit quantization
scores *higher* than the unquantized model in its original `bfloat16` form. It's
hard to say exactly why this happens, it's possible that it is simply luck. With
multiple choice there's always that 25% chance of being right by accident.

What I'm taking away from these scores is that the 8- and 4-bit quantizations
perform well, but the 2-bit quantization has fallen off a cliff. No answer was
found for 97% of the questions, which could mean the model got stuck in a loop
or didn't understand what it was being asked to do.

### Just talk to it

The last test is the easiest but least rigorous: just talk to it! I asked the
same question to all of the different quantization levels to see how they would
respond. The question was: "What is the capital city of England, UK?"

All correct except for the 2-bit quantization, which refused to answer almost
every time I asked it. The "reasoning trace" got a little bit unhinged:

Copy code

```
1The capital city of England is London.2The capital city of England is London.3The capital city of England is London.4The capital city of England is London.5The capital city of England is London.6The capital city of England is London.7The capital city of England is London.8The capital city of England is London.9The capital city of London10The capital city of London11The capital city of London12The capital city of London13The capital city of London14The capital city of London15The capital city of London16The capital city of London
```

But then it would go on to produce an empty response. I think it's fair to say
that 2-bit quantization is too much information loss for Qwen3.5 9B, and it's
not a useful model at that level of compression.

Clearly this is not a thorough or scientific test, but it can be useful to help
you put all of the other scores into perspective.

## How much does quantization affect model speed?

The last thing I want to talk about is model speed. Smaller sizes of
quantization tend to also result in faster models. This is mostly due to there
being less data to move around inside your GPU.

The [`llama.cpp`](https://github.com/ggml-org/llama.cpp) project comes to the rescue again here with its
`llama-bench` tool, which I ran both on a MacBook Pro M1 Max and a rented H100
SXM GPU from [Runpod](https://www.runpod.io/). Performance figures are given in "tokens per second,"
so how fast the model generates responses.

There's a big difference in performance between the original `bfloat16` and the
8- and 4-bit quantizations. It's not obvious to me why the 2-bit is slower than
4-bit, though. I would have expected this to be faster. If you know why this is,
[please reach out and let me know](mailto:s.rose@ngrok.com)!

## Conclusion

The main thing I want you to take away from this post is that **quantized models
are pretty good, actually.**

When I first pitched the idea of writing this post, I didn't know anything about
how quantization worked. I had this assumption that model quality would degrade
linearly as you compress it. So if you start at `bfloat16`, an 8-bit
quantization of that would be half as good. Then a 4-bit quantization would be
half as good as the 8-bit version, and so on.

**That doesn't appear to be true.**

It looks like 16-bit to 8-bit carries almost no quality penalty. 16-bit to 4-bit
is more noticeable, but it's certainly not a quarter as good as the original.
Closer to 90%, depending on how you want to measure it.

So don't be afraid to run local models that are quantized. There's a quality
cliff at some point, but I've given you the tools to know how to identify where
it is. Provided you haven't fallen off that cliff, quantized models work well
and you shouldn't shy away from trying them just because they're compressed!

As you *do* experiment with quantized local models, consider giving ngrok's [AI
gateway](https://ngrok.ai) a shot. Use it to [route LLM requests to these local
models](https://ngrok.com/docs/ai-gateway/concepts/custom-providers), whether
they're running on your laptop or a rented GPU in the cloud.

## Further reading

This post has focused entirely on what's called "post-training quantization" or
PTQ. Some models these days go through what's called "quantization aware
training" or QAT, which introduces quantization during pre-training and helps
the model set its parameters that will quantize well.

I also only covered a couple of quantization methods, there's a lot of more
complex alternatives with different trade-offs. If you're interested, I
recommend looking up AWQ and GPTQ.

Quantization is also only one method of reducing the size of LLMs. There's also
parameter pruning and distillation. [Efficient Large Language Models: A
Survey](https://openreview.net/pdf?id=bsCCJHbO8A) is a litle old now (May 2024) but it gives a good overview of the
methods being pursued to make LLMs more efficient.

## Appendix

### Installing llama.cpp

Copy code

```
brew install llama.cpp
```

### Downloading Qwen 3.5 9B

Copy code

```
1llama-server -hf unsloth/Qwen3.5-9B-GGUF:BF16 --port 8000
```

This downloads the `bfloat16` version of Qwen 3.5 9B, then runs an OpenAI
compatible server on port 8000 backed by the model.

### Running the GPQA benchmark

You can clone the official [GPQA](https://github.com/idavidrein/gpqa) repository and unzip the question set like this:

Copy code

```
1git clone git@github.com:idavidrein/gpqa.git2cd gpqa3uv venv --python 3.94uv pip install -r requirements.txt5unzip -P deserted-untie-orchid dataset.zip
```

But I found that it doesn't let you run the benchmark against an arbitrary local
model. I [made some modifications](https://github.com/samwho/gpqa/commit/5100232b529fe4cede08d9970232fb7a6e93c42b) (sorry they're a bit noisy, my
editor changed a bunch of quotes and stuff) to allow me to run:

Copy code

```
1OPENAI_BASE_URL=http://localhost:8000/v1 uv run python baselines/run_baseline.py main \2        --model_name qwen3.5-9b-bf16 \3        --data_filename dataset/gpqa_diamond.csv \4        --prompt_type zero_shot \5        --max-tokens 30000 \6        --verbose
```

I ended up running the benchmark against a `llama-server` that allowed for 4096 reasoning tokens:

Copy code

```
llama-server -hf unsloth/Qwen3.5-9B-GGUF:BF16 --reasoning-budget 4096
```

### Quantizing the model

Copy code

```
1cd ~/Library/Caches/llama.cpp2llama-quantize unsloth_Qwen3.5-9B-GGUF_Qwen3.5-9B-BF16.gguf unsloth_Qwen3.5-9B-GGUF_Qwen3.5-9B-Q8_0.gguf Q8_0
```

There's a lot going on there, I'll break it down:

* `~/Library/Caches/llama.cpp`: This is the directory where `llama.cpp` stores models it's downloaded.
* `unsloth_Qwen3.5-9B-GGUF_Qwen3.5-9B-BF16.gguf`: This is the filename that was given to the model we downloaded when we ran `llama-server -hf unsloth/Qwen3.5-9B-GGUF:BF16` earlier.
* `unsloth_Qwen3.5-9B-GGUF_Qwen3.5-9B-Q8_0.gguf`: This is the filename I want to give to my newly quantized model.
* `Q8_0`: This is the quantization format, `llama.cpp` has a special format for these strings, the "Q8" here means quantize to 8-bit, and the "\_0" means symmetric quantization.

That command only took a minute on my laptop, and the resulting file is just over half the size of the original.

Here are the format strings to use for each of the quantization levels I used throughout the post:

`llama.cpp` doesn't seem to offer a 8-bit asymmetric or 2-bit symmetric option
as far as I can tell.

Also, I know that the 2-bit quantization I'm using is different to the rest. I
watched the fantastic [reverse-engineering
GGUF](https://www.youtube.com/watch?v=vW30o4U9BFE) video from Julia Turc, but it
was between K-quant or I-quant, there's no legacy quant available for 2-bit. So
I compromised. I also suspect this has something to do with why my `llama-bench`
results for 2-bit were weird.

### Measuring perplexity and KL divergence

I used the [get-wikitext-2.sh](https://github.com/ggml-org/llama.cpp/blob/master/scripts/get-wikitext-2.sh) script from the llama.cpp repo to download the wikitext-2 test dataset then ran:

Copy code

```
llama-perplexity -hf unsloth/Qwen3.5-9B-GGUF:BF16 -f wikitext-2-raw/wiki.test.raw -c 512 --kl-divergence-base ~/reference.kld
```

This saves KL divergence data you'll need when measuring the quantized versions of the model. Use it like this:

Copy code

```
llama-perplexity -m path/to/quantized/model.gguf -f wikitext-2-raw/wiki.test.raw -c 512 --kl-divergence-base ~/reference.kld --kl-divergence
```

### Talking to models locally

Copy code

```
llama-cli -hf unsloth/Qwen3.5-9B-GGUF:BF16
```

### Measuring performance

Copy code

```
llama-bench -hf unsloth/Qwen3.5-9B-GGUF:BF16
```
