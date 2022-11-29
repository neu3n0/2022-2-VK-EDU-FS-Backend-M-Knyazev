from .models import Chat, ChatMember
from users.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .serializers import ChatSerializer, ChatEditSerializer, ChatMemberSerializer, ChatMemberListSerializer, ChatCreateSerializer, ChatMemberEditSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.exceptions import ValidationError
from utils.utils import user_in_chat


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'home.html')


class ChatCreate(CreateAPIView):
    serializer_class = ChatCreateSerializer
    queryset = Chat.objects.all()

    # def create(self, request, *args, **kwargs):
    #     res = super().create(request, *args, **kwargs)
    #     ChatMember.objects.create(
    #         chat=Chat.objects.get(id=res.data.get('id')),
    #         user=self.request.user,
    #         chat_admin=True
    #     )
    #     return res


class UsersChatsList(ListAPIView):
    serializer_class = ChatMemberListSerializer
    queryset = ChatMember.objects.all()

    def get_queryset(self):
        return ChatMember.objects.filter(user=self.request.user)


class ChatMemberCreate(CreateAPIView):
    serializer_class = ChatMemberSerializer
    queryset = ChatMember.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        chat_id = self.request.POST.get('chat')
        if not ChatMember.objects.filter(chat_id=chat_id).filter(user=user).exists():
            raise ValidationError('Only chat members can add another user')
        return super().perform_create(serializer)


class ChatRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()

    def get_object(self):
        chat = get_object_or_404(Chat, pk=self.kwargs.get('pk'))
        if not user_in_chat(chat.id, self.request.user.id):
            raise ValidationError('This user is not in this chat')
        return super().get_object()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return ChatEditSerializer
        return ChatSerializer


class ChatMemberDelete(DestroyAPIView):
    serializer_class = ChatMemberSerializer
    queryset = ChatMember.objects.all()

    def get_object(self):
        return get_object_or_404(ChatMember, user_id=self.kwargs.get('user_id'), chat_id=self.kwargs.get('chat_id'))

    def perform_destroy(self, instance):
        if not user_in_chat(self.kwargs.get('chat_id'), self.request.user.id):
            raise ValidationError('Only chat members can remove another user')
        return super().perform_destroy(instance)


class ChatMembeSettings(UpdateAPIView):
    serializer_class = ChatMemberEditSerializer
    queryset = ChatMember.objects.all()

    def get_object(self):
        return get_object_or_404(ChatMember, user_id=self.kwargs.get('user_id'), chat_id=self.kwargs.get('chat_id'))
