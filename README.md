## 📑 Documentation

This project is fully documented to make it easy for others to understand, run, and extend.

### 1. Project Overview
The Production Workflow Dashboard analyzes **30 days of manufacturing data** across multiple lines and shifts.  
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

### 2. Data Sources
The project uses three CSV datasets (sample data included):
- `production_logs.csv` → Production counts, cycle times, planned vs. actual runtime  
- `downtime_events.csv` → Cause and duration of stoppages  
- `quality_checks.csv` → Defects found during inspections  

---

### 3. How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/production-workflow-dashboard.git
   cd production-workflow-dashboard

