from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^facebook/', include('ibot.urls')),
]
