# Email management
from flask_mail import Message
from pa_web import mail

# Send email
def send_email(subject, sender, to, text_body, html_body):
    """Send and email to one email address"""
    msg = Message(subject, sender=sender, recipients=[to])
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)
