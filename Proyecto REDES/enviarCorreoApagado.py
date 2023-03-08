# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='bmbstore.2022@gmail.com',
    to_emails='1180045@usap.edu',
    subject='Se Desactivó el Riego',
    html_content='Riego Desactivado')
try:
    f = open ('/proyecto/SENDGRID_API_KEY.txt','r')
    apiKey=f.read()
    sg = SendGridAPIClient(str(apiKey).strip())
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
