import os
import smtplib
from email.message import EmailMessage

email_id=os.environ.get('USER_ID')
email_pass=os.environ.get('USER_PASS')

msg=EmailMessage()

msg['Subject']='Grab dinner this wee'
msg['From']=email_id
msg['To']='bhavesh.goyal2018@vitstudent.ac.in'
msg.set_content('qwertyuibn')

with smtplib.SMTP_SSL('smtp.gmail.com',465)as smtp:
    smtp.login(email_id,email_pass)
    smtp.send_message(msg)
