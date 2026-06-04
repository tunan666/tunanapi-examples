// Basic chat completion with TunanAPI
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'sk-YOUR_API_KEY',
  baseURL: 'https://api.tunanapi.com/v1'
});

const response = await client.chat.completions.create({
  model: 'deepseek-chat',
  messages: [{ role: 'user', content: 'Hello, who are you?' }]
});

console.log(response.choices[0].message.content);
console.log(`Tokens: ${response.usage.total_tokens}`);
