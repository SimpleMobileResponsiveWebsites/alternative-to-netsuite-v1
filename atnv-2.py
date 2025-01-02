import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta

# Generate sample data
def generate_financial_data():
    dates = pd.date_range(start='2024-01-01', periods=12, freq='M')
    return pd.DataFrame({
        'Date': dates,
        'Revenue': np.random.uniform(800000, 1200000, 12),
        'Expenses': np.random.uniform(600000, 900000, 12),
        'Profit': np.random.uniform(200000, 400000, 12),
        'Assets': np.random.uniform(2000000, 2500000, 12),
        'Liabilities': np.random.uniform(1000000, 1500000, 12),
        'Equity': np.random.uniform(500000, 1000000, 12)
    })

def create_balance_sheet_view():
    st.header("Balance Sheet")
    
    # Create sample balance sheet data
    assets = {
        'Current Assets': 1200000,
        'Fixed Assets': 800000,
        'Other Assets': 300000
    }
    
    liabilities = {
        'Current Liabilities': 600000,
        'Long-term Liabilities': 900000
    }
    
    equity = {
        'Common Stock': 400000,
        'Retained Earnings': 400000
    }
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Assets")
        for key, value in assets.items():
            st.metric(key, f"${value:,.2f}")
        st.metric("Total Assets", f"${sum(assets.values()):,.2f}")
        
    with col2:
        st.subheader("Liabilities & Equity")
        for key, value in liabilities.items():
            st.metric(key, f"${value:,.2f}")
        st.metric("Total Liabilities", f"${sum(liabilities.values()):,.2f}")
        st.divider()
        for key, value in equity.items():
            st.metric(key, f"${value:,.2f}")
        st.metric("Total Equity", f"${sum(equity.values()):,.2f}")

def create_trial_balance_view():
    st.header("Trial Balance")
    
    # Create sample trial balance data
    accounts = pd.DataFrame({
        'Account': ['Cash', 'Accounts Receivable', 'Inventory', 'Equipment', 
                   'Accounts Payable', 'Notes Payable', 'Common Stock', 'Revenue', 'Expenses'],
        'Debit': [50000, 30000, 45000, 75000, 0, 0, 0, 0, 35000],
        'Credit': [0, 0, 0, 0, 25000, 40000, 100000, 70000, 0]
    })
    
    st.dataframe(accounts, use_container_width=True)
    
    total_debits = accounts['Debit'].sum()
    total_credits = accounts['Credit'].sum()
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Debits", f"${total_debits:,.2f}")
    with col2:
        st.metric("Total Credits", f"${total_credits:,.2f}")

def create_income_statement_view():
    st.header("Income Statement")
    
    data = generate_financial_data()
    
    # Create monthly income statement
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=data['Date'],
        y=data['Revenue'],
        name='Revenue',
        marker_color='green'
    ))
    
    fig.add_trace(go.Bar(
        x=data['Date'],
        y=data['Expenses'],
        name='Expenses',
        marker_color='red'
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Profit'],
        name='Profit',
        line=dict(color='blue', width=2)
    ))
    
    fig.update_layout(
        title='Monthly Income Statement',
        barmode='group',
        xaxis_title='Month',
        yaxis_title='Amount ($)',
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)

def create_budget_vs_actual_view():
    st.header("Budget vs Actual")
    
    # Create sample budget vs actual data
    categories = ['Revenue', 'Operating Expenses', 'Marketing', 'R&D', 'Admin']
    budget = np.random.uniform(500000, 1000000, len(categories))
    actual = np.random.uniform(400000, 1100000, len(categories))
    variance = actual - budget
    variance_pct = (variance / budget) * 100
    
    data = pd.DataFrame({
        'Category': categories,
        'Budget': budget,
        'Actual': actual,
        'Variance': variance,
        'Variance %': variance_pct
    })
    
    # Create visualization
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Budget',
        x=categories,
        y=budget,
        marker_color='rgb(55, 83, 109)'
    ))
    
    fig.add_trace(go.Bar(
        name='Actual',
        x=categories,
        y=actual,
        marker_color='rgb(26, 118, 255)'
    ))
    
    fig.update_layout(
        title='Budget vs Actual Comparison',
        barmode='group',
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.dataframe(
        data.style.format({
            'Budget': '${:,.2f}',
            'Actual': '${:,.2f}',
            'Variance': '${:,.2f}',
            'Variance %': '{:.1f}%'
        }),
        use_container_width=True
    )

def main():
    st.set_page_config(layout="wide", page_title="NetSuite Dashboard", page_icon="📊")
    
    # Top navigation bar with tabs
    tab_names = ["Activities", "Billing", "Customers", "Vendors", "Payroll and HR", 
                 "Financial", "Reports", "Analytics", "Documents", "Setup"]
    tabs = st.tabs(tab_names)
    
    # Financial Tab Content
    with tabs[5]:  # Financial tab
        st.title("Financial Dashboard")
        
        # Create tiles as buttons in the first row
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("Balance Sheet", use_container_width=True):
                create_balance_sheet_view()
                
        with col2:
            if st.button("Trial Balance", use_container_width=True):
                create_trial_balance_view()
                
        with col3:
            if st.button("Income Statement", use_container_width=True):
                create_income_statement_view()
                
        with col4:
            if st.button("Budget vs Actual", use_container_width=True):
                create_budget_vs_actual_view()
        
        # Default view - show all
        st.divider()
        create_balance_sheet_view()
        st.divider()
        create_trial_balance_view()
        st.divider()
        create_income_statement_view()
        st.divider()
        create_budget_vs_actual_view()

if __name__ == "__main__":
    main()
