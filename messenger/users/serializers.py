from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for message"""
    class Meta:
        model = User
        fields = '__all__'


class UserChatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'