import logging
import os
import time

import concurrent
import schedule
from utils import load_leads_csv, save_report_json, print_summary_report, setup_logging
from classifier import classify_lead
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LEADS_FILE = os.path.join(BASE_DIR, "leads.csv")
REPORT_FILE = os.path.join(BASE_DIR, "report.json")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")


# def process_leads(leads):
#     results = []

#     for i, lead in enumerate(leads, start=1):
#         name = lead["name"]
#         message = lead["message"]

#         print(f"Processing lead {i}/{len(leads)}: {name}")

#         analysis = classify_lead(name, message)
#         results.append(
#             {
#                 "name": name,
#                 "email": lead["email"],
#                 "phone": lead["phone"],
#                 "message": message,
#                 "analysis": analysis,
#             }
#         )

#     return results


def process_single_lead(lead):
    """
    Process a single lead and return the result. This function is designed to be used in a concurrent execution context.
    """
    try:
        analysis = classify_lead(lead["name"], lead["message"])
        return {
            "name": lead["name"],
            "email": lead["email"],
            "phone": lead["phone"],
            "message": lead["message"],
            "analysis": analysis,
        }
    except Exception as e:
        logging.error(f"Error processing lead {lead['name']}: {e}")
        raise e  # Re-raise the exception to be handled by the caller


def process_leads(leads, max_workers=5):
    """
    Process a list of leads concurrently using a ThreadPoolExecutor. This can significantly reduce the processing time when dealing with a large number of leads.
    """
    results = []
    total = len(leads)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Create a dictionary to keep track of the futures and their corresponding leads
        futures = {executor.submit(process_single_lead, lead): lead for lead in leads}

        for future in as_completed(futures):
            lead = futures[future]
            try:
                result = future.result()
                results.append(result)
                logging.info(f"Processed lead: {lead['name']} ({len(results)}/{total})")
            except Exception as e:
                logging.error(f"Error processing lead {lead['name']}: {e}")

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
        print_summary_report(leads_processed)

        from utils import send_discord_notification

        send_discord_notification(leads_processed, DISCORD_WEBHOOK_URL)

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
