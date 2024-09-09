import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Andrei Baditoiu'
email['to'] = 'andrei.baditoiu@gmail.com'
email['subject'] = 'Salutari de la Andrei!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('a56317734@gmail.com', 'tdzm qqss scbz fguy')
    smtp.send_message(email)
    print('all good boss!')










# /////

# simple email sender

# email = EmailMessage()
# email['from'] = 'Andrei Baditoiu'
# email['to'] = 'andrei.baditoiu@gmail.com'
# email['subject'] = 'Salutari de la Andrei!'
#
# email.set_content('Mesaj de test din Python')
#
# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login('a56317734@gmail.com', 'tdzm qqss scbz fguy')
#     smtp.send_message(email)
#     print('all good boss!')
