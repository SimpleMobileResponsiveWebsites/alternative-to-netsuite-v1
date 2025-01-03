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

def exec_management_view():
    st.title("Executive Management Dashboard")
    # Add executive management content here
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total Revenue", value="$15.2M", delta="+12%")
    with col2:
        st.metric(label="Gross Margin", value="68%", delta="+3%")
    with col3:
        st.metric(label="Operating Expenses", value="$8.1M", delta="-5%")
    with col4:
        st.metric(label="Cash Position", value="$5.4M", delta="+8%")

def sales_view():
    st.title("Sales Dashboard")
    # Add sales content here
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total Sales", value="$5.2M", delta="+15%")
    with col2:
        st.metric(label="New Customers", value="127", delta="+23")
    with col3:
        st.metric(label="Pipeline Value", value="$8.7M", delta="+7%")
    with col4:
        st.metric(label="Win Rate", value="62%", delta="+5%")

def customer_hierarchy_view():
    st.title("Customer Hierarchy")
    # Add customer hierarchy content here
    st.subheader("Customer Search")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.text_input("Search Customers", placeholder="Enter customer name or ID")
    with col2:
        st.button("Search")

def inventory_management_view():
    st.title("Inventory Management")
    # Add inventory management content here
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total SKUs", value="1,234", delta="+12")
    with col2:
        st.metric(label="Stock Value", value="$2.1M", delta="+5%")
    with col3:
        st.metric(label="Low Stock Items", value="23", delta="-3")
    with col4:
        st.metric(label="Turnover Rate", value="4.2x", delta="+0.3")

def main():
    # Page configuration
    st.set_page_config(layout="wide", page_title="NetSuite Dashboard")
    
    # Initialize session state for navigation
    if 'page' not in st.session_state:
        st.session_state.page = 'main'

    # Top navigation bar
    col1, col2, col3, col4 = st.columns([2, 6, 1, 1])
    with col1:
        st.image("https://via.placeholder.com/150x50", caption="")
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
        
        # Navigation Shortcut Group with state management
        st.markdown("### Navigation Shortcut Group")
        if st.button("Executive Management", key="exec_mgmt"):
            st.session_state.page = 'executive'
            st.experimental_rerun()
        if st.button("Sales", key="sales"):
            st.session_state.page = 'sales'
            st.experimental_rerun()
        if st.button("Customer Hierarchy", key="customer"):
            st.session_state.page = 'customer'
            st.experimental_rerun()
        if st.button("Inventory Management", key="inventory"):
            st.session_state.page = 'inventory'
            st.experimental_rerun()

    # Content area - conditionally render based on navigation state
    if st.session_state.page == 'executive':
        exec_management_view()
    elif st.session_state.page == 'sales':
        sales_view()
    elif st.session_state.page == 'customer':
        customer_hierarchy_view()
    elif st.session_state.page == 'inventory':
        inventory_management_view()
    else:
        # Default main dashboard view
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

        with right_col:
            st.markdown("### KPI Meter")
            st.plotly_chart(create_gauge_chart(), use_container_width=True)
            
            st.markdown("### Revenue by Period Trend")
            chart_data = pd.DataFrame({
                'Period': pd.date_range(start='2024-01-01', periods=6, freq='M'),
                'Revenue': [3.2, 3.4, 3.5, 3.7, 3.8, 3.9]
            })
            st.line_chart(chart_data.set_index('Period'))

if __name__ == "__main__":
    main()
