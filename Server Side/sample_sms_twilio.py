import os
import sys
#TWILIO api
import requests
import json
# https://www.youtube.com/watch?v=uzBRycRYsqw

from twilio.rest import Client #REST API

# Credentials for ankurvermaaxz@gmail.com
acc_sid = "AC53b30fe714a03aa740462bd9cb36fcf4"
auth_token = "cd9f89bbaec92d0d9e58777b642ff846"

client = Client(acc_sid,auth_token)
message = client.messages.create(
    body = "<>",
    to = '+919996492589',
    from_ ='+19892828077')
    
# # TwilioRestClient has been removed from this version of the library. Please refer to current documentation for guidance.
# https://www.twilio.com/docs/sms/quickstart/python-msg-svc 
# #install-python-and-the-twilio-helper-library
