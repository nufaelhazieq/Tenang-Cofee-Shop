import streamlit as st
from firebase_initializer import db

def display():
    st.title("User Authentication")
    
    st.header("Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        admin_ref = db.collection("users").document(username).get()
        if admin_ref.exists and admin_ref.to_dict()["password"] == password:
            st.success("Login successful!")
        else:
            st.error("Invalid username or password.")
