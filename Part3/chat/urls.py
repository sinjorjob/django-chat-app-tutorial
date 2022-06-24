from django.urls import path
from chat.views import *

app_name = 'chat'

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('chat_room/', ChatRoom.as_view(), name="chat_room"),
    path("search/", SearchUser.as_view(), name="search_user"),
    path("addfriend/<str:username>", addFriend, name="addfriend"), 
    path("chat/<str:username>", get_message, name="get_message"), 
    path('api/messages', UpdateMessage.as_view()),
    path('api/messages/<int:sender>/<int:receiver>', UpdateMessage.as_view()),
]