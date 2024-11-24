# components/feedback.py

import streamlit as st

# Function to display the feedback form
def display():
    st.title("Customer Feedback")

    # Input fields for rating the coffee and service
    coffee_rating = st.slider("Rate the coffee", 1, 5)
    service_rating = st.slider("Rate the service", 1, 5)

    # Additional comments section
    comments = st.text_area("Any additional comments?")

    if st.button("Submit Feedback"):
        # Logic to store feedback (this could be saving it to a database)
        st.success("Thank you for your feedback!")

        # Example of storing feedback in a dictionary (this should be saved to a database)
        feedback_data = {
            "coffee_rating": coffee_rating,
            "service_rating": service_rating,
            "comments": comments
        }

        # For now, just display the feedback as an example
        st.write("Feedback submitted:", feedback_data)


