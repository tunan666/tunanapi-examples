<div align="center">

# 🚀 TunanAPI

**Access China's Best AI Models — One API, PayPal Billing, Zero Hassle**

[![API Status](https://img.shields.io/website?url=https%3A%2F%2Fapi.tunanapi.com&label=API%20Status)](https://api.tunanapi.com)
[![Docs](https://img.shields.io/badge/docs-online-blue)](https://tunanapi.com/docs.html)
[![OpenAI Compatible](https://img.shields.io/badge/OpenAI-Compatible-green)](https://platform.openai.com/docs/api-reference)
[![PayPal](https://img.shields.io/badge/payment-PayPal-blue)](https://tunanapi.com)

**Get your API key in 30 seconds → [tunanapi.com](https://tunanapi.com)**

</div>

---

## Why TunanAPI?

If you're outside China, accessing models like Qwen, DeepSeek, GLM, and MiniMax is painful — you need a Chinese phone number, Alipay/WeChat Pay, and sometimes real-name verification. **TunanAPI removes all of that.**

| Problem | Without TunanAPI | With TunanAPI |
|---------|------------------|---------------|
| Sign up | Chinese phone + ID verification | Any email, 30 seconds |
| Payment | Alipay / WeChat Pay only | PayPal |
| API format | Different per provider | OpenAI-compatible, one endpoint |
| Model access | Register at each provider separately | 8 models, single API key |

---

## Pricing — Up to 8x Cheaper Than GPT-4o

| Model | Provider | Input/1M | Output/1M | Context | Best For |
|-------|----------|----------|-----------|---------|----------|
| **glm-4-flash** | GLM | $0.05 | $0.05 | 128K | ⚡ Free-tier, prototyping |
| **qwen3.5-flash** | Qwen | $0.35 | $1.39 | 1M | 💰 Ultra-cheap production |
| **deepseek-chat** | DeepSeek | $0.70 | $1.40 | 128K | 🤖 Fast, affordable tasks |
| **minimax-m3** | MiniMax | $1.20 | $4.80 | 1M | 🧠 Coding & reasoning |
| **glm-4-plus** | GLM | $1.39 | $1.39 | 128K | 🌐 Chinese + English |
| **qwen3.7-plus** | Qwen | $1.39 | $5.56 | 1M | ⚖️ Balanced performance |
| **qwen3.7-max** | Qwen | $2.08 | $6.25 | 1M | 🏆 Flagship, agents, RAG |
| **deepseek-reasoner** | DeepSeek | $2.18 | $4.35 | 128K | 🔬 Complex reasoning |

### Cost Comparison

| Task (1M input + 1M output) | GPT-4o | Claude Fable 5 | TunanAPI (Qwen3.7-Max) |
|------------------------------|--------|----------------|-------------------------|
| **Cost** | $5.00 | $60.00 | **$8.33** |
| **Savings** | — | — | **40% vs GPT-4o, 86% vs Claude** |

> 💡 **DeepSeek-Chat at $2.10/M tokens total** — cheaper than GPT-4o-mini with better quality.

---

## Quick Start — 3 Lines of Code

Replace your OpenAI base URL. That's it.

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
```

**Get your API key:** [tunanapi.com](https://tunanapi.com) — no credit card required to start.

---

## Framework Integration

### LangChain
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://api.tunanapi.com/v1",
    api_key="your-key",
    model="deepseek-chat"
)
```

### Vercel AI SDK
```typescript
import { createOpenAI } from '@ai-sdk/openai';

const tunan = createOpenAI({
  baseURL: 'https://api.tunanapi.com/v1',
  apiKey: 'your-key',
});
```

### cURL
```bash
curl https://api.tunanapi.com/v1/chat/completions \
  -H "Authorization: Bearer sk-YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek-chat","messages":[{"role":"user","content":"Hello!"}]}'
```

### OpenAI CLI
```bash
export OPENAI_API_KEY="sk-YOUR_API_KEY"
export OPENAI_API_BASE="https://api.tunanapi.com/v1"

openai api chat_completions.create -m deepseek-chat -g user "Hello"
```

---

## Examples

| Directory | Language | What's Included |
|-----------|----------|-----------------|
| [`python/`](python/) | Python | Basic chat, streaming, LangChain, async |
| [`nodejs/`](nodejs/) | Node.js | Express server, streaming, AI SDK |
| [`curl/`](curl/) | Bash | Raw HTTP examples for quick testing |

---

## Free Tier

Every new account gets **500,000 tokens free** on GLM-4-Flash ($0.05/M tokens). Enough to:
- Process ~2,500 short prompts
- Build and test your prototype
- Evaluate output quality before paying

No credit card required. No expiration.

---

## Supported Models Detail

### 🔥 DeepSeek
- **deepseek-chat** — Fast, affordable general-purpose model. Great for chatbots, content generation, and code assistance.
- **deepseek-reasoner** — Chain-of-thought reasoning for math, logic, and complex analysis.

### 🏆 Qwen (Alibaba)
- **qwen3.5-flash** — Ultra-cheap with 1M context window. Best for high-volume tasks.
- **qwen3.7-plus** — Balanced performance/cost. Strong multilingual support.
- **qwen3.7-max** — Flagship model. 1M context, best for agents, RAG, and complex workflows.

### 🌐 GLM (Zhipu AI)
- **glm-4-flash** — The cheapest model we offer. Perfect for prototyping and free-tier usage.
- **glm-4-plus** — Strong bilingual (Chinese/English) performance at mid-range pricing.

### 🧠 MiniMax
- **minimax-m3** — Competitive reasoning and coding capabilities with 1M context.

---

## FAQ

**Q: Do I need a Chinese phone number?**  
A: No. Sign up with any email address.

**Q: Do I need Alipay or WeChat Pay?**  
A: No. We accept PayPal.

**Q: Is it really OpenAI-compatible?**  
A: Yes. Same API format, same SDKs. Just change the base URL and API key.

**Q: Are the models censored?**  
A: Models follow their respective provider's safety guidelines. We do not add additional filtering.

**Q: What's the uptime?**  
A: We run on a dedicated Hong Kong VPS with upstream direct connections to each provider. 99.9% target uptime.

---

## Links

- 🌐 **Website:** [tunanapi.com](https://tunanapi.com)
- 📖 **Docs:** [tunanapi.com/docs.html](https://tunanapi.com/docs.html)
- 📧 **Email:** tunanapi@outlook.com
- 💬 **Discord:** Coming soon
- 🐦 **Twitter:** Coming soon

---

<div align="center">

**Made with ❤️ for developers who want access to China's best AI models without the hassle.**

[Get Started Free →](https://tunanapi.com)

</div>
