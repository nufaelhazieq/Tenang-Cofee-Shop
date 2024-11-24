import streamlit as st
from firebase_initializer import db

def display():
    st.title("Inventory Management")
    
    # Display inventory
    inventory_ref = db.collection("inventory").stream()
    inventory = {item.id: item.to_dict() for item in inventory_ref}

    st.header("Current Inventory")
    for item, details in inventory.items():
        st.write(f"{item}: {details['quantity']} units")

    # Restock items
    st.header("Restock Items")
    item_name = st.text_input("Item Name")
    quantity = st.number_input("Quantity", min_value=0, step=1)
    if st.button("Restock"):
        db.collection("inventory").document(item_name).set(
            {"quantity": quantity}, merge=True
        )
        st.success(f"Restocked {item_name} with {quantity} units.")
