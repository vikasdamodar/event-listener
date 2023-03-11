from django.urls import path

from .views import MandrillEventsConsumer

websocket_urlpatterns = [
    path('ws/data/', MandrillEventsConsumer.as_asgi()),
]
