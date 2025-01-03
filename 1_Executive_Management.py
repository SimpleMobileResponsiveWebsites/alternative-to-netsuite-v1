import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def exec_management_page():
    st.title("Executive Management Dashboard")
    
    # Key Metrics Overview
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total Revenue", value="$15.2M", delta="+12%")
    with col2:
        st.metric(label="Gross Margin", value="68%", delta="+3%")
    with col3:
        st.metric(label="Operating Expenses", value="$8.1M", delta="-5%")
    with col4:
        st.metric(label="Cash Position", value="$5.4M", delta="+8%")
    
    # Financial Summary
    st.subheader("Financial Summary")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Revenue trend
        chart_data = pd.DataFrame({
            'Month': pd.date_range(start='2024-01-01', periods=12, freq='M'),
            'Revenue': [12.1, 12.3, 12.8, 13.2, 13.5, 13.8, 14.1, 14.3, 14.6, 14.9, 15.1, 15.2],
            'Target': [12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5]
        })
        fig = px.line(chart_data, x='Month', y=['Revenue', 'Target'], title='Revenue vs Target')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### Quick Actions")
        st.button("View Financial Reports")
        st.button("Schedule Board Meeting")
        st.button("Review Strategic Goals")
    
    # Risk Management
    st.subheader("Risk Management Overview")
    risks = pd.DataFrame({
        'Risk Category': ['Operational', 'Financial', 'Strategic', 'Compliance'],
        'Risk Level': [7, 4, 5, 3],
        'Status': ['High', 'Low', 'Medium', 'Low']
    })
    st.dataframe(risks, use_container_width=True)

if __name__ == "__main__":
    exec_management_page()
