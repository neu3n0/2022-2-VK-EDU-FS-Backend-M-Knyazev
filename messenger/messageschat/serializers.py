from rest_framework import serializers

from .models import Message


class MessageCreateSerializer(serializers.ModelSerializer):
    """Serializer for create message"""

    class Meta:
        model = Message
        fields = (
            'author',
            'chat',
            'text',
            'pub_date',
        )


class MessageSerializer(serializers.ModelSerializer):
    """Serializer for message"""

    author_username = serializers.CharField(
        source='get_author_username',
        read_only=True
    )
    chat_title = serializers.CharField(source='get_chat_title', read_only=True)

    class Meta:
        model = Message
        fields = (
            'author_username',
            'chat_title',
            'text',
            'pub_date',
            'is_readed',
            'count_readers',
            'edited',
        )


class LastMessageSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='get_author_username')

    class Meta:
        model = Message
        fields = (
            'author_username',
            'text',
            'pub_date',
            'is_readed',
        )


class MessageListSerializer(serializers.ModelSerializer):
    """Serializer for message"""

    author_username = serializers.CharField(
        source='get_author_username',
        read_only=True
    )

    class Meta:
        model = Message
        fields = (
            'author_username',
            'text',
            'pub_date',
            'is_readed',
            'count_readers',
            'edited',
        )
