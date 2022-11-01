from email.policy import default
from django.db import models
from users.models import User


class Chat(models.Model):
    GROUP = 'G'
    BLOG = 'B'
    DIALOG = 'D'
    CHAT_TYPE = (
        (GROUP, 'Group chat'),
        (BLOG, 'Blog'),
        (DIALOG, 'Correspondence 1 on 1'),
    )
    creator = models.ForeignKey(
        User, null=True, related_name='creator_chats', on_delete=models.SET_NULL)
    members = models.ManyToManyField(User, default=creator)
    title = models.CharField(max_length=150, null=False, blank=False, default='chat_name')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    category = models.CharField(
        max_length=1, choices=CHAT_TYPE, null=False, blank=False, default=DIALOG)
