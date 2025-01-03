import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

def create_gauge_chart():
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=3.7,
        title={'text': "Revenue"},
        number={'prefix': "$", 'suffix': "M"},
        gauge={
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
    st.header("Key Financial Metrics")
    st.metric(label="Total Revenue", value="$15.2M", delta="+12%")
    st.metric(label="Gross Margin", value="68%", delta="+3%")
    st.metric(label="Operating Expenses", value="$8.1M", delta="-5%")
    st.metric(label="Cash Position", value="$5.4M", delta="+8%")

def sales_view():
    st.title("Sales Dashboard")
    st.header("Sales Performance")
    st.metric(label="Total Sales", value="$5.2M", delta="+15%")
    st.metric(label="New Customers", value="127", delta="+23")
    st.metric(label="Pipeline Value", value="$8.7M", delta="+7%")
    st.metric(label="Win Rate", value="62%", delta="+5%")

def customer_hierarchy_view():
    st.title("Customer Hierarchy")
    st.text_input("Search Customers", placeholder="Enter customer name or ID")
    st.button("Search")
    st.subheader("Customer List")
    customers = pd.DataFrame({
        "Customer Name": ["Acme Corp", "Beta Ltd", "Gamma Inc"],
        "ID": [101, 102, 103]
    })
    st.table(customers)

def inventory_management_view():
    st.title("Inventory Management")
    st.header("Inventory Metrics")
    st.metric(label="Total SKUs", value="1,234", delta="+12")
    st.metric(label="Stock Value", value="$2.1M", delta="+5%")
    st.metric(label="Low Stock Items", value="23", delta="-3")
    st.metric(label="Turnover Rate", value="4.2x", delta="+0.3")

def main():
    # Page configuration
    st.set_page_config(layout="wide", page_title="Simplified Dashboard")

    # Navigation
    pages = {
        "Executive Management": exec_management_view,
        "Sales": sales_view,
        "Customer Hierarchy": customer_hierarchy_view,
        "Inventory Management": inventory_management_view
    }

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    # Render the selected page
    pages[selection]()

if __name__ == "__main__":
    main()
