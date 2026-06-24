import os
import requests
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def ask_llm(question, context):

    prompt = f"""
You are an Industrial Knowledge Assistant specializing in:

- Industrial maintenance
- Equipment failures
- Safety procedures
- Compliance reports
- Inspection records

IMPORTANT RULES:
1. Use ONLY the information present in the provided context.
2. If the answer exists in the context, answer clearly and concisely.
3. If multiple pieces of information are relevant, combine them.
4. If the answer does not exist in the context, respond EXACTLY with:
"The answer is not available in the uploaded documents."
5. Never use outside knowledge or assumptions.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "qwen/qwen-2.5-7b-instruct",
            "messages": [
                {
                    "role": "system",
                    "content": "You are an industrial AI assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.1,
            "max_tokens": 300
        }
    )

    # Handle API errors gracefully
    if response.status_code != 200:
        return f"OpenRouter Error: {response.text}"

    result = response.json()

    return result["choices"][0]["message"]["content"]