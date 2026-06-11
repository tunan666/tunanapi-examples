# TunanAPI Examples

OpenAI-compatible API for China's best AI models — one endpoint, 8 models, PayPal billing.

**Base URL:** `https://api.tunanapi.com/v1`  
**Get API Key:** [tunanapi.com](https://tunanapi.com)  
**Docs:** [tunanapi.com/docs.html](https://tunanapi.com/docs.html)

## Quick Start

Replace your OpenAI base URL with ours — that's it.

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-YOUR_API_KEY",
    base_url="https://api.tunanapi.com/v1"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

## Available Models

| Model | Provider | Input/1M | Output/1M | Best For |
|-------|----------|----------|-----------|----------|
| glm-4-flash | GLM | $0.05 | $0.05 | Free-tier tasks |
| qwen3.5-flash | Qwen | $0.35 | $1.39 | Ultra-cheap production |
| deepseek-chat | DeepSeek | $0.70 | $1.40 | Fast, affordable tasks |
| minimax-m3 | MiniMax | $1.20 | $4.80 | Coding and reasoning |
| glm-4-plus | GLM | $1.39 | $1.39 | Chinese + English |
| qwen3.7-plus | Qwen | $1.39 | $5.56 | Balanced performance |
| qwen3.7-max | Qwen | $2.08 | $6.25 | 1M context, agents |
| deepseek-reasoner | DeepSeek | $2.18 | $4.35 | Complex reasoning |

**vs Anthropic Fable 5 ($10/$50):** Qwen3.7-Max is **8x cheaper** for flagship-tier performance.

## Framework Integration

**LangChain:**
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://api.tunanapi.com/v1",
    api_key="your-key",
    model="deepseek-chat"
)
```

**Vercel AI SDK:**
```typescript
import { createOpenAI } from '@ai-sdk/openai';

const tunan = createOpenAI({
  baseURL: 'https://api.tunanapi.com/v1',
  apiKey: 'your-key',
});
```

**cURL:**
```bash
curl https://api.tunanapi.com/v1/chat/completions   -H "Authorization: Bearer sk-YOUR_API_KEY"   -H "Content-Type: application/json"   -d '{"model":"deepseek-chat","messages":[{"role":"user","content":"Hello!"}]}'
```

## Examples

- [`python/`](python/) — Python examples (basic, streaming, LangChain)
- [`nodejs/`](nodejs/) — Node.js examples
- [`curl/`](curl/) — Raw HTTP examples

## Why TunanAPI?

- No China phone/ID required — sign up with any email
- PayPal payments — no Chinese payment methods needed  
- OpenAI-compatible — drop-in replacement, zero code changes
- 8 models — DeepSeek, Qwen, GLM, MiniMax in one API
- Free tier — GLM-4-Flash at $0.05/M tokens

## Support

- Email: tunanapi@outlook.com
- Docs: https://tunanapi.com/docs.html
