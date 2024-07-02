import smtplib

sender = "soulsalsal99@gmail.com"
receiver = "abdallahsalahsalem9@gmail.com"
password = "soulsal01150134573"
subject = "Python Email"
body = "Keep learning python dude!"
message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""
server = smtplib.SMTP("smtp.gmail.com", 587);
server.starttls()

try:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("unable to sign in")
