# Writing data to /Aghanya/wRp5oAmLakVa8csn5uNm/1234/uBVMNldU3bohO1xSSaLi

from firebase import firebase
import time
import os
import sys


#refer : https://youtu.be/jcUVCtVbuc
dbconn = firebase.FirebaseApplication("https://aghanya-test-py.firebaseio.com/", None)
# Install these Initially
# pip install python-jwt
# pip install gcloud
# pip install firebase-admin
# pip install sseclient
# pip install pycrypto
# pip install pycryptodome
# pip install firebase
while True:
    tags = "Cow"
    prob ="98.128"
    
    data_to_upload = {
        "Tag" : (tags),
        "Probability" : (prob)

    }
    result = dbconn.post("/Camera1_feed/", data_to_upload)

    print(result)
