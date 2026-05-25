import json
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_FILE = os.path.join(BASE_DIR, "leads_report.json")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def search_leads_by_interest(level: str) -> str:
    try:
        with open(REPORT_FILE, "r", encoding="utf-8") as f:
            leads = json.load(f)

        filtered = [l for l in leads if l.get("analysis", {}).get("interest") == level]

        if not filtered:
            return f"There are no leads with {level} interest."

        names = [l["name"] for l in filtered]

        return f"{len(filtered)} leads with {level} interest: {', '.join(names)}"

    except FileNotFoundError:
        return "Report not found. Run the pipeline first."


def count_total_leads() -> str:
    try:
        with open(REPORT_FILE, "r", encoding="utf-8") as f:
            leads = json.load(f)

        return f"Total leads in the report: {len(leads)}"

    except FileNotFoundError:
        return "Report not found."


def get_recommended_action(name: str) -> str:
    try:
        with open(REPORT_FILE, "r", encoding="utf-8") as f:
            leads = json.load(f)

        # Find the lead by name
        # hint: use next() with a generator expression to find the lead
        lead = next((l for l in leads if l["name"].lower() == name.lower()), None)

        if lead is None:
            return f"Lead not found: {name}"

        action = lead.get("analysis", {}).get("next_action", "No action defined.")
        return f"Recommended action for {name}: {action}"

    except FileNotFoundError:
        return "Report not found."


# Function name → actual function map
TOOLS_MAP = {
    "search_leads_by_interest": search_leads_by_interest,
    "count_total_leads": count_total_leads,
    "get_recommended_action": get_recommended_action,
}

# Tool descriptions for the model
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_leads_by_interest",
            "description": "Searches and lists leads based on their interest level",
            "parameters": {
                "type": "object",
                "properties": {
                    "level": {
                        "type": "string",
                        "description": "Lead interest level",
                        "enum": ["high", "medium", "low"],
                    }
                },
                "required": ["level"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "count_total_leads",
            "description": "Counts the total number of leads in the report",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_recommended_action",
            "description": "Gets the recommended action for a specific lead",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "The name of the lead"}
                },
                "required": ["name"],
            },
        },
    },
]


def run_agent(question: str):
    """
    Full agent cycle:
    1. Receives a question
    2. Model decides whether to use a tool
    3. If yes, execute the tool
    4. Return the result to the model
    5. Model generates the final response
    """

    print(f"\nQuestion: {question}")
    print("-" * 40)

    messages = [
        {
            "role": "system",
            "content": (
                "You are a sales assistant. "
                "You ONLY have access to the provided tools. "
                "Never invent tools. "
                "If the information is unavailable, say so."
            ),
        },
        {"role": "user", "content": question},
    ]

    # Step 1 — first model call
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        tools=TOOLS,
        tool_choice="auto",  # the model decides whether to use a tool
        temperature=0,
    )

    message = response.choices[0].message

    # Step 2 — does the model want to use a tool?
    if message.tool_calls:

        for tool_call in message.tool_calls:

            name = tool_call.function.name

            raw_arguments = tool_call.function.arguments

            try:
                arguments = json.loads(raw_arguments) if raw_arguments else {}
            except json.JSONDecodeError:
                arguments = {}

            if arguments is None:
                arguments = {}

            print(f"Tool used: {name}({arguments})")

            # Step 3 — execute the real function
            function = TOOLS_MAP.get(name)
            if function is None:
                print(f"Tool not found: {name}")
                continue
            result = function(**arguments)

            print(f"Result     : {result}")

            # Step 4 — append result to conversation history
            messages.append({"role": "assistant", "tool_calls": [tool_call]})

            messages.append(
                {"role": "tool", "tool_call_id": tool_call.id, "content": result}
            )

        # Step 5 — second model call including tool results
        final_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0,
        )

        answer = final_response.choices[0].message.content

    else:
        # Model responded directly without tools
        answer = message.content

    print(f"Answer     : {answer}\n")

    return answer


if __name__ == "__main__":

    run_agent("How many leads do we have in total?")

    run_agent("Who are the high-interest leads?")

    run_agent("What is the difference between a lead and a customer?")

    run_agent("What should I do with Carlos Barrientos?")
