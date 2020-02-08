"""
    filename : 
        db_interaction.py
    description : 
        Connects to the database and loads data in
    authors : 
        Dylan P. Jackson
"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./spottr-2507e-firebase-adminsdk-5pq8m-6f205660b7.json')
firebase_admin.initialize_app(cred)

#db = firestore.client()

