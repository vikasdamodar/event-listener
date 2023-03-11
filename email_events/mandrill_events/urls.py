from django.urls import path


from .views import webhook, websocket_view

urlpatterns = [
    path('webhook/', webhook),
    path('ws/', websocket_view, name='websocket'),
]
