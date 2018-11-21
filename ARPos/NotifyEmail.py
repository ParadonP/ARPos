import smtplib

server = 'smtp.gmail.com', 587
user = ''
password = ''

recipients = ['paradonp@outlook.com', 'tempa_d4@hotmail.com']
sender = 'ppanjaroen@gmail.com'
message = '''Hello World Don
what are you doing'''

session = smtplib.SMTP(server)

session.login(user, password)
session.sendmail(sender, recipients, message)