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


class MessageEditSerializer(serializers.ModelSerializer):
    """Serializer for message text"""

    class Meta:
        model = Message
        fields = (
            'text',
            'edited',
            'is_readed',
            'count_readers'
        )



class MessageSerializer(serializers.ModelSerializer):
    """Serializer for message list"""

    author_username = serializers.CharField(source='get_author_username')
    chat_title = serializers.CharField(source='get_chat_title')

    class Meta:
        model = Message
        fields = (
            'id',
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










class MessageSerializer2(serializers.ModelSerializer):
    """Serializer for message"""

    # chat = serializers.CharField(source='get_chat_title')

    # chat = serializers.SerializerMethodField(method_name='get_chat_title')
    # def get_chat_title(self, message):
    #     title = message.chat.title + str(message.chat.id)
    #     return title

    class Meta:
        model = Message
        fields = (
            'author',
            'chat',
            'text',
            'pub_date',
            'is_readed',
            'count_readers',
        )


class MessageListSerializer(serializers.ModelSerializer):
    """Serializer for message list"""

    chat = serializers.CharField(source='get_chat_title')

    class Meta:
        model = Message
        fields = (
            'id',
            'author',
            'chat',
            'text',
            'pub_date',
            'is_readed',
            'count_readers',
        )
