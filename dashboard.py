import streamlit as st
import csv

st.title("Procrastination Detection System")
st.header("Productivity Dashboard")


# Define apps
focus_apps = [
    "VS Code",
    "Visual Studio",
    "PyCharm",
    "Jupyter",
    "Notepad",
    "Word",
    "Excel",
    "Power BI",
    "SQL Workbench"
]

distraction_apps = [
    "YouTube",
    "Instagram",
    "WhatsApp",
    "Facebook",
    "Twitter",
    "Netflix",
    "Hotstar",
    "Amazon Prime",
    "Prime Video",
    "Hill Climb Racing"
]


# Read CSV
data = []

with open("activity_log.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        data.append(row)


# Count
focus_count = 0
distraction_count = 0

for row in data:
    app = row[1]

    if app in focus_apps:
        focus_count += 1
    elif app in distraction_apps:
        distraction_count += 1


# Convert to time
focus_time = focus_count * 5
distraction_time = distraction_count * 5

total_time = focus_time + distraction_time


# Productivity score
if total_time > 0:
    productivity_score = (focus_time / total_time) * 100
else:
    productivity_score = 0


# Display results
st.subheader("Results")

st.write("Focus Time (seconds):", focus_time)
st.write("Distraction Time (seconds):", distraction_time)
st.write("Productivity Score:", round(productivity_score, 2), "%")