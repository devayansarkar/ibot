"""import json to form the request body ,requests to send request to endpoint
    and os to get env details"""
import json
import os
import requests


PAGE_ACCESS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN')
ENDPOINT_URL = 'https://graph.facebook.com/v2.10/me/messages?access_token=%s'

# Send simple message to enduser
def send_text_message(fbid, text):
    """Sends messages to Facebook"""
    post_message_url = ENDPOINT_URL%PAGE_ACCESS_TOKEN
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":text}})
    resp=requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
    print(resp.content)
