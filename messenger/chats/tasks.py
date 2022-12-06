from application.celery import app
from django.core.mail import send_mail

from application.settings import ADMINS, EMAIL_HOST_USER
import json
import requests


@app.task
def send_admin_email(user_id, username, chat_id, chat_title):
    send_mail(
        subject="New chat member",
        message=f"User {username}(id={user_id}) was added to chat {chat_title}(id={chat_id})",
        from_email=EMAIL_HOST_USER,
        recipient_list=ADMINS,
    )

@app.task
def create_chat_ws(data, channel="chat"):
    command = {
        "method": "publish",
        "params": {
            "channel": channel,
            "data": data
        }
    }
    api_key = '7f8b3e18-49ad-42a0-bc7f-2ed3f0a9af97'
    data = json.dumps(command)
    headers = {'Content-type': 'application/json',
               'Authorization': 'apikey ' + api_key}
    requests.post('http://localhost:9000/api', data=data, headers=headers)
