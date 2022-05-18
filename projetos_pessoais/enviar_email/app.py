import os
import smtplib
from email.message import EmailMessage
from segredos import senha


EMAIL_ADRESS = 'alexkurumin@gmail.com'
EMAIL_PASSWORD = senha



msg = EmailMessage()
msg['Subject'] = input('\nAssunto: ')
msg['From'] = 'alexkurumin@gmail.com'
msg['To'] = input('\nDestinatário: ')
msg.set_content(input('\nMensagem: '))

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
