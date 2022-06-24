from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    #Home画面を表示するビュー
    template_name = 'home.html'
    
    
class ChatRoom(TemplateView):
    #Home画面を表示するビュー
    template_name = 'chat/chat_box.html'
    
    