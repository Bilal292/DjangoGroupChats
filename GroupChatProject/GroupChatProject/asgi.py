import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import groupchat.routing



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MScProject.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            groupchat.routing.websocket_urlpatterns
        )
    )
})
