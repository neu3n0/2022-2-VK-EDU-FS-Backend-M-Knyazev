from tabnanny import verbose
from unicodedata import category
from django.db import models
from users.models import User


class ChatProfile(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    # count_users = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Chat {self.title} profile'


class Chat(models.Model):
    GROUP = 'G'
    BLOG = 'B'
    DIALOG = 'D'
    CHAT_TYPE = (
        (GROUP, 'Group chat'),
        (BLOG, 'Blog'),
        (DIALOG, 'Correspondence 1 on 1'),
    )
    profile = models.OneToOneField(
        ChatProfile, on_delete=models.CASCADE, related_name='profile_chat')
    creator = models.ForeignKey(
        User, null=True, related_name='creator_chats', on_delete=models.SET_NULL)
    # мб логичнее хранить в user его чаты, хотя разницы быть не должно вроде?)))))))
    members = models.ManyToManyField(User)
    category = models.CharField(
        max_length=1, choices=CHAT_TYPE, default=DIALOG)

    def __str__(self) -> str:
        return f'Chat #{self.pk}: {self.profile.title}'
