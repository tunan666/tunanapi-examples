"""Compare responses across multiple models"""
from openai import OpenAI

client = OpenAI(
    api_key="sk-YOUR_API_KEY",
    base_url="https://api.tunanapi.com/v1"
)

models = ["deepseek-chat", "qwen3.5-flash", "glm-4-flash"]
prompt = "What is the capital of France? Answer in one word."

for model in models:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50
    )
    answer = response.choices[0].message.content.strip()
    tokens = response.usage.total_tokens
    print(f"{model:20s} → {answer} ({tokens} tokens)")
