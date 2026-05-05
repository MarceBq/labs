import csv
import json
import os


def load_leads_csv(file_path):
    leads = []
    with open(file_path, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            leads.append(row)
    # print(f"Loaded {len(leads)} leads from {file_path}")
    return leads


def save_report_json(data, file_path):
    with open(file_path, mode="w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile)
    print(f"Report saved to {file_path}")


def print_summary_report(lead_proccesed):
    total = len(lead_proccesed)

    count = {"high": 0, "medium": 0, "low": 0, "error": 0}
    for lead in lead_proccesed:
        interest = lead.get("analysis", {}).get("interest", "error")
        if interest in count:
            count[interest] += 1
        else:
            count["error"] += 1

    print("\n" + "=" * 45)
    print("   RESUME LEADS PROCESSED")
    print("=" * 45)
    print(f"  Total Leads Proccesed : {total}")
    print(f"  High Interest    : {count['high']}")
    print(f"  Medium Interest  : {count['medium']}")
    print(f"  Low Interest     : {count['low']}")
    if count["error"] > 0:
        print(f"  Errors IA        : {count['error']}")
    print("=" * 45)

    # Show only the high interest leads with recommended actions
    highs = [
        lead
        for lead in lead_proccesed
        if lead.get("analysis", {}).get("interest") == "high"
    ]
    if highs:
        print("\n Priority Leads (High Interest):")
        for lead in highs:
            action = lead.get("analysis", {}).get("next_action", "-")
            print(f"  -> {lead['name']:<20} | {action}")
