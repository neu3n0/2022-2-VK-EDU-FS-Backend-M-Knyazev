from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for message"""
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'id',
            'username',
            'mobile',
            'description',
            'age',
            'is_active',
            'is_superuser',
        )
