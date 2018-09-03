from channels.routing import ProtocolTypeRouter
from ocm_django.consumers import ws_message, ws_connect, ws_disconnect

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
})



channel_routing = {
    'websocket.connect': ws_connect,
    'websocket.receive': ws_message,
    'websocket.disconnect': ws_disconnect,
}