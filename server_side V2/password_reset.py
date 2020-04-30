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

auth = firebase.auth()


# PASSWORD RESET
pass_reset = auth.send_password_reset_email(email)
print("Password Reset Email Sent")