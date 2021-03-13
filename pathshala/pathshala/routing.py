from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chatapp.routing
from core import routing as core_routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            #chatapp.routing.websocket_urlpatterns,
            core_routing.websocket_urlpatterns,
        )
    ),
})