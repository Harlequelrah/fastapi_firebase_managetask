
import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate("FASTAPI\\fastapi_firebase_managetask\\fastapi-firebase-managetask-firebase-adminsdk-fbsvc-b9e70b1008.json")
firebase_admin.initialize_app(cred)
db=firestore.client()
