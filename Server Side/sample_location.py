import requests
import os
import sys 
#https://www.youtube.com/watch?v=OlSQ2TEP3oc


res = requests.get("https://ipinfo.io/")
print(res.text)
print(type(res.text))