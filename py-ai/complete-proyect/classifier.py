import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
                You are a senior sales analyst. 
                You receive a message from a lead and must classify it. 
                Respond ONLY with a valid JSON, no explanations, no code blocks. 
                Exact format: 
                { 
                  "interest": "high|medium|low", 
                  "urgency": "immediate|this_month|exploring", 
                  "estimated_budget": "high|medium|low|unknown", 
                  "profile": "enterprise|startup|individual|unknown", 
                  "next_action": "specific personalized business action" 
                }
                """


def classify_lead(name, message):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Lead: {name}\nMensaje: {message}"},
            ],
            temperature=0.1,
        )

        text = response.choices[0].message.content.strip()
        return json.loads(text)

    except json.JSONDecodeError:
        return {"error": "Invalid JSON response from model", "raw_response": text}

    except Exception as e:
        return {"error": str(e)}
