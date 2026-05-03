import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, "leads.json")
OUTPUT_FILE = os.path.join(BASE_DIR, "processed_leads.json")

def load_leads(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
    
def calcate_priority(lead):
    if lead["compras"] >= 3:
        return "high"
    elif lead["compras"] >= 1:
        return "medium"
    else:
        return "low"

def save_leads(leads, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(leads, file, indent=2, ensure_ascii=False)
        
def main():
    leads = load_leads(INPUT_FILE)
    
    higth_priority = 0
    mid_priority = 0
    low_priority = 0
        
    for lead in leads:
        lead["priority"] = calcate_priority(lead)
        if lead["priority"] == "high":
            higth_priority += 1
        elif lead["priority"] == "medium":
            mid_priority += 1
        else:
            low_priority += 1
        
    save_leads(leads, OUTPUT_FILE)
    print(f"""
              High Priority: {higth_priority}
              Medium Priority: {mid_priority}
              Low Priority: {low_priority}
              Saved processed leads to {OUTPUT_FILE}""")
    
main()