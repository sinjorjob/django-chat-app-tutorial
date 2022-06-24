from django.contrib import admin
from .models import Friends, Messages


class FriendsAdmin(admin.ModelAdmin):
    list_display=('pk','user', 'friend',)


class MessagesAdmin(admin.ModelAdmin):
    list_display=('pk','description','sender_name', 'receiver_name','time', 'seen', 'timestamp')


admin.site.register(Friends,FriendsAdmin)
admin.site.register(Messages, MessagesAdmin)