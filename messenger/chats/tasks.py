from application.celery import app
from django.core.mail import send_mail

from application.settings import ADMINS, EMAIL_HOST_USER


@app.task
def send_admin_email():
    send_mail(
        subject="New chat cre",
        message="Hello fff",
        from_email=EMAIL_HOST_USER,
        recipient_list=ADMINS,
    )
