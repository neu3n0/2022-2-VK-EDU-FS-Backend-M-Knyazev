from django.db import models
from users.models import User
from chats.models import Chat


class Message(models.Model):
    """"Message model"""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author_messages',
        verbose_name='Автор'
    )
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name='chat_messages',
        verbose_name='Чат'
    )
    text = models.TextField(verbose_name='Текст сообщения')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    is_readed = models.BooleanField(default=False, verbose_name='Прочитано')
    edited = models.BooleanField(default=False, verbose_name='Изменено')
    count_readers = models.IntegerField(
        default=0,
        verbose_name='Количество прочтений'
    )

    def get_author_username(self):
        return self.author.username

    def get_chat_title(self):
        return self.chat.title

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-pub_date']
