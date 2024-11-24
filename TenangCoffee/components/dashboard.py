# components/dashboard.py
import streamlit as st

def display():
    # Dashboard Title
    st.title("Coffee Shop Dashboard")

    # Real-Time Monitoring Section
    st.header("Real-Time Monitoring")
    st.subheader("Current Orders")
    st.write("List of current orders will go here.")
    # You can simulate data here or connect to a database
    st.write("Order 1: Americano - Preparing")
    st.write("Order 2: Latte - Waiting")

    st.subheader("Inventory Levels")
    st.write("Current inventory levels for key items:")
    # Again, this could be dynamically pulled from a database
    st.write("Coffee Beans: 50kg")
    st.write("Milk: 20 liters")
    st.write("Cups: 1000")

    # Inventory Health Check Section
    st.header("Inventory Health Check")
    st.write("Items running low and need to be restocked:")
    st.write("- Coffee Beans: 20% remaining")
    st.write("- Milk: 10% remaining")

    # Add logic to show items based on real-time stock levels
    st.write("Items that are in good stock:")
    st.write("- Sugar: 80% remaining")
    st.write("- Cups: 90% remaining")


