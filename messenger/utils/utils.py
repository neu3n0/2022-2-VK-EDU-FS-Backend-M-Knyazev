from chats.models import ChatMember
from django.db.models import Q


def user_in_chat(chat, user):
    return ChatMember.objects.filter(Q(user__id=user) & Q(chat__id=chat)).exists()
