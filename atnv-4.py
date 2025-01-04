# app.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

# Configuration and Page Setup
st.set_page_config(page_title="NetSuite Dashboard Clone", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for styling
st.markdown("""
    <style>
    .main { padding-top: 0rem; }
    .block-container { padding-top: 1rem; }
    .stMetric {
        background-color: white;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Sample data for financial statements
balance_sheet_data = {
    'Assets': {
        'Current Assets': {
            'Cash and Cash Equivalents': 1500000,
            'Accounts Receivable': 2026663,
            'Inventory': 1297591,
            'Prepaid Expenses': 150000
        },
        'Non-Current Assets': {
            'Property, Plant & Equipment': 3500000,
            'Intangible Assets': 750000,
            'Long-term Investments': 1000000
        }
    },
    'Liabilities': {
        'Current Liabilities': {
            'Accounts Payable': 2026663,
            'Short-term Debt': 500000,
            'Accrued Expenses': 250000
        },
        'Non-Current Liabilities': {
            'Long-term Debt': 2000000,
            'Deferred Tax Liabilities': 300000
        }
    },
    'Equity': {
        "Shareholders' Equity": {
            'Common Stock': 1000000,
            'Retained Earnings': 4147591,
            'Additional Paid-in Capital': 500000
        }
    }
}

income_statement_data = pd.DataFrame({
    'Category': ['Revenue', 'Cost of Goods Sold', 'Gross Profit', 'Operating Expenses', 'Operating Income',
                'Other Income', 'Interest Expense', 'Income Before Tax', 'Income Tax', 'Net Income'],
    'Current Period': [3472235, 1440722, 2031513, 1835031, 196482, 
                      50000, 25000, 221482, 55371, 166111],
    'Previous Period': [3025079, 1042042, 1983037, 2286981, -303944,
                       45000, 27000, -285944, -71486, -214458],
    'YoY Change %': ['+14.8%', '+38.3%', '+2.4%', '-19.8%', '+164.6%',
                    '+11.1%', '-7.4%', '+177.5%', '+177.5%', '+177.5%']
})

budget_vs_actual_data = pd.DataFrame({
    'Category': ['Revenue', 'Expenses', 'Net Income'],
    'Actual': [3472235, 1835031, 166111],
    'Budget': [3300000, 1900000, 150000],
    'Variance': [172235, -64969, 16111],
    'Variance %': ['+5.2%', '-3.4%', '+10.7%']
})

# Sidebar
with st.sidebar:
    st.header("Reminders")
    st.info("📋 Expense Reports to Approve")
    st.info("📝 Purchase Request to Approve")
    st.warning("⚠️ Invoice > 30 Days > 50K")
    st.success("✓ New Customers")
    
    st.header("Navigation Shortcut Group")
    selected_page = st.radio(
        "Select Page",
        ["Dashboard", "Balance Sheet", "Trial Balance", "Income Statement", "Budget vs Actual"]
    )

# Function to display the main dashboard
def show_dashboard():
    st.title("Dashboard")
    
    # KPI Metrics Row
    col1, col2, col3, col4 = st.columns(4)
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

    # Revenue Trend Chart
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
    revenue_data = pd.DataFrame({
        'Date': dates,
        'Revenue': [3.2, 3.4, 3.7, 3.5, 3.8, 3.6, 3.9, 3.7, 3.8, 4.0, 3.9, 3.7],
    })
    
    st.subheader("Revenue by Period Trend")
    fig = px.line(revenue_data, x='Date', y='Revenue',
                  labels={'Revenue': 'Revenue (Millions $)', 'Date': 'Period'},
                  line_shape='spline')
    fig.update_layout(height=400, margin=dict(l=20, r=20, t=20, b=20))
    st.plotly_chart(fig, use_container_width=True)

def show_balance_sheet():
    st.title("Balance Sheet")
    
    # Convert balance sheet data to DataFrame for better display
    rows = []
    for category, subcategories in balance_sheet_data.items():
        for subcategory, items in subcategories.items():
            for item, amount in items.items():
                rows.append({
                    'Category': category,
                    'Subcategory': subcategory,
                    'Item': item,
                    'Amount': f"${amount:,.2f}"
                })
    
    df = pd.DataFrame(rows)
    
    # Display as an expandable tree
    for category in df['Category'].unique():
        st.subheader(category)
        category_data = df[df['Category'] == category]
        for subcategory in category_data['Subcategory'].unique():
            with st.expander(subcategory):
                subcategory_data = category_data[category_data['Subcategory'] == subcategory]
                st.dataframe(subcategory_data[['Item', 'Amount']], hide_index=True)

def show_income_statement():
    st.title("Income Statement")
    
    # Format currency values
    income_statement_data['Current Period'] = income_statement_data['Current Period'].apply(lambda x: f"${x:,.2f}")
    income_statement_data['Previous Period'] = income_statement_data['Previous Period'].apply(lambda x: f"${x:,.2f}")
    
    st.dataframe(income_statement_data, hide_index=True, use_container_width=True)
    
    # Add waterfall chart for current period
    current_period_values = [float(x.replace('$', '').replace(',', '')) for x in income_statement_data['Current Period']]
    fig = go.Figure(go.Waterfall(
        name="Income Statement",
        orientation="v",
        measure=["relative"] * len(income_statement_data),
        x=income_statement_data['Category'],
        y=current_period_values,
        connector={"line": {"color": "rgb(63, 63, 63)"}},
    ))
    fig.update_layout(title="Income Statement Waterfall Chart", height=500)
    st.plotly_chart(fig, use_container_width=True)

def show_budget_vs_actual():
    st.title("Budget vs Actual")
    
    # Format currency values
    for col in ['Actual', 'Budget', 'Variance']:
        budget_vs_actual_data[col] = budget_vs_actual_data[col].apply(lambda x: f"${x:,.2f}")
    
    st.dataframe(budget_vs_actual_data, hide_index=True, use_container_width=True)
    
    # Add bar chart comparison
    fig = go.Figure(data=[
        go.Bar(name='Actual', x=budget_vs_actual_data['Category'], 
               y=[float(x.replace('$', '').replace(',', '')) for x in budget_vs_actual_data['Actual']]),
        go.Bar(name='Budget', x=budget_vs_actual_data['Category'], 
               y=[float(x.replace('$', '').replace(',', '')) for x in budget_vs_actual_data['Budget']])
    ])
    fig.update_layout(barmode='group', title="Budget vs Actual Comparison")
    st.plotly_chart(fig, use_container_width=True)

def show_trial_balance():
    st.title("Trial Balance")
    
    # Create sample trial balance data
    trial_balance_data = pd.DataFrame({
        'Account': ['Cash', 'Accounts Receivable', 'Inventory', 'Accounts Payable', 
                   'Revenue', 'Expenses', 'Common Stock', 'Retained Earnings'],
        'Debit': ['$1,500,000', '$2,026,663', '$1,297,591', '', '', 
                  '$1,835,031', '', ''],
        'Credit': ['', '', '', '$2,026,663', '$3,472,235', '', 
                  '$1,000,000', '$160,387']
    })
    
    st.dataframe(trial_balance_data, hide_index=True, use_container_width=True)

# Display selected page
if selected_page == "Dashboard":
    show_dashboard()
elif selected_page == "Balance Sheet":
    show_balance_sheet()
elif selected_page == "Trial Balance":
    show_trial_balance()
elif selected_page == "Income Statement":
    show_income_statement()
elif selected_page == "Budget vs Actual":
    show_budget_vs_actual()
