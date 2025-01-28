from django.urls import path
from tasks.consumers import CtfConsumer

websocket_urlpatterns = [
    path('ws/ctf/<int:ctf_id>/', CtfConsumer.as_asgi()),
]