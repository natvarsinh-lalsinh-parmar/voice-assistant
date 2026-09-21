import os
from dotenv import load_dotenv
from openai import OpenAI
import requests

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# openAI API related code
# def ask_ai(prompt):
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are Nakshi, a helpful AI voice assistant."},
#             {"role": "user", "content": prompt}
#         ]
#     )

#     return response.choices[0].message.content

# Ollama model related code (installed in local system)
OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_ai(prompt):

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3",
                # "model": "qwen2.5:1.5b",
                # "model": "phi3:mini",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()
        return data["response"]

    except Exception as e:
        print("Ollama error:", e)
        return "AI is not available right now."