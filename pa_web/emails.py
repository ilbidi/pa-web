# Email management
from flask import current_app, render_template
from flask_mail import Message
from pa_web import mail
from threading import Thread

# Send email
def send_email(subject, sender, to, text_body, html_body):
    """Send a syncronous email to one email address"""
    msg = Message(subject, sender=sender, recipients=[to])
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

# Send asyncronous email
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

# Send email
def send_email_template(to, subject, template, **kwargs):
    """Send and email to one email address with a specific template
    template is provided as name, the function assumes that  file .txt and .html
    with the same name exists."""
    app = current_app._get_current_object()
    subject_prefix = app.config['PAWEB_SUBJECT_PREFIX']
    sender = app.config['PAWEB_MAIL_SENDER']
    msg = Message(subject_prefix + subject, sender=sender, recipients=[to])
    msg.body = render_template(template+'.txt', **kwargs)
    msg.html = render_template(template+'.html', **kwargs)
    thr = Thread(target = send_async_email, args=[app, msg] )
    thr.start()
    return thr
