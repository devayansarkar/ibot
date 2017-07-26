"""importing modules requried"""
from django.conf.urls import  url
from .views import BotController
urlpatterns = [
                  url(r'^webhook/?$', BotController.as_view()) 
]