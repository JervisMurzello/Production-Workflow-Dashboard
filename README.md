# 📑 Production Workflow Dashboard — Documentation

This project is fully documented to make it easy for others to understand, run, and extend.

---

## 1. Project Overview
The **Production Workflow Dashboard** analyzes **30 days of manufacturing data** across multiple lines and shifts.  
It calculates and visualizes key KPIs such as:
- **Availability**
- **Performance**
- **Quality**
- **Overall Equipment Effectiveness (OEE)**

It also provides insights into:
- Downtime by cause (Pareto analysis)  
- Defect trends over time  
- Line/Shift performance comparisons  

---

## 2. Data Sources
The project uses three CSV datasets (sample data included):
- `production_logs.csv` → Production counts, cycle times, planned vs. actual runtime  
- `downtime_events.csv` → Cause and duration of stoppages  
- `quality_checks.csv` → Defects found during inspections  

---

## 3. How to Run the Project

# Step 1: Clone the repository

git clone https://github.com/JervisMurzello/Production-Workflow-Dashboard.git
cd Production-Workflow-Dashboard

Make sure to install python on the same path where you store the above repository.
# Step 2: Create and activate a Python virtual environment
Windows CMD/PowerShell:
python -m venv .venv
.venv\Scripts\activate

macOS/Linux Terminal:
python3 -m venv .venv
source .venv/bin/activate

# Step 3: Install required dependencies
pip install -r requirements.txt

# Step 4: Ensure data files are present in the "data/" folder
 You should have the following CSV files:
 - sample_production_logs.csv
 - downtime_events.csv
 - quality_checks.csv

# Step 5: Run the Streamlit dashboard
streamlit run app/streamlit_app.py

# Step 6: Open the dashboard in your browser
The app will open at http://localhost:8501 (copy-paste into browser if it doesn't open automatically)

# Step 7: Stop the server
Press Ctrl + C to stop the Streamlit server

# Step 8: Optional - Deactivate the virtual environment
deactivate
