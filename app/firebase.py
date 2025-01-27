
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("fastapi-firebase-managetask-firebase-adminsdk-fbsvc-b9e70b1008.json")
firebase_admin.initialize_app(cred)
