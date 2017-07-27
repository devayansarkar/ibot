"""importing modules required"""
import os
import requests

API_TOKEN = os.getenv('API_TOKEN')
QUERY_ENDPOINT = os.getenv('QUERY_ENDPOINT')

def parse_text(text, session):
    """To parse the text from in the servie and return proper response"""
    response_from_bot = []
    if text:
        headers = {"content-type": "application/json", "Authorization":"Bearer "+API_TOKEN}
        query_string = {"v":"20150910", "query":text, "lang":"en", "sessionId":session}
        data = requests.get(QUERY_ENDPOINT,headers=headers,params=query_string).json()
        response_from_bot = process_response(data)
    return response_from_bot

def process_response(data):
    """To parse the response received the api"""
    text = []
    if data['status']['code'] is 200:
        if data['result']['action'] and not data['result']['actionIncomplete']:
            text.append(data['result']['action'])
        for msg in data['result']['fulfillment']['messages']:
            text.append(msg['speech'])
    return text
    
