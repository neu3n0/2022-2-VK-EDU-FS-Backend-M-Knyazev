from .models import Chat, ChatMember
from users.models import User
from django.shortcuts import get_object_or_404


from .serializers import ChatSerializer, ChatEditSerializer, ChatMemberSerializer, ChatMemberListSerializer, ChatCreateSerializer, ChatMemberEditSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.exceptions import ValidationError


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
        # можно просто прокидывать self.request.user
        user_id = self.request.GET.get('user_id')
        get_object_or_404(User, id=user_id)
        return ChatMember.objects.filter(user__id=user_id)


class ChatMemberCreate(CreateAPIView):
    serializer_class = ChatMemberSerializer
    queryset = ChatMember.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        chat_id = self.request.POST.get('chat')
        if not ChatMember.objects.filter(chat__id=chat_id).filter(user=user).exists():
            raise ValidationError('Only chat members can add another user')
        return super().perform_create(serializer)


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


class ChatMemberDelete(DestroyAPIView):
    serializer_class = ChatMemberSerializer
    queryset = ChatMember.objects.all()

    def get_object(self):
        return get_object_or_404(ChatMember, user__id=self.kwargs.get('user_id'), chat__id=self.kwargs.get('chat_id'))

    def perform_destroy(self, instance):
        user = self.request.user
        chat_id = self.kwargs.get('chat_id')
        if not ChatMember.objects.filter(chat__id=chat_id).filter(user=user).exists():
            raise ValidationError('Only chat members can remove another user')
        return super().perform_destroy(instance)


class ChatMembeSettings(UpdateAPIView):
    serializer_class = ChatMemberEditSerializer
    queryset = ChatMember.objects.all()

    def get_object(self):
        return get_object_or_404(ChatMember, user__id=self.kwargs.get('user_id'), chat__id=self.kwargs.get('chat_id'))
