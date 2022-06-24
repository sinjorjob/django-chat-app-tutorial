from rest_framework import serializers
from accounts.models import CustomUser
from chat.models import Messages


class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Messages
        fields = ['sender_name', 'receiver_name', 'description', 'time']