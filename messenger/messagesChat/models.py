from django.db import models
from users.models import User
from chats.models import Chat


class Message(models.Model):
    # можно ввести тип контента (текст, видео кружочек, голосовое сообщение, файл). Сообщение хранить в текст филд, другие в облаке.
    # чат можно сделать будет ManyToMany - ...
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    pub_data = models.DateTimeField(auto_now_add=True)
    is_readed = models.BooleanField(default=False)
