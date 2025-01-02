import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

class DashboardData:
    def generate_activities_data(self):
        return pd.DataFrame({'Activity': ['Task 1', 'Task 2'], 'Status': ['Completed', 'In Progress']})
    
    def generate_billing_data(self):
        return pd.DataFrame({'Invoice': ['INV001', 'INV002'], 'Amount': [1000, 1500]})
    
    def generate_customers_data(self):
        return pd.DataFrame({'Customer Name': ['Alice', 'Bob'], 'Purchase Amount': [200, 300]})
    
    def generate_vendors_data(self):
        return pd.DataFrame({'Vendor Name': ['Vendor A', 'Vendor B'], 'Order Count': [5, 7]})
    
    def generate_payroll_data(self):
        return pd.DataFrame({'Employee': ['John', 'Sarah'], 'Salary': [50000, 60000]})
    
    def generate_financial_data(self):
        return pd.DataFrame({'Metric': ['Revenue', 'Expenses'], 'Value': [120000, 90000]})

class DashboardLayouts:
    def render_activities_tab(self, data):
        st.title("Activities Overview")
        st.dataframe(data)

    def render_billing_tab(self, data):
        st.title("Billing Overview")
        st.dataframe(data)

    def render_customers_tab(self, data):
        st.title("Customers Overview")
        st.dataframe(data)

    def render_vendors_tab(self, data):
        st.title("Vendors Overview")
        st.dataframe(data)

    def render_payroll_tab(self, data):
        st.title("Payroll Overview")
        st.dataframe(data)

    def render_financial_tab(self, data):
        st.title("Financial Overview")
        st.dataframe(data)

    def render_reports_tab(self, data):
        st.title("Reports Overview")
        for category, df in data['reports'].items():
            st.subheader(category)
            st.dataframe(df)

    def render_analytics_tab(self, data):
        st.title("Analytics Overview")
        st.subheader("Key Performance Indicators (KPIs)")
        for kpi, values in data['kpis'].items():
            st.metric(label=kpi, value=values['current'], delta=values['delta'])
        
        st.subheader("Metrics")
        selected_metric = st.selectbox("Select Metric", options=data['available_metrics'])
        st.line_chart(data['metric_data'][selected_metric])

    def render_documents_tab(self, data):
        st.title("Documents Overview")
        st.metric("Total Documents", data['total_documents'])
        st.metric("Recent Uploads", data['recent_uploads'])
        st.metric("Pending Review", data['pending_review'])
        st.dataframe(data['document_list'])

    def render_setup_tab(self):
        st.title("Setup and Configuration")
        st.write("Configure your dashboard settings here.")

class DashboardApp:
    def __init__(self):
        self.data = DashboardData()
        self.layouts = DashboardLayouts()
        
    def run(self):
        st.set_page_config(layout="wide", page_title="NetSuite Dashboard", page_icon="📊")
        
        # Create sidebar for global filters
        self.create_sidebar()
        
        # Create main navigation
        tab_names = ["Activities", "Billing", "Customers", "Vendors", 
                     "Payroll and HR", "Financial", "Reports", "Analytics", 
                     "Documents", "Setup"]
        tabs = st.tabs(tab_names)
        
        # Render each tab with its corresponding data and layout
        with tabs[0]:  # Activities
            self.layouts.render_activities_tab(self.data.generate_activities_data())
            
        with tabs[1]:  # Billing
            self.layouts.render_billing_tab(self.data.generate_billing_data())
            
        with tabs[2]:  # Customers
            self.layouts.render_customers_tab(self.data.generate_customers_data())
            
        with tabs[3]:  # Vendors
            self.layouts.render_vendors_tab(self.data.generate_vendors_data())
            
        with tabs[4]:  # Payroll and HR
            self.layouts.render_payroll_tab(self.data.generate_payroll_data())
            
        with tabs[5]:  # Financial
            self.layouts.render_financial_tab(self.data.generate_financial_data())
            
        with tabs[6]:  # Reports
            self.layouts.render_reports_tab(self.generate_reports_data())
            
        with tabs[7]:  # Analytics
            self.layouts.render_analytics_tab(self.generate_analytics_data())
            
        with tabs[8]:  # Documents
            self.layouts.render_documents_tab(self.generate_documents_data())
            
        with tabs[9]:  # Setup
            self.layouts.render_setup_tab()

    def create_sidebar(self):
        with st.sidebar:
            st.title("Filters")
            
            # Date Range Filter
            st.date_input(
                "Date Range",
                value=(datetime.now() - timedelta(days=30), datetime.now())
            )
            
            # Company Filter
            st.selectbox(
                "Company",
                options=["All"] + [f"Company {i}" for i in range(1, 6)]
            )
            
            # Department Filter
            st.multiselect(
                "Department",
                options=["Sales", "Marketing", "Finance", "Operations", "IT"]
            )
            
            # Refresh Button
            if st.button("Refresh Data"):
                st.rerun()

    def generate_reports_data(self):
        # Generate sample reports data
        reports = {
            'Financial Reports': pd.DataFrame({
                'Report Name': ['Balance Sheet', 'Income Statement', 'Cash Flow', 'Trial Balance'],
                'Last Run': pd.date_range(end=datetime.now(), periods=4),
                'Status': ['Completed', 'Completed', 'In Progress', 'Scheduled']
            }),
            'Sales Reports': pd.DataFrame({
                'Report Name': ['Sales by Region', 'Product Performance', 'Customer Analysis'],
                'Last Run': pd.date_range(end=datetime.now(), periods=3),
                'Status': ['Completed', 'Completed', 'Completed']
            }),
            'Inventory Reports': pd.DataFrame({
                'Report Name': ['Stock Level', 'Reorder Points', 'Inventory Valuation'],
                'Last Run': pd.date_range(end=datetime.now(), periods=3),
                'Status': ['Completed', 'In Progress', 'Completed']
            }),
            'Custom Reports': pd.DataFrame({
                'Report Name': ['Custom Report 1', 'Custom Report 2'],
                'Last Run': pd.date_range(end=datetime.now(), periods=2),
                'Status': ['Completed', 'Draft']
            })
        }
        return {'reports': reports}

    def generate_analytics_data(self):
        # Generate sample analytics data
        dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
        
        kpis = {
            'Revenue Growth': {
                'current': '15.2%',
                'delta': '2.3%'
            },
            'Customer Satisfaction': {
                'current': '4.5/5',
                'delta': '0.2'
            },
            'Operating Margin': {
                'current': '28.5%',
                'delta': '-1.2%'
            },
            'Employee Retention': {
                'current': '94.5%',
                'delta': '1.5%'
            }
        }
        
        metrics = {
            'Revenue': pd.DataFrame({
                'date': dates,
                'value': np.random.uniform(800000, 1200000, len(dates))
            }),
            'Customer Count': pd.DataFrame({
                'date': dates,
                'value': np.cumsum(np.random.randint(1, 10, len(dates)))
            }),
            'Average Order Value': pd.DataFrame({
                'date': dates,
                'value': np.random.uniform(100, 500, len(dates))
            })
        }
        
        return {
            'kpis': kpis,
            'available_metrics': list(metrics.keys()),
            'metric_data': metrics
        }

    def generate_documents_data(self):
        # Generate sample documents data
        num_docs = 100
        documents = pd.DataFrame({
            'Document Name': [f'Document {i}' for i in range(num_docs)],
            'Type': np.random.choice(['Invoice', 'Contract', 'Report', 'Policy'], num_docs),
            'Created Date': pd.date_range(end=datetime.now(), periods=num_docs),
            'Status': np.random.choice(['Draft', 'Under Review', 'Approved'], num_docs),
            'Owner': np.random.choice(['John D.', 'Sarah M.', 'Mike R.'], num_docs)
        })
        
        return {
            'total_documents': len(documents),
            'recent_uploads': len(documents[documents['Created Date'].dt.date == datetime.now().date()]),
            'pending_review': len(documents[documents['Status'] == 'Under Review']),
            'document_list': documents
        }

if __name__ == "__main__":
    app = DashboardApp()
    app.run()
