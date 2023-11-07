import smtplib
import ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

with open('password.txt','r') as f:
    password = f.read()

with open('message.txt','r') as f:
    message = f.read()

with open('sender.txt','r') as f:
    email_sender = f.read()

with open('receiver.txt','r') as f:
    email_receiver = f.read()

msg = MIMEMultipart()

msg['From'] = 'bob'
msg['To'] = 'example@example.com'
msg['Subject'] = 'hello'
msg.attach(MIMEText(message,'plain'))

text = msg.as_string()

"""
filename = 'image.jpg'
attachment = open(filename,'rb')

p = MIMEBase('aplication','octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment; filename={filename}')
msg.attach(p)
"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_receiver, text)
