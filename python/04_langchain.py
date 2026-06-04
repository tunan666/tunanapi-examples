"""Using TunanAPI with LangChain"""
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOpenAI(
    model="deepseek-chat",
    api_key="sk-YOUR_API_KEY",
    base_url="https://api.tunanapi.com/v1"
)

messages = [
    SystemMessage(content="You are a senior software engineer."),
    HumanMessage(content="Review this code: def add(a, b): return a + b")
]

response = llm.invoke(messages)
print(response.content)
