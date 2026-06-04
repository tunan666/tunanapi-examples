// Streaming chat completion with TunanAPI
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'sk-YOUR_API_KEY',
  baseURL: 'https://api.tunanapi.com/v1'
});

const stream = await client.chat.completions.create({
  model: 'deepseek-chat',
  messages: [{ role: 'user', content: 'Write a haiku about coding.' }],
  stream: true
});

for await (const chunk of stream) {
  const content = chunk.choices[0]?.delta?.content || '';
  process.stdout.write(content);
}
console.log();
