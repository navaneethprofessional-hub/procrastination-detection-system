import pygetwindow as gw
import time

def get_app_name(title):
    title_lower = title.lower()

    # VS Code
    if "visual studio code" in title_lower:
        return "VS Code"

    # Chrome tabs (YouTube, ChatGPT, etc.)
    elif "google chrome" in title_lower:
        parts = title.split(" - ")
        if len(parts) > 1:
            return parts[0]
        return "Chrome"

    # All other apps (WhatsApp, Power BI, PDF, Games, etc.)
    else:
        return title


while True:
    try:
        window = gw.getActiveWindow()

        if window is not None:
            app_name = get_app_name(window.title)
            print(app_name)

    except:
        print("Error detecting window")

    time.sleep(5)