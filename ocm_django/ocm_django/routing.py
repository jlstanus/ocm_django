from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import GPS.routing


application = ProtocolTypeRouter({
    			'websocket': AuthMiddlewareStack(
		            URLRouter(
		                GPS.routing.websocket_urlpatterns,
		            )
    			),
			})