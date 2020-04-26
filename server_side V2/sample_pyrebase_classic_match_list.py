# https://firebase.google.com/docs/functions/database-events  : References
# https://github.com/thisbejim/Pyrebase
import os
import sys
#sys.path.append('/Users/Dell/AppData/Local/Programs/Python/Python37/Lib/site-packages')
import pyrebase
import collections
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

# Initialization
cam_info =[]
cam_location=[] # can be a dictionary
# storage = firebase.storage()
firebase = pyrebase.initialize_app(config)
db = firebase.database()

#firebase object db

cams = db.child("Cam_info").get()
#cam_dict = cams.val()
#print(cam_dict)
#print(type(cam_dict))

for keys ,values in (cams.val()).items():
    #print(keys)
    cam_info.append(keys) #camera number
    cam_location.append(values) # camera location

cam_info.sort() # cam_info initialised
print("initial cam info:", cam_info)



while True :
    cam__ =[]
    cam_loc__ =[]
    db_ = firebase.database()

#firebase object db

    cams_ = db_.child("Cam_info").get()
    for keys_ ,values_ in (cams_.val()).items():
    #print(keys)
        cam__.append(keys_) #camera number
        cam_loc__.append(values_) # camera location

    cam__.sort()

    if cam__ != cam_info : # some changes made
        print(" changed cam_ info")
        cam_info = cam__
        cam_location =cam_loc__
        print(" New cam info :", cam_info)

    else:
        print("no changes")
    
    time.sleep(10) # check for change, every 10 sec
    





