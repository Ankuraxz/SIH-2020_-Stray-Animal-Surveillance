import os
import sys
import pyrebase
import requests
import time

config = {
    "apiKey": "AIzaSyDienGaKvTKGuSgKIFsU1pupYC1DABpeYk",
    "authDomain": "aghanya-test-py.firebaseapp.com",
    "databaseURL": "https://aghanya-test-py.firebaseio.com",
    "projectId": "aghanya-test-py",
    "storageBucket": "aghanya-test-py.appspot.com",
    "messagingSenderId": "356482709357",
    "appId": "1:356482709357:web:eeb1790474348ca3660c64",
    "measurementId": "G-MGVHBRZDTV"
}

# storage = firebase.storage()
firebase = pyrebase.initialize_app(config)
db = firebase.database()

while True: 
    email = str(input("Enter Email: "))
    password = str(input("Enter password:"))

    auth = firebase.auth()
    user = auth.create_user_with_email_and_password(email,password)
    print("User created successfully")

    print("\n Do you want to create more users?")
    a = str(input("Press Y for YES, press any other chracter for NO"))

    if a == "Y" or a == "y":
        continue
    else: 
        break


