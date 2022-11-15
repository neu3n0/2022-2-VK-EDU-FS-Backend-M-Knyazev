from django.db import models
from users.models import User
from chats.models import Chat


class Message(models.Model):
    """"Message model"""
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name='chat_messages',
        verbose_name='Чат'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author_messages',
        verbose_name='Автор'
    )
    text = models.TextField(verbose_name='Контент')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    is_readed = models.BooleanField(default=False, verbose_name='Прочитано')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-pub_date']
