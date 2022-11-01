from django.db import models
from users.models import User
from chats.models import Chat


class Message(models.Model):
    chat = models.ForeignKey(Chat, null=False, blank=False, on_delete=models.CASCADE, related_name='chat_messages')
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name='author_messages')
    content = models.TextField(null=False, blank=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_readed = models.BooleanField(default=False)