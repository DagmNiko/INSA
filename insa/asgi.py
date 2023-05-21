import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from dotenv import load_dotenv
project_folder = os.path.expanduser('~/insa')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "insa.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.

django_asgi_app = get_asgi_application()
# project_folder = os.path.expanduser('~/insa')  # adjust as appropriate


import core.routing
application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(core.routing.websocket_urlpatterns))
        ),
    }
)
