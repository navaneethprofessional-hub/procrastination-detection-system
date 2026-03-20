# Define focus and distraction apps
focus_apps = [
    "VS Code",
    "Word",
    "Power BI",
    "Notepad",
    "Jupyter"
]

distraction_apps = [
    "YouTube",
    "Instagram",
    "WhatsApp",
    "Netflix",
    "Hill Climb Racing"
]


import csv

data = []

# Read CSV file
with open("activity_log.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    for row in reader:
        data.append(row)

print("Data:", data)


# Initialize counters
focus_count = 0
distraction_count = 0
unknown_apps = set()


# Classify data
for row in data:
    app = row[1]

    if app in focus_apps:
        focus_count += 1
    elif app in distraction_apps:
        distraction_count += 1
    else:
        unknown_apps.add(app)


# Print results
print("\nFocus Count:", focus_count)
print("Distraction Count:", distraction_count)
print("Unknown Apps:", unknown_apps)

# Convert count to time (in seconds)
focus_time = focus_count * 5
distraction_time = distraction_count * 5

# Convert seconds to minutes
focus_minutes = focus_time / 60
distraction_minutes = distraction_time / 60

print("\nFocus Time (seconds):", focus_time)
print("Distraction Time (seconds):", distraction_time)

print("\nFocus Time (minutes):", round(focus_minutes, 2))
print("Distraction Time (minutes):", round(distraction_minutes, 2))

# Total time
total_time = focus_time + distraction_time

# Productivity score (in percentage)
if total_time > 0:
    productivity_score = (focus_time / total_time) * 100
else:
    productivity_score = 0

print("\nProductivity Score:", round(productivity_score, 2), "%")