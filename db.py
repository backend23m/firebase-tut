import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('/Users/djumanov/Desktop/smartphone-shop-db-firebase-adminsdk-80ld9-2553aafe36.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

users_ref = db.collection("users")

for doc in users_ref.stream():
    print(doc.to_dict())
    