from django.db import models
from users.models import User


class Chat(models.Model):
    """"Chat model

        If chat type is dialog, then chat_admin = null

        TO DO! Chat type: bot?
    """
    GROUP = 'G'
    BLOG = 'B'
    DIALOG = 'D'
    CHAT_TYPE = (
        (GROUP, 'Group chat'),
        (BLOG, 'Blog'),
        (DIALOG, 'Correspondence 1 on 1'),
    )
    chat_admin = models.ForeignKey(
        User,
        related_name='admin_chats',
        on_delete=models.SET_NULL,
        verbose_name='Администратор чата',
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    category = models.CharField(
        max_length=1,
        choices=CHAT_TYPE,
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class ChatMember(models.Model):
    """"Chat members model"""
    chat = models.ForeignKey(
        Chat,
        related_name='chat_members',
        on_delete=models.CASCADE,
        verbose_name='ID чата'
    )
    user = models.ForeignKey(
        User,
        related_name='user_members',
        on_delete=models.CASCADE,
        verbose_name='ID пользователя',
    )
    added_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления пользователя'
    )
    added_by_user = models.ForeignKey(
        User,
        related_name='added_by_user_members',
        on_delete=models.SET_NULL,
        verbose_name='ID добавившего пользователя',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Пользователь чата'
        verbose_name_plural = 'Пользователи чата'
        ordering = ['added_at']
