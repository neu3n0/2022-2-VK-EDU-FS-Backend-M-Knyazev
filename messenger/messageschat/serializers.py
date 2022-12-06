from rest_framework import serializers

from .models import Message
from .tasks import create_mess_ws
from django.db import transaction
from bs4 import BeautifulSoup


class MessageCreateSerializer(serializers.ModelSerializer):
    """Serializer for create message"""

    @transaction.atomic
    def save(self, **kwargs):
        t = self.validated_data['text']
        soup = BeautifulSoup(t, 'html.parser')

        # 1
        # if soup.get_text() != t:
        #     self.validated_data['text'] = 'бэд хацкер))))))'

        # 2
        # for s in soup.select('script, img'):
        #     s.extract()
        # self.validated_data['text'] = str(soup)

        # 3
        invalid_tags = ['script', 'img']
        for tag in invalid_tags:
            for match in soup.findAll(tag):
                match.replaceWithChildren()

        self.validated_data['text'] = str(soup)

        mess = super().save(**kwargs)
        create_mess_ws.delay(
            {
                "id": mess.id,
                "author_username": mess.author.username,
                "author_id": mess.author.id,
                "chat_title": "chatOne",
                "text": mess.text,
                "pub_date": mess.pub_date,
                "is_readed": mess.is_readed,
                "count_readers": mess.count_readers,
                "edited": mess.edited
            }
        )
        return mess

    class Meta:
        model = Message
        fields = (
            'id',
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

    chat_title = serializers.CharField(
        source='get_chat_title',
        read_only=True
    )

    class Meta:
        model = Message
        fields = (
            'id',
            'author_username',
            'author_id',
            'chat_title',
            'text',
            'pub_date',
            'is_readed',
            'count_readers',
            'edited',
        )


class LastMessageSerializer(serializers.ModelSerializer):
    """Serializer for last message"""
    author_username = serializers.CharField(source='get_author_username')

    class Meta:
        model = Message
        fields = (
            'id',
            'author_username',
            'text',
            'pub_date',
            'is_readed',
        )


class MessageListSerializer(serializers.ModelSerializer):
    """Serializer for list messages"""

    author_username = serializers.CharField(
        source='get_author_username',
        read_only=True
    )

    class Meta:
        model = Message
        fields = (
            'id',
            'author_username',
            'text',
            'pub_date',
            'is_readed',
            'count_readers',
            'edited',
        )
