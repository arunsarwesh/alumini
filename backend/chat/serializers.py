from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import ChatMessage as Message

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'profile_photo']

class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source='sender.username', read_only=True)
    time = serializers.DateTimeField(source='timestamp', format='%H:%M')
    
    class Meta:
        model = Message
        fields = ['id', 'content', 'timestamp', 'sender', 'sender_name', 'receiver', 'receiver_name']