import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

OUTPUT_FILE = "leads_analizados.json"
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def clasificar_lead(nombre, mensaje):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """Eres un analista de ventas.
Analiza el mensaje de un lead y responde ÚNICAMENTE con un JSON válido, sin explicaciones.
Formato exacto:
{
  "interes": "alto|medio|bajo",
  "urgencia": "inmediata|este_mes|explorando",
  "presupuesto_estimado": "alto|medio|bajo|desconocido",
  "siguiente_accion": "texto corto con la acción recomendada"
}""",
            },
            {"role": "user", "content": f"Lead: {nombre}\nMensaje: {mensaje}"},
        ],
        temperature=0.1,
    )

    text = response.choices[0].message.content
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"error": "Respuesta no es JSON válido", "raw_response": text}


def save_leads(leads, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(leads, file, indent=2, ensure_ascii=False)


def main():
    leads_prueba = [
        {
            "nombre": "Carlos Méndez",
            "mensaje": "Necesito implementar esto antes de fin de mes, tenemos presupuesto aprobado.",
        },
        {
            "nombre": "Laura Quispe",
            "mensaje": "Solo estoy viendo opciones por ahora, nada urgente.",
        },
        {
            "nombre": "Diego Salas",
            "mensaje": "Cuánto cuesta? Necesito comparar con otras opciones.",
        },
    ]

    leads_analizados = []
    leads_alto_interes = 0

    for lead in leads_prueba:
        analisis = clasificar_lead(lead["nombre"], lead["mensaje"])

        leads_analizados.append({**lead, **analisis})

        if analisis.get("interes") == "alto":
            leads_alto_interes += 1

        print(f"\n{lead['nombre']}:")
        print(f"  Interés      : {analisis.get('interes')}")
        print(f"  Urgencia     : {analisis.get('urgencia')}")
        print(f"  Presupuesto  : {analisis.get('presupuesto_estimado')}")
        print(f"  Acción       : {analisis.get('siguiente_accion')}")

    save_leads(leads_analizados, OUTPUT_FILE)

    print(f"\nLeads procesados : {len(leads_analizados)}")
    print(f"Interés alto     : {leads_alto_interes}")
    print(f"Guardado en      : {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
