→ Title: Procrastination Detection System

→ Overview:  
This project tracks user activity on a computer and analyzes productivity by identifying focus and distraction patterns. It calculates a productivity score and procrastination percentage based on application usage.

→ Features:  
- Real-time application tracking  
- Automatic data logging in CSV format  
- Classification of applications into focus and distraction categories  
- Productivity score calculation  
- Procrastination analysis  
- Interactive dashboard using Streamlit  
- Visualization using pie chart and bar chart  

→ Working:  
- The system tracks active applications at regular intervals (every 5 seconds)  
- Data is stored in a CSV file  
- Applications are classified into focus and distraction based on predefined rules  
 → The system calculates:  
  - Focus time  
  - Distraction time  
  - Productivity score  
  - Procrastination percentage  
- Results are displayed using a web-based dashboard  

→ Output:  
- Pie chart showing focus vs distraction  
- Bar chart showing work vs procrastination  
- Productivity score  
- Procrastination percentage  

→ Technologies Used:  
- Python  
- Streamlit  
- Matplotlib  
- CSV  
- PyGetWindow  

→ How to Run:  

Step 1: Install dependencies  
pip install streamlit pygetwindow matplotlib  

Step 2: Run tracker  
python tracker.py  

Step 3: Run dashboard  
python -m streamlit run dashboard.py  

→ Future Improvements:  
- AI-based classification of applications  
- Detection of educational vs non-educational content  
- Real-time notifications  
- Extension to mobile platforms  