from ollama import Client
from config import MODEL_NAME, OLLAMA_API_KEY

client = Client(
    host="https://ollama.com",
    headers={"Authorization": f"Bearer {OLLAMA_API_KEY}"}
)

def ask_llm(prompt: str) -> str:
    response = client.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']
