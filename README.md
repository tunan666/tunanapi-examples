# ð TunanAPI

**Access China's Best AI Models â One API, PayPal Billing, Zero Hassle**

**Get your API key in 30 seconds â [tunanapi.com](https://tunanapi.com/)**

â­ **If you find this useful, star the repo! It helps others discover it.**

---

OpenAI-compatible API for China's best AI models â one endpoint, 8 models, PayPal billing.

**Base URL:** `https://api.tunanapi.com/v1`
**Get API Key:** [tunanapi.com](https://tunanapi.com)
**Docs:** [tunanapi.com/docs.html](https://tunanapi.com/docs.html)

---

## Quick Start

Replace your OpenAI base URL with ours â that's it.

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.tunanapi.com/v1",
    api_key="your-key-here"
)

response = client.chat.completions.create(
    model="qwen3.7-max",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

## Available Models

> *Pricing updated August 2026. DeepSeek V4 Pro permanently reduced 75%.*

| Model | Provider | Input/1M | Output/1M | Best For |
|-------|----------|----------|-----------|----------|
| glm-4-flash | GLM | $0.05 | $0.05 | Free-tier tasks |
| qwen3.5-flash | Qwen | $0.35 | $1.39 | Ultra-cheap production |
| deepseek-v4-flash | DeepSeek | $0.70 | $1.40 | Fast, affordable tasks |
| minimax-m3 | MiniMax | $1.20 | $4.80 | Coding & reasoning |
| glm-4-plus | GLM | $1.39 | $1.39 | Chinese + English |
| qwen3.7-plus | Qwen | $1.39 | $5.56 | Balanced performance |
| qwen3.7-max | Qwen | $2.08 | $6.25 | 1M context, agents |
| deepseek-v4-pro | DeepSeek | $2.18 | $4.35 | Complex reasoning |

**DeepSeek V4 Flash** is the #1 model globally on OpenRouter (7.22T tokens/week, Aug 2026).
**vs Anthropic Fable 5 ($10/$50):** Qwen3.7-Max is **8x cheaper** for flagship-tier performance.

## Framework Integration

### LangChain

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://api.tunanapi.com/v1",
    model="deepseek-v4-flash",
    api_key="your-key-here"
)
```

### Vercel AI SDK

```tsx
import { createOpenAI } from '@ai-sdk/openai';
import { streamText } from 'ai';

const tunan = createOpenAI({
  baseURL: 'https://api.tunanapi.com/v1',
  apiKey: process.env.TUNAN_API_KEY,
});

const result = streamText({
  model: tunan('qwen3.7-max'),
  prompt: 'Explain Next.js App Router in 3 sentences.',
});
```

### cURL

```bash
curl https://api.tunanapi.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-key-here" \
  -d '{
    "model": "deepseek-v4-flash",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## Examples

- [python/](python/) â Python examples (basic, streaming, LangChain)
- [nodejs/](nodejs/) â Node.js examples
- [curl/](curl/) â Raw HTTP examples

## ð Case Studies

### I Ching Oracle â AI Fortune Teller
Ancient Chinese divination meets modern AI. Built with Qwen 3.7-Max's 1M context window.

- **Tech stack:** FastAPI + Vanilla JS + PayPal
- **Model:** Qwen 3.7-Max (full I Ching text in system prompt)
- **Cost per reading:** ~$0.03
- **Live:** [oracle.tunanapi.com](https://oracle.tunanapi.com)

```python
# 1M context = entire I Ching + commentary in one prompt
llm = ChatOpenAI(
    base_url="https://api.tunanapi.com/v1",
    model="qwen3.7-max",
    temperature=0.8,
)
```

*More case studies coming soon â building something with TunanAPI? Let us know!*

## ð ï¸ Tools & Calculators

### ð° Token Cost Calculator
Compare pricing across 8 Chinese AI models vs OpenAI, Anthropic, Google.
Free, no signup needed.

ð **[Try the calculator](https://tunanapi.com/pricing-calculator.html)**

Example savings for 10M tokens/month (5M in + 5M out):

| Provider | Monthly Cost | Savings vs Claude |
|----------|-------------|-------------------|
| Claude Fable 5 | $540 | â |
| GPT-4o | $100 | 81% |
| **TunanAPI (DeepSeek V4 Pro)** | **$32.65** | **94%** |

## Why TunanAPI?

- ð **No China phone/ID required** â sign up with any email
- ð³ **PayPal payments** â no Chinese payment methods needed
- ð **OpenAI-compatible** â drop-in replacement, zero code changes
- â¡ **8 models** â DeepSeek, Qwen, GLM, MiniMax in one API
- ð **Free tier** â GLM-4-Flash at $0.05/M tokens
- ð **Privacy first** â Hong Kong hosted, no data stored, no prompts logged

## Support

- ð° **[Cost Calculator](https://tunanapi.com/pricing-calculator.html)** â Free tool to compare AI pricing
- ð® **[I Ching Oracle](https://oracle.tunanapi.com)** â Built with TunanAPI
- ð§ Email: tunanapi@outlook.com
- ð Docs: [tunanapi.com/docs.html](https://tunanapi.com/docs.html)
- ð¬ **Discord:** Coming soon
- ð¦ **Twitter/X:** Coming soon
