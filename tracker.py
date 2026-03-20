import pygetwindow as gw
import time
import csv
from datetime import datetime
import os

# Show where CSV is stored
print("CSV will be saved at:", os.getcwd())


def get_app_name(title):
    title_lower = title.lower()

    # VS Code
    if "visual studio code" in title_lower:
        return "VS Code"

    # Chrome tabs
    elif "google chrome" in title_lower:
        parts = title.split(" - ")
        if len(parts) > 1:
            name = parts[0]

            # Remove numbers like (2195)
            if ")" in name:
                name = name.split(")")[-1].strip()

            return name
        return "Chrome"

    # Other apps (PDF, WhatsApp, Power BI, etc.)
    else:
        parts = title.split(" - ")
        return parts[0]


# Create CSV file with header if not exists
if not os.path.exists("activity_log.csv"):
    with open("activity_log.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Application"])


while True:
    try:
        window = gw.getActiveWindow()

        # Handle Desktop / empty window
        if window is not None and window.title.strip() != "":
            app_name = get_app_name(window.title)
        else:
            app_name = "Desktop"

        # Get current time
        current_time = datetime.now().strftime("%H:%M:%S")

        # Write to CSV
        with open("activity_log.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([current_time, app_name])

        # Print output
        print("Saved:", current_time, "-", app_name)

    except Exception as e:
        print("Error:", e)

    time.sleep(5)