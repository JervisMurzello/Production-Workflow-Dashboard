import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Production Workflow Dashboard", layout="wide")

@st.cache_data
def load_data():
    prod = pd.read_csv("data/sample_production_logs.csv", parse_dates=["date"])
    dt = pd.read_csv("data/downtime_events.csv", parse_dates=["date"])
    qc = pd.read_csv("data/quality_checks.csv", parse_dates=["date"])
    return prod, dt, qc

prod, dt, qc = load_data()

st.title("🏭 Production Workflow Dashboard")

# Filters
with st.sidebar:
    st.header("Filters")
    dates = st.date_input("Date range", [prod["date"].min(), prod["date"].max()])
    line = st.multiselect("Production line", sorted(prod["production_line"].unique()), default=list(sorted(prod["production_line"].unique())))
    shift = st.multiselect("Shift", sorted(prod["shift"].unique()), default=list(sorted(prod["shift"].unique())))
    product = st.multiselect("Product", sorted(prod["product"].unique()), default=list(sorted(prod["product"].unique())))

mask = (
    (prod["date"] >= pd.to_datetime(dates[0])) &
    (prod["date"] <= pd.to_datetime(dates[-1])) &
    (prod["production_line"].isin(line)) &
    (prod["shift"].isin(shift)) &
    (prod["product"].isin(product))
)
prod_f = prod.loc[mask]
dt_f = dt.loc[
    (dt["date"] >= pd.to_datetime(dates[0])) &
    (dt["date"] <= pd.to_datetime(dates[-1])) &
    (dt["production_line"].isin(line)) &
    (dt["shift"].isin(shift))
]
qc_f = qc.loc[
    (qc["date"] >= pd.to_datetime(dates[0])) &
    (qc["date"] <= pd.to_datetime(dates[-1])) &
    (qc["production_line"].isin(line)) &
    (qc["shift"].isin(shift)) &
    (qc["product"].isin(product))
]

# KPI calculations
planned_time = prod_f["planned_minutes"].sum()
downtime = prod_f["downtime_minutes"].sum()
runtime = max(1, planned_time - downtime)

units_total = prod_f["units_total"].sum()
units_good = prod_f["units_good"].sum()
units_defect = prod_f["units_defect"].sum()

# OEE components
availability = runtime / planned_time if planned_time else 0
# Performance uses ideal cycle time weighted average
if len(prod_f):
    weighted_ideal = (prod_f["ideal_cycle_time_sec"] * prod_f["units_total"]).sum() / max(1, prod_f["units_total"].sum())
else:
    weighted_ideal = 0
theoretical_output = runtime * 60 / max(1e-9, weighted_ideal) if weighted_ideal else 0
performance = units_total / theoretical_output if theoretical_output else 0
quality = units_good / max(1, units_total)

oee = availability * performance * quality

# KPI cards
kpi_cols = st.columns(4)
kpi_cols[0].metric("OEE", f"{oee*100:.1f}%",
                   help="Overall Equipment Effectiveness = Availability × Performance × Quality")
kpi_cols[1].metric("Availability", f"{availability*100:.1f}%")
kpi_cols[2].metric("Performance", f"{performance*100:.1f}%")
kpi_cols[3].metric("Quality", f"{quality*100:.1f}%")

# Trends
st.subheader("Production & Downtime Over Time")
prod_daily = prod_f.groupby("date", as_index=False).agg(
    units_total=("units_total", "sum"),
    units_good=("units_good", "sum"),
    downtime_minutes=("downtime_minutes", "sum")
)

c1, c2 = st.columns(2)
with c1:
    fig1 = px.line(prod_daily, x="date", y=["units_total", "units_good"], title="Units Produced vs Good Units")
    st.plotly_chart(fig1, use_container_width=True)
with c2:
    fig2 = px.bar(prod_daily, x="date", y="downtime_minutes", title="Downtime Minutes")
    st.plotly_chart(fig2, use_container_width=True)

# Pareto of downtime
st.subheader("Downtime Pareto (Top causes)")
pareto = dt_f.groupby("event_type", as_index=False)["duration_minutes"].sum().sort_values("duration_minutes", ascending=False)
fig3 = px.bar(pareto, x="event_type", y="duration_minutes", title="Downtime by Cause")
st.plotly_chart(fig3, use_container_width=True)

# Quality
st.subheader("Quality Sampling")
qc_daily = qc_f.groupby("date", as_index=False).agg(defects_found=("defects_found", "sum"), sample_size=("sample_size", "sum"))
qc_daily["defect_rate"] = qc_daily["defects_found"] / qc_daily["sample_size"]
fig4 = px.line(qc_daily, x="date", y="defect_rate", title="Defect Rate (QC Samples)")
st.plotly_chart(fig4, use_container_width=True)

st.caption("Demo dataset and dashboard scaffold. Replace CSVs with real data feeds, extend KPIs, and add role-based access.")
