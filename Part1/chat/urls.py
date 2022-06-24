from django.urls import path
from chat.views import *

app_name = 'chat'

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('chat_room/', ChatRoom.as_view(), name="chat_room"),
]