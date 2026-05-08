import csv
import json
import logging
import os
import requests


def send_discord_notification(leads_processed, webhook_url):
    if not webhook_url:
        logging.warning("No Discord webhook URL provided. Skipping notification.")
        return

    # Filter high interest leads
    high_interest_leads = [
        lead
        for lead in leads_processed
        if lead.get("analysis", {}).get("interest") == "high"
    ]

    if not high_interest_leads:
        logging.info("No high interest leads to notify.")
        return

    # Create the message content
    lines = [f"**New High Interest Leads Processed: {len(high_interest_leads)}**\n"]
    for lead in high_interest_leads:
        action = lead["analysis"].get("next_action", "-")
        lines.append(f"**{lead['name']}** - {lead['email']}")
        lines.append(f"  -> {action}\n")

    message_content = "\n".join(lines)

    try:
        response = requests.post(
            webhook_url,
            json={"content": message_content},
            timeout=10,
        )
        response.raise_for_status()
        logging.info(
            "Discord notification sent successfully. Total high interest leads: %d",
            len(high_interest_leads),
        )
    except Exception as e:
        logging.error(f"Error sending Discord notification: {str(e)}")


def setup_logging(log_dir="logs"):
    """
    Setup logging configuration to log messages to a file with timestamps.
    """

    os.makedirs(log_dir, exist_ok=True)  # Ensure the log directory exists

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(
                f"{log_dir}/pipeline.log",
                encoding="utf-8",
            ),
            logging.StreamHandler(),  # Also log to console
        ],
    )


def load_leads_csv(file_path):
    try:
        leads = []
        with open(file_path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                leads.append(row)
        # print(f"Loaded {len(leads)} leads from {file_path}")
        return leads

    except Exception as e:
        logging.error(f"Error loading leads from {file_path}: {e}")
        raise e


def save_report_json(data, file_path):
    try:
        with open(file_path, mode="w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile)
        print(f"Report saved to {file_path}")
    except Exception as e:
        logging.error(f"Error saving report to {file_path}: {e}")
        raise e


def print_summary_report(lead_processed):
    total = len(lead_processed)

    count = {"high": 0, "medium": 0, "low": 0, "error": 0}
    for lead in lead_processed:
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
        for lead in lead_processed
        if lead.get("analysis", {}).get("interest") == "high"
    ]
    if highs:
        print("\n Priority Leads (High Interest):")
        for lead in highs:
            action = lead.get("analysis", {}).get("next_action", "-")
            print(f"  -> {lead['name']:<20} | {action}")
