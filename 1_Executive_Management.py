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
