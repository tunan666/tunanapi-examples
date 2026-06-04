#!/bin/bash
# TunanAPI curl examples
# Replace sk-YOUR_API_KEY with your actual key

API_KEY="sk-YOUR_API_KEY"
BASE="https://api.tunanapi.com/v1"

echo "=== Basic Chat ==="
curl -s "$BASE/chat/completions" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek-chat","messages":[{"role":"user","content":"Say hello"}]}' | jq .

echo -e "\n=== Streaming ==="
curl -s "$BASE/chat/completions" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek-chat","messages":[{"role":"user","content":"Count to 5"}],"stream":true}'

echo -e "\n\n=== List Models ==="
curl -s "$BASE/models" \
  -H "Authorization: Bearer $API_KEY" | jq .

echo -e "\n=== Check Balance ==="
curl -s "https://api.tunanapi.com/api/user/self" \
  -H "Authorization: Bearer $API_KEY" | jq .
