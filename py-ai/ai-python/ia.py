import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "¿Cuál es la capital de Perú?"}],
)

# print(type(response))

print(f"Respuesta del modelo: {response.choices[0].message.content}")
