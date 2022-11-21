import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Chat, ChatMember
from users.models import User
from messageschat.models import Message
from django.shortcuts import get_object_or_404
from django.db.models import Q


from .serializers import ChatSerializer, ChatEditSerializer, ChatMemberSerializer, ChatMemberListSerializer, ChatCreateSerializer

from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, RetrieveUpdateAPIView


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

    # def perform_create(self, serializer):
    #     chat = serializer.save()
    #     if (self.request.user):
    #         ChatMember.objects.create(
    #             chat=chat, user=self.request.user, chat_admin=True)


class UsersChatsList(ListAPIView):
    serializer_class = ChatMemberListSerializer
    queryset = ChatMember.objects.all()

    def get_queryset(self):
        # можно просто прокидывать self.request.user
        user_id = self.request.GET.get('user_id')
        get_object_or_404(User, id=user_id)
        return ChatMember.objects.filter(user__id=user_id)


class ChatRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return ChatEditSerializer
        return ChatSerializer

    def update(self, request, *args, **kwargs):
        ans = super().update(request, *args, **kwargs)
        print(ans)
        return ans


class ChatMemberCreate(CreateAPIView):
    serializer_class = ChatMemberSerializer

    def get_queryset(self):
        return ChatMember.objects.filter(pk=self.kwargs.get('chat_id'))

    def perform_create(self, serializer):
        serializer.save(added_by_user=self.request.user)
