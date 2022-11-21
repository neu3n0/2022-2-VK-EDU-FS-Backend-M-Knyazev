from .models import Message
from chats.models import ChatMember

from .serializers import MessageSerializer, MessageCreateSerializer, MessageListSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.exceptions import ValidationError

from django.db.models import Q


def user_in_chat(chat, user):
    return ChatMember.objects.filter(Q(user__id=user) & Q(chat__id=chat)).exists()


class MessageCreate(CreateAPIView):
    serializer_class = MessageCreateSerializer
    queryset = Message.objects.all()

    def perform_create(self, serializer):
        if not user_in_chat(chat=self.request.POST.get('chat'),
                            user=self.request.POST.get('author')):
            raise ValidationError('This user is not in this chat')
        return super().perform_create(serializer)


class MessageRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageListList(ListAPIView):
    serializer_class = MessageListSerializer
    queryset = Message.objects.all()
