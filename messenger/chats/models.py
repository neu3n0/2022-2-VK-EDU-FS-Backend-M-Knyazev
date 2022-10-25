from django.db import models
from users.models import User


class ChatProfile(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    counts_users = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Chat(models.Model):
    GROUP = 'G'
    BLOG = 'B'
    DIALOG = 'D'
    CHAT_TYPE = (
        (GROUP, 'Group chat'),
        (BLOG, 'Blog'),
        (DIALOG, 'Correspondence 1 on 1'),
    )
    profile = models.OneToOneField(ChatProfile, on_delete=models.CASCADE)
    creator = models.ForeignKey(
        User, null=True, related_name='creator', on_delete=models.SET_NULL)
    members = models.ManyToManyField(User)
    type = models.IntegerField(choices=CHAT_TYPE, default=DIALOG)
