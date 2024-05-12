# """
# ASGI config for house_rental project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
# # """

# import os
# import chat.routing
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# # from channels.security.websocket import AllowedHostsOriginValidator
# # from conversation.routing import websocket_urlpatterns
# # from django.core.asgi import get_asgi_application
# from channels.auth import AuthMiddlewareStack
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'house_rental.settings')

# # application = get_asgi_application()

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     #"websocket": AllowedHostsOriginValidator(
#     #         URLRouter(
#     #             websocket_urlpatterns
#     #         )
#     #     ),
#      "websocket": AuthMiddlewareStack(
#               URLRouter(
#                   chat.routing.websocket_urlpatterns
#               )
#           ),
# })

import os

# 👇 1. Update the below import lib
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from paymnet.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'house_rental.settings')

# 👇 2. Update the application var
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
            URLRouter(
                websocket_urlpatterns
            )
        ),
})