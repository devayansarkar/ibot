"""import all the modules required for the controller"""
import json
import os
from ibot.services import facebook
from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils.datastructures import MultiValueDictKeyError

VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')

class BotController(generic.View):
    """Controlles and analyzes the request recieved from Facebook"""
    def get(self, *args, **kwargs):
        """Authenticates Facebook webhook"""
        try:
            if self.request.GET['hub.verify_token'] == 'abc':
                return HttpResponse(self.request.GET['hub.challenge'])
            else:
                res = HttpResponse('Error, invalid token')
                res.status_code = 403
                return res
        except MultiValueDictKeyError:
            print('Required params not received while webhook auth')
            res = HttpResponse('Bad request')
            res.status_code = 400
            return res

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)
    def post(self, *args, **kwargs):
        """Receives all messages sent to the webhook"""
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    facebook.send_text_message(message['sender']['id'], message['message']['text'])    
        return HttpResponse() 