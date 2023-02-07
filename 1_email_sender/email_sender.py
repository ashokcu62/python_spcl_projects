# go over to our gmail account  and setup 2 factor authentication
# generate app password
# create a function to send the email
from email.message import EmailMessage
from app import PASSWORD

import ssl
import smtplib

email_sender = "liteyagami432@gmail.com"
email_password = PASSWORD

email_reciever = "fasifet755@fsouda.com"
subject = "python email function"
body = """
this is the message that i created with
 python  email api and the code makes 
 direct email send 
 have a nice day 
"""
# body="hiii its ashok"


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

#fn
def send():
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())


send()