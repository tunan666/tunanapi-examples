"""Streaming chat completion with TunanAPI"""
from openai import OpenAI

client = OpenAI(
    api_key="sk-YOUR_API_KEY",
    base_url="https://api.tunanapi.com/v1"
)

stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Write a short poem about AI."}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)

print()  # newline
