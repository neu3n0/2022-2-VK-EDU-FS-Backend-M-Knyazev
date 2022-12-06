from rest_framework import serializers
from .models import Chat, ChatMember
from messageschat.models import Message
from django.shortcuts import get_object_or_404
from django.db.models import Q
from messageschat.serializers import LastMessageSerializer, MessageSerializer
from django.db import transaction, IntegrityError
from users.models import User
from rest_framework.exceptions import ValidationError

from .tasks import send_admin_email, create_chat_ws


class ChatCreateSerializer(serializers.ModelSerializer):
    """Serializer for chat"""

    new_members = serializers.ListField(write_only=True, required=False)

    members = serializers.ListField(source='get_members', read_only=True)
    admins = serializers.ListField(source='get_admins', read_only=True)

    @transaction.atomic
    def save(self, **kwargs):
        members = self.validated_data.pop('new_members', {})
        chat = super().save(**kwargs)
        ChatMember.objects.create(
            chat=chat,
            user=self.context['request'].user,
            chat_admin=True
        )
        create_chat_ws.delay(
            {
                "chat": {
                    "id": chat.id,
                    "title": chat.title,
                    "category": chat.title,
                },
                "muted": 'false',
                "last_message": None,
            }
        )
        try:
            for member in members:
                user = User.objects.get(id=member)
                ChatMember.objects.create(
                    chat=chat,
                    user=user,
                    added_by_user=self.context['request'].user
                )
        except IntegrityError:
            raise ValidationError('u cant add creator to member list')
        except:
            raise ValidationError(f'user with id={member} does not exits')
        return chat

    class Meta:
        model = Chat
        fields = (
            'title',
            'description',
            'category',
            'private',
            'new_members',
            'members',
            'admins'
        )


class ChatListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('id', 'title', 'category', 'created_at')


class ChatMemberListSerializer(serializers.ModelSerializer):

    chat = ChatListSerializer()
    last_message = serializers.SerializerMethodField()

    def get_last_message(self, obj):
        l_message = Message.objects.filter(chat_id=obj.chat.id).first()
        if (l_message):
            return LastMessageSerializer(l_message).data
        return None

    class Meta:
        model = ChatMember
        fields = ('chat', 'muted', 'last_message',)


class ChatMemberSerializer(serializers.ModelSerializer):

    def save(self, **kwargs):
        chatmember = super().save(**kwargs)
        print(self.context['request'].user.id, self.context['request'].user.username,
              chatmember.chat.id, chatmember.chat.title)
        send_admin_email.delay(
            self.context['request'].user.id, self.context['request'].user.username, chatmember.chat.id, chatmember.chat.title)
        return chatmember

    class Meta:
        model = ChatMember
        fields = ('user', 'chat', 'chat_admin')


class ChatSerializer(serializers.ModelSerializer):
    """Serializer for chat"""

    members = serializers.ListField(source='get_members')
    admins = serializers.ListField(source='get_admins')
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = '__all__'

    def get_messages(self, obj):
        return MessageSerializer(obj.chat_messages, many=True).data


class ChatEditSerializer(serializers.ModelSerializer):

    new_members = serializers.ListField(write_only=True)

    @transaction.atomic
    def update(self, instance, validated_data):
        members = validated_data.get('new_members')
        for member in members:
            user = get_object_or_404(User, id=member)
            ChatMember.objects.create(
                chat=instance,
                user=user,
                added_by_user=self.context['request'].user
            )
        return super().update(instance, validated_data)

    """Serializer for chat"""
    class Meta:
        model = Chat
        fields = ('title', 'description', 'new_members')


class ChatMemberEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatMember
        fields = ('muted', 'chat_admin')
