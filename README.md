# TunanAPI Examples

OpenAI-compatible API for China's best AI models — one endpoint, 10+ models.

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
```

## Available Models

| Model | Provider | Input/1M | Output/1M | Best For |
|-------|----------|----------|-----------|----------|
| deepseek-chat | DeepSeek | $0.20 | $0.40 | General purpose |
| deepseek-reasoner | DeepSeek | $2.50 | $5.00 | Complex reasoning |
| qwen3.7-max | Qwen | $1.80 | $5.40 | Advanced tasks |
| qwen3.7-plus | Qwen | $0.58 | $1.74 | Balanced |
| qwen3.5-flash | Qwen | $0.07 | $0.22 | Fast & cheap |
| glm-4-plus | GLM | $1.80 | $5.40 | Advanced tasks |
| glm-4-flash | GLM | $0.07 | $0.22 | Fast & cheap |
| minimax-m2.5 | MiniMax | $0.22 | $1.65 | General + long ctx |
| minimax-m2.7 | MiniMax | $0.29 | $1.73 | Improved reasoning |
| minimax-m3 | MiniMax | $0.43 | $3.31 | 1M context window |

## Examples

- [`python/`](python/) — Python examples (basic, streaming, LangChain)
- [`nodejs/`](nodejs/) — Node.js examples
- [`curl/`](curl/) — Raw HTTP examples

## Why TunanAPI?

- 🌍 **No China phone/ID required** — sign up with any email
- 💳 **PayPal payments** — no Chinese payment methods needed  
- 🔑 **OpenAI-compatible** — drop-in replacement, zero code changes
- ⚡ **10+ models** — DeepSeek, Qwen, GLM, MiniMax in one API
- 🆓 **$0.50 free** — start building immediately

## Support

- Email: tunanapi@outlook.com
- Docs: https://tunanapi.com/docs.html
