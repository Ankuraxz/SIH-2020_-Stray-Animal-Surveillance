import os
import sys
# https://www.tutorialspoint.com/python/python_sending_email.htm
# https://www.instructables.com/id/Send-Email-Using-Python/
#https://www.youtube.com/watch?v=JRCJ6RtE3xU

import smtplib
#TRANSMITTER
email_tx = "sihjune2020@gmail.com"
pass_tx = "Asdfgh1234@"
#reciever
email_rx = ["ankurvermaaxz@gmail.com","ruchikamodgil@gmail.com"]

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email_tx,pass_tx)

    subject = "ANIMAL DETECTED"
    body =" \n ANIMAL DETECTED! \n Tag: Cow \t Prob: 98.12"

    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(email_tx, email_rx[1], msg)


