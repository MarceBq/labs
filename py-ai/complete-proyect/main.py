import logging
import os
import time

import schedule
from utils import load_leads_csv, save_report_json, print_summary_report, setup_logging
from classifier import classify_lead

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LEADS_FILE = os.path.join(BASE_DIR, "leads.csv")
REPORT_FILE = os.path.join(BASE_DIR, "report.json")


def process_leads(leads):
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


def run_pipeline():
    """
    This function runs the entire pipeline: loading leads, processing them with the AI classifier, and saving the report.
    """
    logging.info("=" * 40)
    logging.info("Starting AI Lead Classification Pipeline")

    try:
        leads = load_leads_csv(LEADS_FILE)

        logging.info(f"Loaded {len(leads)} leads from {LEADS_FILE}")

        leads_processed = process_leads(leads)

        save_report_json(leads_processed, REPORT_FILE)

        logging.info(
            f"Pipeline report completed and saved successfully to {REPORT_FILE}"
        )

    except Exception as e:

        logging.error(f"An error occurred: {e}")


# def main():
#     print("Loading leads from CSV...")
#     leads = load_leads_csv(LEADS_FILE)
#     print(f"Total leads loaded: {len(leads)}")

#     print("Processing leads with AI classifier...")

#     leads_processed = process_leads(leads)

#     save_report_json(leads_proccesed, REPORT_FILE)
#     print_summary_report(leads_proccesed)


if __name__ == "__main__":
    setup_logging()

    # Execute the pipeline inmediately when the script is run to process the leads and generate the report.
    run_pipeline()

    # After the initial execution, schedule the pipeline to run every hour to keep the report updated with new leads.
    schedule.every(1).hours.do(run_pipeline)

    logging.info(
        "Scheduler activated. The pipeline will run every hour to process new leads and update the report."
    )
    logging.info("Press Ctrl+C to exit.")

    while True:
        schedule.run_pending()
        time.sleep(1)
