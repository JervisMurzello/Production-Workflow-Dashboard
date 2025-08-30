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
- **Downtime by cause (Pareto analysis)**  
- **Defect trends over time**  
- **Line/Shift performance comparisons**  

---

## 2. Data Sources
The project uses three CSV datasets (sample data included):
- `production_logs.csv` → Production counts, cycle times, planned vs. actual runtime  
- `downtime_events.csv` → Cause and duration of stoppages  
- `quality_checks.csv` → Defects found during inspections  

---

## 🏃 How to Run the Project Locally

Follow these steps to clone and run the **Production Workflow Dashboard** on your local machine.

---

### **1. Clone the Repository**

First, clone this repository to your local machine using Git. Open your terminal or command prompt and run the following commands:

```git clone https://github.com/JervisMurzello/Production-Workflow-Dashboard.git```

```cd Production-Workflow-Dashboard```

Note: Make sure to install Python in the same path where you store the repository.

### 2. Set Up a Python Virtual Environment
It’s a good practice to use a virtual environment to keep dependencies isolated from your system Python.

Create and Activate Virtual Environment
To create and activate a virtual environment, use the following commands:

Windows CMD/PowerShell:

```python -m venv .venv```

```.venv\Scripts\activate```

macOS/Linux (Terminal):


```python3 -m venv .venv```

```.venv/bin/activate```

After activating the virtual environment, you should see (.venv) at the beginning of the command line, indicating that the environment is active.

### 3. Install Required Dependencies
Once the virtual environment is active, you need to install all the required dependencies listed in the requirements.txt file. Run this command:

```pip install -r requirements.txt```

This will install packages such as streamlit, pandas, plotly, etc.

### 4. Add the Data Files

Ensure that the required data files are in the data/ folder for the dashboard to work correctly. Your project should have these sample CSV files in the data/ folder:

sample_production_logs.csv

downtime_events.csv

quality_checks.csv

If these files are missing, please obtain or create sample data files that match the structure described in the README.md.

### 5. Run the Streamlit Dashboard

With the dependencies installed and data files in place, you can now run the Streamlit app using the following command:

```streamlit run app/streamlit_app.py```

This will start a local server and automatically open the dashboard in your default web browser at:

**http://localhost:8501**


If the dashboard does not open automatically, copy and paste the URL into your browser.

### 6. Explore the Dashboard
Once the app is running, you can explore the following features:

**Sidebar Filters:** Filter data by date range, production line, shift, and product.

**KPI Cards:** View key performance indicators such as OEE (Overall Equipment Effectiveness), Availability, Performance, and Quality.

**Trend Charts:** Analyze trends in units produced, downtime, and defect rates over time.

**Pareto Chart:** View the top downtime causes using a Pareto chart.

### 7. Stop the Server

When you are done exploring, stop the Streamlit app by pressing **Ctrl + C** in the terminal or command prompt window.

### 8. Optional: Deactivate the Virtual Environment

Once you’re done, you can deactivate the virtual environment by running:


```deactivate```

This will return you to your system's Python environment.
