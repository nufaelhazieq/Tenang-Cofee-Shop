# components/payment.py
import streamlit as st

def display():
    st.title("Secure Payment")
    
    # You can simulate a payment form
    st.write("Please enter your payment details below:")

    # Payment details fields
    credit_card_number = st.text_input("Credit Card Number")
    expiry_date = st.text_input("Expiry Date")
    cvv = st.text_input("CVV", type="password")
    
    # Example payment button (you can integrate with actual payment gateway here)
    if st.button("Pay Now"):
        # In reality, you would send the payment information to your payment gateway
        st.success("Payment successful! Thank you for your purchase.")
        
        # Optionally, generate an order invoice or receipt
        st.write("Invoice generated:")
        st.write(f"Credit Card Number: {credit_card_number[:4]} **** **** ****")
        st.write(f"Expiry Date: {expiry_date}")
        st.write(f"Total Amount: $20.00")  # Example amount

