import pyrebase
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
firebase = pyrebase.initialize_app(config)

    # database for data, storage for storing
storage = firebase.storage()
db = firebase.database()


def distance(lon1,lat1,lon2,lat2):
    from math import radians, cos, sin, asin, sqrt
    #RED DOTS
    
    lon1 = radians(lon1) 
    lon2 = radians(lon2) 
    lat1 = radians(lat1) 
    lat2 = radians(lat2) 
    # Haversine formula  
    dlon = lon2 - lon1  
    dlat = lat2 - lat1 
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))  
    # Radius of earth in kilometers. Use 3956 for miles 
    r = 6371 
    # calculate the result 
    return(c * r) 
    



#STREAMING in "ANDROID" child
def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}
    # print(type(message["data"]))
    
    if type(message["data"])== dict:
        #OLD COMPLAINTS
        user = message["data"].keys()
        loc = message["data"].values()
        print(loc)
        print(user)
    elif type(message["data"])== str:
        #NEW ENTRY
        loc = str(message["data"])
        user = str(message["path"])
        i = loc.find(',')
        lat2 = float(loc[:i])
        # print(lat)
        lon2 =float(loc[i+1:])
        # print(lon)
        
        d=[]
        total_nodes = 6 
        nodes = {"red1" :[29.965470, 76.891908],
                    "red2" : [29.970303, 76.875890],
                    "red3" : [29.971725, 76.857072],
                    "red4" : [29.954427, 76.851762],
                    "red5" : [29.956509, 76.866385],
                    "red6" : [29.955431, 76.881695]}
        for ix in nodes.values():
            lat1 = ix[0]
            lon1 = ix[1]
            dist = distance(lon1,lat1,lon2,lat2)
            d.append(dist)

        print(min(d))
        print(d.index(min(d)))


my_stream = db.child("Android").stream(stream_handler)
time.sleep(5000)

