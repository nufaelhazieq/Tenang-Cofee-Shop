import streamlit as st
from firebase_initializer import db
import uuid
import datetime

def display():
    st.title("Customer Order")
    
    # Menu
    menu = {
        "Americano": 10,
        "Cappuccino": 12,
        "Latte": 14,
        "Caramel Macchiato": 15,
    }

    st.header("Menu")
    for item, price in menu.items():
        st.write(f"{item}: RM {price}")

    # Order placement
    st.header("Place Your Order")
    coffee = st.selectbox("Select Coffee", list(menu.keys()))
    size = st.radio("Select Size", ["Small", "Medium", "Large"])
    add_ons = st.multiselect("Add-ons", ["Extra Sugar", "Milk"])
    if st.button("Confirm Order"):
        booking_id = str(uuid.uuid4())
        prep_time = datetime.datetime.now() + datetime.timedelta(minutes=10)
        
        db.collection("orders").add({
            "coffee": coffee,
            "size": size,
            "add_ons": add_ons,
            "booking_id": booking_id,
            "prep_time": prep_time.strftime("%Y-%m-%d %H:%M:%S"),
        })
        
        st.success(f"Order Confirmed! Booking ID: {booking_id}")
        st.info(f"Estimated preparation time: {prep_time.strftime('%H:%M:%S')}")
