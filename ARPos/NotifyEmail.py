import smtplib

server = 'smtp.gmail.com'
user = ''
password = ''

recipients = ['user@mail.com', 'other@mail.com']
sender = 'you@mail.com'
message = 'Hello World'

session = smtplib.SMTP(server)
# if your SMTP server doesn't need authentications,
# you don't need the following line:
session.login(user, password)
session.sendmail(sender, recipients, message)