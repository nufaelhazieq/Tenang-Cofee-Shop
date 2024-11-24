import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate(r"C:\Users\Nufael Hazieq\OneDrive - Universiti Teknologi PETRONAS\Documents\Data Visualization\TenangCoffee\firebase_config.json")
    firebase_admin.initialize_app(cred)

# Firestore database instance
db = firestore.client()
