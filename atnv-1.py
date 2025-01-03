import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

def create_gauge_chart():
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 3.7,
        title = {'text': "Revenue"},
        number={'prefix': "$", 'suffix': "M"},
        gauge = {
            'axis': {'range': [None, 5]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 5], 'color': "lightgray"}
            ],
        }
    ))
    fig.update_layout(height=200)
    return fig

def main():
    # Page configuration
    st.set_page_config(layout="wide", page_title="NetSuite Dashboard")
    
    # Initialize session state for cross-page data sharing
    if 'key_metrics' not in st.session_state:
        st.session_state.key_metrics = {
            'revenue': 3.7,
            'sales': 5.2,
            'expenses': 8.1,
            'receivables': 2.1
        }
    
    # Top navigation bar
    col1, col2, col3, col4 = st.columns([2, 6, 1, 1])
    with col1:
        st.image("https://via.placeholder.com/150x50", caption="")  # Logo placeholder
    with col2:
        tabs = ["Activities", "Billing", "Customers", "Vendors", "Payroll and HR", 
                "Financial", "Reports", "Analytics", "Documents", "Setup"]
        st.selectbox("Navigation", tabs, label_visibility="collapsed")
    with col3:
        st.button("Help")
    with col4:
        st.button("Feedback")

    # Main content area
    left_col, middle_col, right_col = st.columns([1, 2, 1])

    # Left sidebar
    with left_col:
        st.markdown("### Reminders")
        reminders = [
            "📊 Expense Reports to Approve",
            "📝 Purchase Request to Approve",
            "❗ Invoices > 30 Days > $5K",
            "👥 New Customers"
        ]
        for reminder in reminders:
            st.markdown(reminder)
        
        # Updated Navigation Shortcut Group with page switching
        st.markdown("### Navigation Shortcut Group")
        if st.button("Executive Management", key="exec_mgmt"):
            st.switch_page("pages/1_Executive_Management.py")
        if st.button("Sales", key="sales"):
            st.switch_page("pages/2_Sales.py")
        if st.button("Customer Hierarchy", key="customer"):
            st.switch_page("pages/3_Customer_Hierarchy.py")
        if st.button("Inventory Management", key="inventory"):
            st.switch_page("pages/4_Inventory_Management.py")

    # Middle section
    with middle_col:
        st.markdown("### Tiles")
        tile_cols = st.columns(4)
        tiles = ["Balance Sheet", "Trial Balance", "Income Statement", "Budget vs Actual"]
        for i, tile in enumerate(tiles):
            with tile_cols[i]:
                st.button(tile)
        
        st.markdown("### Key Performance Indicators")
        kpi_cols = st.columns(4)
        kpis = ["Sales", "Expenses", "Revenue", "Receivables"]
        for i, kpi in enumerate(kpis):
            with kpi_cols[i]:
                st.metric(
                    label=kpi,
                    value=f"${round(float(1000000 + i*500000)/1000000, 1)}M",
                    delta=f"{5 + i}%"
                )

    # Right column
    with right_col:
        st.markdown("### KPI Meter")
        st.plotly_chart(create_gauge_chart(), use_container_width=True)
        
        st.markdown("### Revenue by Period Trend")
        # Create a simple line chart for revenue trend
        chart_data = pd.DataFrame({
            'Period': pd.date_range(start='2024-01-01', periods=6, freq='M'),
            'Revenue': [3.2, 3.4, 3.5, 3.7, 3.8, 3.9]
        })
        st.line_chart(chart_data.set_index('Period'))

if __name__ == "__main__":
    main()
