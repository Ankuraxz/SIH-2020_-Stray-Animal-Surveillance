import os 
import sys 
import smtplib 
from email.message import EmailMessage 
# https://www.tutorialspoint.com/python/python_sending_email.htm
# https://www.instructables.com/id/Send-Email-Using-Python/
#https://www.youtube.com/watch?v=JRCJ6RtE3xU

#TRANSMITTER
email_tx = "sihjune2020@gmail.com"
pass_tx = "Asdfgh1234@"
#reciever
email_rx = ["ankurvermaaxz@gmail.com","ruchikamodgil@gmail.com"]

msg = EmailMessage()
msg['Subject']= 'ANIMAL DETECTED!'
msg['From'] = email_tx
msg['To'] = email_rx
msg.set_content(" \n Tag: Cow \t Probability: 98.2")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_tx,pass_tx)

    smtp.send_message(msg)

