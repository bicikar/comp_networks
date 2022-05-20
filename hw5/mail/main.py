import smtplib
import ssl
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 465

context = ssl.create_default_context()


def message_cap(sender_email, dest_email):
    m = MIMEMultipart()
    m["Subject"] = "hw #5"
    m["From"] = sender_email
    m["To"] = dest_email

    with open('text') as text_file:
        text = text_file.read()
    with open('html') as html_file:
        html = html_file.read()

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    m.attach(part1)
    m.attach(part2)
    return m.as_string()


if __name__ == '__main__':
    sender_email = input('Enter your email: ')
    password = input('Enter the password: ')
    dest_email = sys.argv[1]
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        message = message_cap(sender_email, dest_email)
        server.sendmail(sender_email, dest_email, message)
        print('Message sent')