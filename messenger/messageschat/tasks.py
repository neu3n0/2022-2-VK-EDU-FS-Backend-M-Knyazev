from application.celery import app
import json
import requests

@app.task
def create_mess_ws(data, channel="messages"):
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
