---
title: Flex processing | OpenAI API
type: source
source_type: article
url: https://platform.openai.com/docs/guides/flex-processing
fetched: 2026-10-19
---

# Flex processing | OpenAI API

Flex processing provides lower costs for [Responses](/api/docs/api-reference/responses) or [Chat Completions](/api/docs/api-reference/chat) requests in exchange for slower response times and occasional resource unavailability. It’s ideal for non-production or lower priority tasks, such as model evaluations, data enrichment, and asynchronous workloads.

Tokens are [priced](/api/docs/pricing) at [Batch API rates](/api/docs/guides/batch), with additional discounts from [prompt caching](/api/docs/guides/prompt-caching).

Flex processing is in beta with limited model availability. Supported models
are listed on the [pricing page](/api/docs/pricing?latest-pricing=flex).

To use Flex processing, set the `service_tier` parameter to `flex` in your API request:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16import OpenAI from "openai";
const client = new OpenAI({
  timeout: 15 * 1000 * 60, // Increase default timeout to 15 minutes
});

const response = await client.responses.create(
  {
    model: "gpt-6-astra",
    instructions: "List and describe all the metaphors used in this book.",
    input: "<very long text of book here>",
    service_tier: "flex",
  },
  { timeout: 15 * 1000 * 60 }
);

console.log(response.output_text);
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16from openai import OpenAI

client = OpenAI(
    # increase default timeout to 15 minutes (from 10 minutes)
    timeout=900.0
)

# you can override the max timeout per request as well
response = client.with_options(timeout=900.0).responses.create(
    model="gpt-6-astra",
    instructions="List and describe all the metaphors used in this book.",
    input="<very long text of book here>",
    service_tier="flex",
)

print(response.output_text)
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25package main

import (
	"context"
	"fmt"
	"time"

	"github.com/openai/openai-go/v3"
	"github.com/openai/openai-go/v3/option"
	"github.com/openai/openai-go/v3/responses"
)

func main() {
	client := openai.NewClient(option.WithRequestTimeout(15 * time.Minute))
	response, err := client.Responses.New(context.Background(), responses.ResponseNewParams{
		Model:        "gpt-6-astra",
		Instructions: openai.String("List and describe all the metaphors used in this book."),
		Input:        responses.ResponseNewParamsInputUnion{OfString: openai.String("<very long text of book here>")},
		ServiceTier:  responses.ResponseNewParamsServiceTierFlex,
	})
	if err != nil {
		panic(err)
	}
	fmt.Println(response.OutputText())
}
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.responses.ResponseCreateParams;
import java.time.Duration;

client = client.withOptions(options -> options.timeout(Duration.ofMinutes(15)));

ResponseCreateParams params =
    ResponseCreateParams.builder()
        .model("gpt-6-astra")
        .input("<very long text of book here>")
        .instructions("List and describe all the metaphors used in this book.")
        .serviceTier(ResponseCreateParams.ServiceTier.FLEX)
        .build();

client.responses().create(params).output().stream()
    .flatMap(item -> item.message().stream())
    .flatMap(message -> message.content().stream())
    .flatMap(content -> content.outputText().stream())
    .forEach(text -> System.out.println(text.text()));
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19using System.ClientModel;
using OpenAI.Responses;
#pragma warning disable OPENAI001

string key = Environment.GetEnvironmentVariable("OPENAI_API_KEY")!;
ResponsesClientOptions clientOptions = new() { NetworkTimeout = TimeSpan.FromMinutes(15) };
ResponsesClient client = new(new ApiKeyCredential(key), clientOptions);

CreateResponseOptions options = new()
{
    Model = "gpt-6-astra",
    Instructions = "List and describe all the metaphors used in this book.",
    ServiceTier = ResponseServiceTier.Flex,
};
options.InputItems.Add(ResponseItem.CreateUserMessageItem("<very long text of book here>"));

using CancellationTokenSource timeout = new(TimeSpan.FromMinutes(15));
ResponseResult response = await client.CreateResponseAsync(options, timeout.Token);
Console.WriteLine(response.GetOutputText());
```

```
1
2
3
4
5
6
7
8
9
10
11
12require "openai"

client = OpenAI::Client.new(timeout: 900.0)

response = client.responses.create(
  model: "gpt-6-astra",
  service_tier: :flex,
  instructions: "List and describe all the metaphors used in this book.",
  input: "<very long text of book here>"
)

puts(response.output_text)
```

```
1
2
3
4
5
6
7
8
9curl https://api.openai.com/v1/responses \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-6-astra",
    "instructions": "List and describe all the metaphors used in this book.",
    "input": "<very long text of book here>",
    "service_tier": "flex"
  }'
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21import OpenAI from "openai";
const client = new OpenAI({
  timeout: 15 * 1000 * 60,
});

const response = await client.chat.completions.create(
  {
    model: "gpt-6-astra",
    messages: [
      {
        role: "developer",
        content: "List and describe all the metaphors used in this book.",
      },
      { role: "user", content: "<very long text of book here>" },
    ],
    service_tier: "flex",
  },
  { timeout: 15 * 1000 * 60 }
);

console.log(response.choices[0].message.content);
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18from openai import OpenAI

client = OpenAI(timeout=900.0)

response = client.chat.completions.create(
    model="gpt-6-astra",
    messages=[
        {
            "role": "developer",
            "content": "List and describe all the metaphors used in this book.",
        },
        {"role": "user", "content": "<very long text of book here>"},
    ],
    service_tier="flex",
    timeout=900.0,
)

print(response.choices[0].message.content)
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26package main

import (
	"context"
	"fmt"
	"time"

	"github.com/openai/openai-go/v3"
	"github.com/openai/openai-go/v3/option"
)

func main() {
	client := openai.NewClient(option.WithRequestTimeout(15 * time.Minute))
	completion, err := client.Chat.Completions.New(context.Background(), openai.ChatCompletionNewParams{
		Model:       "gpt-6-astra",
		ServiceTier: openai.ChatCompletionNewParamsServiceTierFlex,
		Messages: []openai.ChatCompletionMessageParamUnion{
			openai.DeveloperMessage("List and describe all the metaphors used in this book."),
			openai.UserMessage("<very long text of book here>"),
		},
	})
	if err != nil {
		panic(err)
	}
	fmt.Println(completion.Choices[0].Message.Content)
}
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.chat.completions.ChatCompletionCreateParams;
import java.time.Duration;

client = client.withOptions(options -> options.timeout(Duration.ofMinutes(15)));

ChatCompletionCreateParams params =
    ChatCompletionCreateParams.builder()
        .model("gpt-6-astra")
        .addDeveloperMessage("List and describe all the metaphors used in this book.")
        .addUserMessage("<very long text of book here>")
        .serviceTier(ChatCompletionCreateParams.ServiceTier.FLEX)
        .build();

client.chat().completions().create(params).choices().stream()
    .flatMap(choice -> choice.message().content().stream())
    .forEach(System.out::println);
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22using System.ClientModel;
using OpenAI;
using OpenAI.Chat;
#pragma warning disable OPENAI001

string key = Environment.GetEnvironmentVariable("OPENAI_API_KEY")!;
string model = "gpt-6-astra";
OpenAIClientOptions clientOptions = new() { NetworkTimeout = TimeSpan.FromMinutes(15) };
ChatClient client = new(model, new ApiKeyCredential(key), clientOptions);

ChatCompletionOptions options = new() { ServiceTier = ChatServiceTier.Flex };
using CancellationTokenSource timeout = new(TimeSpan.FromMinutes(15));
ChatCompletion completion = await client.CompleteChatAsync(
    [
        new DeveloperChatMessage("List and describe all the metaphors used in this book."),
        new UserChatMessage("<very long text of book here>"),
    ],
    options,
    timeout.Token
);

Console.WriteLine(completion.Content[0].Text);
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20require "openai"

client = OpenAI::Client.new(timeout: 900.0)

completion = client.chat.completions.create(
  model: "gpt-6-astra",
  service_tier: :flex,
  messages: [
    {
      role: :developer,
      content: "List and describe all the metaphors used in this book."
    },
    {
      role: :user,
      content: "<very long text of book here>"
    }
  ]
)

puts(completion.choices.fetch(0).message.content)
```

```
1
2
3
4
5
6
7
8curl https://api.openai.com/v1/chat/completions   -H "Content-Type: application/json"   -H "Authorization: Bearer $OPENAI_API_KEY"   -d '{
    "model": "gpt-6-astra",
    "messages": [
      {"role": "developer", "content": "List and describe all the metaphors used in this book."},
      {"role": "user", "content": "<very long text of book here>"}
    ],
    "service_tier": "flex"
  }' --max-time 900
```

Due to slower processing speeds with Flex processing, request timeouts are more likely. Here are some considerations for handling timeouts:

* **Default timeout**: The default timeout is **10 minutes** when making API requests with an official OpenAI SDK. You may need to increase this timeout for lengthy prompts or complex tasks.
* **Configuring timeouts**: Each SDK will provide a parameter to increase this timeout. In the Python and JavaScript SDKs, this is `timeout` as shown in the code samples above.
* **Automatic retries**: The OpenAI SDKs automatically retry requests that result in a `408 Request Timeout` error code twice before throwing an exception.

Flex processing may sometimes lack sufficient resources to handle your requests, resulting in a `429 Resource Unavailable` error code. **You will not be charged when this occurs.**

Consider implementing these strategies for handling resource unavailable errors:

* **Retry requests with exponential backoff**: Implementing exponential backoff is suitable for workloads that can tolerate delays and aims to minimize costs, as your request can eventually complete when more capacity is available. For implementation details, see [this cookbook](/cookbook/examples/how_to_handle_rate_limits?utm_source=chatgpt.com#retrying-with-exponential-backoff).
* **Retry requests with standard processing**: When receiving a resource unavailable error, implement a retry strategy with standard processing if occasional higher costs are worth ensuring successful completion for your use case. To do so, set `service_tier` to `auto` in the retried request, or remove the `service_tier` parameter to use the default mode for the project.
