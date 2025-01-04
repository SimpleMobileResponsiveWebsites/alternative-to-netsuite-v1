# app.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import plotly.express as px

# Configuration and Page Setup
st.set_page_config(
    page_title="NetSuite Dashboard Clone",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        padding-top: 0rem;
    }
    .block-container {
        padding-top: 1rem;
    }
    .stMetric {
        background-color: white;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("Reminders")
    st.info("📋 Expense Reports to Approve")
    st.info("📝 Purchase Request to Approve")
    st.warning("⚠️ Invoice > 30 Days > 50K")
    st.success("✓ New Customers")
    
    st.header("Navigation Shortcut Group")
    st.subheader("Executive Management")
    st.markdown("📊 Sales")
    st.markdown("📈 Customer Profitability")
    st.markdown("📉 Gross Profit Stats")
    
    st.subheader("Inventory Management")
    st.markdown("📦 Inventory Status")
    st.markdown("🔄 Purchase Order History")

# Main Content
st.title("Dashboard")

# Create tabs for different sections
tabs = st.tabs(["Balance Sheet", "Trial Balance", "Income Statement", "Budget vs Actual"])

# KPI Metrics Row
col1, col2, col3, col4 = st.columns(4)

# Sample data for KPIs
kpi_data = {
    "Sales": {"value": "$3,735,857", "change": "+23.5%"},
    "Expenses": {"value": "$1,835,031", "change": "-24.4%"},
    "Revenue": {"value": "$3,472,235", "change": "+20.5%"},
    "Receivables": {"value": "$2,026,663", "change": "+8.2%"}
}

with col1:
    st.metric("Sales", kpi_data["Sales"]["value"], kpi_data["Sales"]["change"])
with col2:
    st.metric("Expenses", kpi_data["Expenses"]["value"], kpi_data["Expenses"]["change"])
with col3:
    st.metric("Revenue", kpi_data["Revenue"]["value"], kpi_data["Revenue"]["change"])
with col4:
    st.metric("Receivables", kpi_data["Receivables"]["value"], kpi_data["Receivables"]["change"])

# Create sample data for the revenue trend chart
dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
revenue_data = pd.DataFrame({
    'Date': dates,
    'Revenue': [3.2, 3.4, 3.7, 3.5, 3.8, 3.6, 3.9, 3.7, 3.8, 4.0, 3.9, 3.7],
})

# Revenue Trend Chart
st.subheader("Revenue by Period Trend")
fig = px.line(revenue_data, x='Date', y='Revenue',
              labels={'Revenue': 'Revenue (Millions $)', 'Date': 'Period'},
              line_shape='spline')
fig.update_layout(
    height=400,
    margin=dict(l=20, r=20, t=20, b=20),
)
st.plotly_chart(fig, use_container_width=True)

# Detailed Metrics Table
st.subheader("Key Performance Indicators")
detailed_metrics = pd.DataFrame({
    'Metric': ['Sales', 'Expenses', 'Revenue', 'Receivables', 'Total Bank Balance',
               'Payables', 'COGS', 'Inventory', 'Total Pipeline Deals', 'Credit Card Balance'],
    'Current Period': ['$3,735,857', '$1,835,031', '$3,472,235', '$2,026,663', '$3,824,663',
                      '$2,026,663', '$1,440,722', '$1,297,591', '$4,500,000', '$840'],
    'Previous Period': ['$3,026,079', '$2,286,981', '$3,025,079', '$1,881,027', '$3,266,078',
                       '$1,297,289', '$1,042,042', '$1,097,638', '$4,200,000', '$775'],
    'Change': ['+23.5%', '-24.4%', '+20.5%', '+8.2%', '+17.0%',
               '+56.2%', '+12.3%', '+18.3%', '+7.1%', '+8.4%']
})

st.dataframe(detailed_metrics, hide_index=True, use_container_width=True)
