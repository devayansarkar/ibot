from django.conf.urls import url, include

urlpatterns = [
    url(r'^facebook/', include('ibot.urls')),
]
