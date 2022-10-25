from email.policy import default
from django.db import models
from users.models import User
from chats.models import Chat


class Message(models.Model):
    # можно ввести тип контента (текст, видео кружочек, голосовое сообщение, файл). Сообщение хранить в текст филд, другие в облаке.
    # чат можно сделать будет ManyToMany - ...
    chat = models.ForeignKey(Chat, null=False, blank=False, on_delete=models.CASCADE, related_name='chat_messages')
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name='author_messages')
    content = models.TextField(null=False, blank=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_readed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Message #{self.pk} from {self.author.username}'