import os
import base64
import time

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

def send_email(end_time, total_seconds):
    message = Mail(
        from_email='<FROM_EMAIL>',
        to_emails='<TO_EMAIL>',
        subject='Max has finished eating at ' + end_time.strftime("%d-%b-%Y %H:%M:%S"),
        html_content='It took him ' + total_seconds+ ' seconds')
    
    
    with open('/home/pi/Desktop/image.jpg', 'rb') as f:
        data  = f.read()
        f.close()
    encoded_file = base64.b64encode(data).decode()
       
    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName("filename.jpg"),
        FileType("image/jpg"),
        Disposition('attachment')
    )
    
    message.attachment = attachedFile
    
    try:
        sg = SendGridAPIClient('<API_KEY>')
        response = sg.send(message)
        print(response.status_code)
        print('Email Sent')
    except Exception as e:
        print(e)
