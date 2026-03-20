import streamlit as st
import csv
import matplotlib.pyplot as plt

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


# Initialize counters
focus_count = 0
distraction_count = 0
vs_code_count = 0


# Classify
for row in data:
    app = row[1]

    if app == "VS Code":
        vs_code_count += 1

    if app in focus_apps:
        focus_count += 1
    elif app in distraction_apps:
        distraction_count += 1


# Convert to time
focus_time = focus_count * 5
distraction_time = distraction_count * 5
vs_code_time = vs_code_count * 5

total_time = focus_time + distraction_time


# Productivity score
if total_time > 0:
    productivity_score = (focus_time / total_time) * 100
else:
    productivity_score = 0


# Interruption calculation
if (vs_code_time + distraction_time) > 0:
    interruption = (distraction_time / (vs_code_time + distraction_time)) * 100
else:
    interruption = 0


# Display results
st.subheader("Overall Productivity")

st.write("Focus Time (seconds):", focus_time)
st.write("Distraction Time (seconds):", distraction_time)
st.write("Productivity Score:", round(productivity_score, 2), "%")


# Pie chart 1 (Focus vs Distraction)
st.subheader("Focus vs Distraction")

labels = ["Focus", "Distraction"]
values = [focus_time, distraction_time]

fig, ax = plt.subplots()
ax.pie(values, labels=labels, autopct='%1.1f%%')

st.pyplot(fig)


# NEW SECTION — Work Interruption
st.subheader("Work Interruption Analysis")

st.write("VS Code Work Time:", vs_code_time, "seconds")
st.write("Interruption Level:", round(interruption, 2), "%")


# Pie chart 2 (Work vs Distraction)
st.subheader("Work vs Distraction During Coding")

labels2 = ["Work (VS Code)", "Distraction"]
values2 = [vs_code_time, distraction_time]

fig2, ax2 = plt.subplots()
ax2.pie(values2, labels=labels2, autopct='%1.1f%%')

st.pyplot(fig2)