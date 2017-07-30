"""import json to form the request body ,requests to send request to endpoint
    and os to get env details"""
import json
import os
import requests


PAGE_ACCESS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN','EAAGr0cSz46oBAKT8IHft4rsAjt3mIJG43AlybsK5w0egq6iCl1e8wa2pnLTsrgkJJNhFwtbB5zZClrMen5UIv4ogYKlmvzSotDVXUVsAYV2ruCcAXM1BGiZCTlZCU9wWGWX70iJMcfvJTqRPhAO2xMbyoPgGLZBO8eUeY8JztAZDZD')
ENDPOINT_URL = 'https://graph.facebook.com/v2.10/me/messages?access_token=%s'


def send_text_message(fbid, text):
    """Create a simple text message to be sent to the end user"""
    payload = json.dumps({"recipient":{"id":fbid}, "message":{"text":text}})
    send_message(payload)

def send_message(payload):
    """Send message to be sent to the end user"""
    post_message_url = ENDPOINT_URL%PAGE_ACCESS_TOKEN
    requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=payload)
