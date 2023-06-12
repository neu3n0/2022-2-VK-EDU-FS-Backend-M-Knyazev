from .models import Message
from chats.models import ChatMember, Chat

from .serializers import MessageSerializer, MessageCreateSerializer, MessageListSerializer, TestCreateSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from utils.utils import user_in_chat

from django.http import JsonResponse

def test(request):
    print(request.user ,request.method, request.body, request.POST.get('text'), request)
    return JsonResponse({'1': 'a'})

class TestCreate(CreateAPIView):
    serializer_class = TestCreateSerializer
    queryset = Message.objects.all()




class MessageCreate(CreateAPIView):
    serializer_class = MessageCreateSerializer
    queryset = Message.objects.all()

    def perform_create(self, serializer):
        # if self.request.user.id != int(self.request.POST.get('author')):
        #     raise ValidationError('current user != message user')
        # if not user_in_chat(chat=self.request.POST.get('chat'),
        #                     user=self.request.user.id):
        #     raise ValidationError('This user is not in this chat')
        return super().perform_create(serializer)


class MessageRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_object(self):
        mess = get_object_or_404(Message, pk=self.kwargs.get('pk'))
        chat = mess.chat
        if not user_in_chat(chat.id, self.request.user.id):
            raise ValidationError('This user is not in this chat')
        return super().get_object()


class MessageList(ListAPIView):
    serializer_class = MessageListSerializer
    queryset = Message.objects.all()
