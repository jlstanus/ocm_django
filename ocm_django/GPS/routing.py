from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from .consumers import GpsConsumer

websocket_urlpatterns = [
    url(r'^ws/gps/(?P<gps_name>[^/]+)/$', GpsConsumer),
]

