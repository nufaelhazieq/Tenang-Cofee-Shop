import streamlit as st
from google.cloud import firestore
import datetime

# Firebase Initialization
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r"C:\Users\Nufael Hazieq\OneDrive - Universiti Teknologi PETRONAS\Documents\Data Visualization\TenangCoffee\firebase_config.json")
try:
    firebase_admin.initialize_app(cred)
except ValueError:
    pass  # Firebase already initialized

db = firestore.client()

# Functions to fetch data and generate reports
# (Code remains the same as provided earlier)

# Main function renamed to 'display'
def display():
    st.title("Sales Reporting Dashboard")
    
# Functions to fetch data
def fetch_sales_data(start_date, end_date):
    """Fetch sales data between the specified dates from Firestore."""
    sales_ref = db.collection("sales")
    query = sales_ref.where("date", ">=", start_date).where("date", "<=", end_date)
    docs = query.stream()
    sales_data = [doc.to_dict() for doc in docs]
    return sales_data

def generate_reports(sales_data):
    """Generate sales reports."""
    total_revenue = 0
    total_quantity = 0
    coffee_type_count = {}
    profit = 0

    for sale in sales_data:
        coffee_type = sale["coffee_type"]
        revenue = sale["price"] * sale["quantity"]
        cost = sale["cost"] * sale["quantity"]

        # Update totals
        total_revenue += revenue
        total_quantity += sale["quantity"]
        profit += (revenue - cost)

        # Update coffee type count
        if coffee_type not in coffee_type_count:
            coffee_type_count[coffee_type] = 0
        coffee_type_count[coffee_type] += sale["quantity"]

    # Find best and worst sellers
    best_seller = max(coffee_type_count, key=coffee_type_count.get) if coffee_type_count else None
    worst_seller = min(coffee_type_count, key=coffee_type_count.get) if coffee_type_count else None

    # Format reports
    report = {
        "total_revenue": total_revenue,
        "total_quantity": total_quantity,
        "profit": profit,
        "coffee_type_count": coffee_type_count,
        "best_seller": best_seller,
        "worst_seller": worst_seller,
    }
    return report

# Streamlit UI
def display():
    st.title("Sales Reporting Dashboard")

    # Date Range Selection
    st.sidebar.header("Filter Sales Data")
    start_date = st.sidebar.date_input("Start Date", datetime.date.today() - datetime.timedelta(days=7))
    end_date = st.sidebar.date_input("End Date", datetime.date.today())

    if st.sidebar.button("Generate Report"):
        # Fetch data
        sales_data = fetch_sales_data(start_date, end_date)
        if not sales_data:
            st.warning("No sales data found for the selected date range.")
            return

        # Generate Reports
        report = generate_reports(sales_data)

        # Display Reports
        st.subheader("Sales Report")
        st.write(f"**Total Revenue:** ${report['total_revenue']:.2f}")
        st.write(f"**Total Quantity Sold:** {report['total_quantity']}")
        st.write(f"**Profit:** ${report['profit']:.2f}")
        
        st.subheader("Sales Breakdown by Coffee Type")
        for coffee_type, quantity in report["coffee_type_count"].items():
            st.write(f"- {coffee_type}: {quantity} cups sold")

        st.subheader("Best and Worst Sellers")
        st.write(f"**Best Seller:** {report['best_seller']}" if report["best_seller"] else "No sales data.")
        st.write(f"**Worst Seller:** {report['worst_seller']}" if report["worst_seller"] else "No sales data.")

        # Visualize data
        st.subheader("Sales Breakdown (Bar Chart)")
        st.bar_chart(report["coffee_type_count"])

if __name__ == "__main__":
    display()


