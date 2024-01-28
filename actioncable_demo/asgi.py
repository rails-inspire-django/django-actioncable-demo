"""
ASGI config for actioncable_demo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from actioncable import ActionCableConsumer, CableChannel, cable_channel_register

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'actioncable_demo.settings')

# Rails ActionCable uses the /cable path by default
# It can also work with your legacy code without conflict
urlpatterns = [
    path("cable", ActionCableConsumer.as_asgi()),
]

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(urlpatterns)
    }
)


# Use cable_channel_register to register your channels
@cable_channel_register
class ChatChannel(CableChannel):

    def __init__(self, consumer: ActionCableConsumer, identifier_key, params=None):
        self.params = params if params else {}
        self.identifier_key = identifier_key
        self.consumer = consumer
        self.group_name = None

    async def subscribe(self):
        self.group_name = f"chat_{self.params['pk']}"
        await self.consumer.subscribe_group(self.group_name, self)

    async def unsubscribe(self):
        await self.consumer.unsubscribe_group(self.group_name, self)
