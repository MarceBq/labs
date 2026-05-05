import os
from utils import load_leads_csv, save_report_json, print_summary_report
from classifier import classify_lead

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LEADS_FILE = os.path.join(BASE_DIR, "leads.csv")
REPORT_FILE = os.path.join(BASE_DIR, "report.json")


def proccess_leads(leads):
    results = []

    for i, lead in enumerate(leads, start=1):
        name = lead["name"]
        message = lead["message"]

        print(f"Processing lead {i}/{len(leads)}: {name}")

        analysis = classify_lead(name, message)
        results.append(
            {
                "name": name,
                "email": lead["email"],
                "phone": lead["phone"],
                "message": message,
                "analysis": analysis,
            }
        )

    return results


def main():
    print("Loading leads from CSV...")
    leads = load_leads_csv(LEADS_FILE)
    print(f"Total leads loaded: {len(leads)}")

    print("Processing leads with AI classifier...")

    leads_proccesed = proccess_leads(leads)

    save_report_json(leads_proccesed, REPORT_FILE)
    print_summary_report(leads_proccesed)


if __name__ == "__main__":
    main()
