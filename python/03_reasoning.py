"""Deep reasoning with DeepSeek Reasoner"""
from openai import OpenAI

client = OpenAI(
    api_key="sk-YOUR_API_KEY",
    base_url="https://api.tunanapi.com/v1"
)

response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role": "user", "content": "Prove that there are infinitely many prime numbers."}]
)

print("=== Reasoning ===")
print(response.choices[0].message.reasoning_content)
print("\n=== Answer ===")
print(response.choices[0].message.content)
