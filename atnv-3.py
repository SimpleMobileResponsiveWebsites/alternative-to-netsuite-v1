import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class DashboardData:
    def generate_activities_data(self):
        activities = pd.DataFrame({
            'Activity': ['Team Meeting', 'Project Launch', 'Deadline'],
            'Date': [datetime.now() - timedelta(days=i) for i in range(3)],
            'Status': ['Completed', 'Scheduled', 'Upcoming']
        })
        return {'activities': activities}

    def generate_billing_data(self):
        billing = pd.DataFrame({
            'Invoice ID': [f'INV-{i:04d}' for i in range(1, 6)],
            'Amount': np.random.uniform(1000, 5000, 5).round(2),
            'Due Date': [datetime.now() + timedelta(days=i * 5) for i in range(5)],
            'Status': ['Paid', 'Due', 'Overdue', 'Paid', 'Due']
        })
        return {'billing': billing}

    def generate_customers_data(self):
        customers = pd.DataFrame({
            'Customer Name': [f'Customer {i}' for i in range(1, 11)],
            'Email': [f'customer{i}@example.com' for i in range(1, 11)],
            'Total Spent': np.random.uniform(5000, 20000, 10).round(2),
            'Last Purchase': [datetime.now() - timedelta(days=i * 10) for i in range(10)]
        })
        return {'customers': customers}

    def generate_vendors_data(self):
        vendors = pd.DataFrame({
            'Vendor Name': [f'Vendor {i}' for i in range(1, 6)],
            'Contact': [f'contact{i}@vendor.com' for i in range(1, 6)],
            'Pending Orders': np.random.randint(1, 10, 5),
            'Last Order': [datetime.now() - timedelta(days=i * 7) for i in range(5)]
        })
        return {'vendors': vendors}

    def generate_payroll_data(self):
        payroll = pd.DataFrame({
            'Employee': [f'Employee {i}' for i in range(1, 6)],
            'Department': np.random.choice(['HR', 'Finance', 'IT', 'Sales'], 5),
            'Last Payroll Date': [datetime.now() - timedelta(days=i * 15) for i in range(5)],
            'Salary': np.random.uniform(4000, 8000, 5).round(2)
        })
        return {'payroll': payroll}

    def generate_financial_data(self):
        financial = pd.DataFrame({
            'Metric': ['Revenue', 'Expenses', 'Profit', 'Cash Flow'],
            'Amount': [120000, 80000, 40000, 30000],
            'Trend': ['Up', 'Down', 'Up', 'Flat']
        })
        return {'financial': financial}

    def generate_reports_data(self):
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
        }
        return {'reports': reports}

    def generate_analytics_data(self):
        dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
        kpis = {
            'Revenue Growth': {'current': '15.2%', 'delta': '2.3%'},
            'Customer Satisfaction': {'current': '4.5/5', 'delta': '0.2'},
        }
        metrics = {
            'Revenue': pd.DataFrame({'date': dates, 'value': np.random.uniform(800000, 1200000, len(dates))}),
            'Customer Count': pd.DataFrame({'date': dates, 'value': np.cumsum(np.random.randint(1, 10, len(dates)))}),
        }
        return {'kpis': kpis, 'available_metrics': list(metrics.keys()), 'metric_data': metrics}

    def generate_documents_data(self):
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

class DashboardApp:
    def __init__(self):
        self.data = DashboardData()

    def run(self):
        st.set_page_config(layout="wide", page_title="NetSuite Dashboard", page_icon="📊")

        # Sidebar Navigation
        st.sidebar.title("Navigation")
        pages = [
            "Activities",
            "Billing",
            "Customers",
            "Vendors",
            "Payroll and HR",
            "Financial",
            "Reports",
            "Analytics",
            "Documents",
            "Setup"
        ]
        selected_page = st.sidebar.radio("Go to", pages)

        # Render the selected page
        if selected_page == "Activities":
            self.render_activities_page()
        elif selected_page == "Billing":
            self.render_billing_page()
        elif selected_page == "Customers":
            self.render_customers_page()
        elif selected_page == "Vendors":
            self.render_vendors_page()
        elif selected_page == "Payroll and HR":
            self.render_payroll_page()
        elif selected_page == "Financial":
            self.render_financial_page()
        elif selected_page == "Reports":
            self.render_reports_page()
        elif selected_page == "Analytics":
            self.render_analytics_page()
        elif selected_page == "Documents":
            self.render_documents_page()
        elif selected_page == "Setup":
            self.render_setup_page()

    def render_activities_page(self):
        data = self.data.generate_activities_data()
        st.title("Activities Dashboard")
        st.write("Here you can track ongoing activities.")
        st.table(data['activities'])

    def render_billing_page(self):
        data = self.data.generate_billing_data()
        st.title("Billing Dashboard")
        st.write("Track billing cycles and invoices.")
        st.table(data['billing'])

    def render_customers_page(self):
        data = self.data.generate_customers_data()
        st.title("Customer Dashboard")
        st.write("View and manage customer data.")
        st.table(data['customers'])

    def render_vendors_page(self):
        data = self.data.generate_vendors_data()
        st.title("Vendor Dashboard")
        st.write("Monitor and manage vendor relationships.")
        st.table(data['vendors'])

    def render_payroll_page(self):
        data = self.data.generate_payroll_data()
        st.title("Payroll and HR Dashboard")
        st.write("Manage payroll processes and HR information.")
        st.table(data['payroll'])

    def render_financial_page(self):
        data = self.data.generate_financial_data()
        st.title("Financial Dashboard")
        st.write("Analyze financial data and trends.")
        st.table(data['financial'])

    def render_reports_page(self):
        data = self.data.generate_reports_data()
        st.title("Reports Dashboard")
        st.write("Access detailed reports.")
        st.table(data['reports']['Financial Reports'])
        st.table(data['reports']['Sales Reports'])

    def render_analytics_page(self):
        data = self.data.generate_analytics_data()
        st.title("Analytics Dashboard")
        st.subheader("Key Performance Indicators (KPIs)")
        for kpi, values in data['kpis'].items():
            st.metric(label=kpi, value=values['current'], delta=values['delta'])

        st.subheader("Metrics")
        selected_metric = st.selectbox("Select Metric", options=data['available_metrics'])
        metric_data = data['metric_data'][selected_metric]
        st.line_chart(metric_data.set_index('date')['value'])

    def render_documents_page(self):
        data = self.data.generate_documents_data()
        st.title("Documents Dashboard")
        st.write(f"Total Documents: {data['total_documents']}")
        st.write(f"Recent Uploads: {data['recent_uploads']}")
        st.write(f"Pending Review: {data['pending_review']}")
        st.dataframe(data['document_list'])

    def render_setup_page(self):
        st.title("Setup Dashboard")
        st.write("Configure application settings and preferences.")

if __name__ == "__main__":
    app = DashboardApp()
    app.run()
