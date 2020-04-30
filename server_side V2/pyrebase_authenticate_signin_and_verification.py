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
#firebase object db
email = str(input("Enter Email: "))
password = str(input("Enter password:"))

auth = firebase.auth()
signin = auth.sign_in_with_email_and_password(email, password)
print("sign in successful")
# print("Your ID Token is \n",signin['idToken']) # id token for the email id

# SINGLE TIME USE
# verify = auth.send_email_verification(signin['idToken'])
# print("Verification link sent at :", email)

# FOR DELETING AN ACCOUT
# user_del = auth.delete_user_account(signin['idToken'])
# print("account deleted successfully")

data = {"tag": "COW"}
db.child("test_case_auth").push(data,signin["idToken"]) #only authentic user can put data
print("Done")