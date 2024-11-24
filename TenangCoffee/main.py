import streamlit as st
from components import (
    customer_order,
    inventory_management,
    sales_reporting,
    user_auth,
    feedback,
    payment,
    dashboard,
)

# Navigation
st.sidebar.title("Tenang Coffee Management System")
menu = st.sidebar.radio(
    "Navigate",
    [
        "Customer Order",
        "Inventory Management",
        "Sales Reporting",
        "User Authentication",
        "Feedback",
        "Payment",
        "Dashboard",
    ],
)

if menu == "Customer Order":
    customer_order.display()
elif menu == "Inventory Management":
    inventory_management.display()
elif menu == "Sales Reporting":
    sales_reporting.display()
elif menu == "User Authentication":
    user_auth.display()
elif menu == "Feedback":
    feedback.display()
elif menu == "Payment":
    payment.display()
elif menu == "Dashboard":
    dashboard.display()




