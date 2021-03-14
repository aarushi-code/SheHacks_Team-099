from core import consumers

from django.conf.urls import url,re_path

websocket_urlpatterns = [
    url(r'ws$', consumers.ChatConsumer),
]
