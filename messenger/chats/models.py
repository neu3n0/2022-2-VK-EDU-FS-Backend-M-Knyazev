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
        User, null=True, related_name='creator_chats', on_delete=models.SET_NULL, verbose_name='Создатель чата')
    members = models.ManyToManyField(User, default=creator, related_name='chats', verbose_name='Участники')
    title = models.CharField(max_length=150, null=False, blank=False, default='chat_name', verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False, verbose_name='Дата создания')
    category = models.CharField(
        max_length=1, choices=CHAT_TYPE, null=False, blank=False, default=DIALOG, verbose_name='Категория')

    class Meta:
        verbose_name='Чат'
        verbose_name_plural='Чаты'
