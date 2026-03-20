import pygetwindow as gw
import time
import csv
from datetime import datetime
import os

# Display the current working directory (where CSV will be stored)
print("CSV will be saved at:", os.getcwd())


# Function to extract clean application name from window title
def get_app_name(title):
    title_lower = title.lower()

    # Detect VS Code
    if "visual studio code" in title_lower:
        return "VS Code"

    # Detect Google Chrome and extract tab name
    elif "google chrome" in title_lower:
        parts = title.split(" - ")
        
        if len(parts) > 1:
            name = parts[0]

            # Remove unwanted numbers like (2195)
            if ")" in name:
                name = name.split(")")[-1].strip()

            return name

        return "Chrome"

    # Handle all other applications (PDF, WhatsApp, etc.)
    else:
        parts = title.split(" - ")
        return parts[0]


# Create CSV file with header if it does not exist
if not os.path.exists("activity_log.csv"):
    with open("activity_log.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Application"])


# Infinite loop to continuously track applications
while True:
    try:
        # Get the currently active window
        window = gw.getActiveWindow()

        # Handle cases where no window title is available (Desktop)
        if window is not None and window.title.strip() != "":
            app_name = get_app_name(window.title)
        else:
            app_name = "Desktop"

        # Get current time in HH:MM:SS format
        current_time = datetime.now().strftime("%H:%M:%S")

        # Append data to CSV file
        with open("activity_log.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([current_time, app_name])

        # Display output in terminal
        print("Saved:", current_time, "-", app_name)

    except Exception as e:
        # Handle errors gracefully
        print("Error:", e)

    # Wait for 5 seconds before next tracking
    time.sleep(5)