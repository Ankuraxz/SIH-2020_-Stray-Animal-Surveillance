import os
import sys
#sys.path.append('/Users/Dell/AppData/Local/Programs/Python/Python37/Lib/site-packages')
import pyrebase

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

img_path = "./img_test/image.jpg" #image of  currentframe

firebase = pyrebase.initialize_app(config)

# database for data, storage for storing
storage = firebase.storage()
db = firebase.database()

data = {
        "Tag" : "cow",
           "Probability" : "53.5"
    }

#storage.child(path_on_cloud).put(img_path)
result = db.child("/Camera_2_feed/").push(data) #provide tag
#print(result) #token unique to data
#print(type(result)) #dict
#print(result.get('name')) #extracting the token

path_on_cloud = "camera_2_feed/"+str(result.get('name'))+".jpg" #token+.jpg
storage.child(path_on_cloud).put(img_path)


