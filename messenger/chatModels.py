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


class GroupChat(models.Model):
    """"
        ?
    """
    chat_id = models.ForeignKey(
        Chat,
        related_name='chat_id_groupchats',
        on_delete=models.CASCADE,
        verbose_name='ID чата',
    )
    chat_admin = models.ForeignKey(
        User,
        related_name='admin_chats',
        on_delete=models.SET_NULL,
        verbose_name='Администратор чата',
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=150, verbose_name='Название')


class Dialog(models.Model):
    """"
        ?
    """
    chat_id = models.ForeignKey(
        Chat,
        related_name='chat_id_dialogs',
        on_delete=models.CASCADE,
        verbose_name='ID чата',
    )
    member_one = models.ForeignKey(
        User,
        related_name='member_one_chats',
        on_delete=models.SET_NULL,
        verbose_name='Участник #1',
    )
    member_two = models.ForeignKey(
        User,
        related_name='member_two_chats',
        on_delete=models.SET_NULL,
        verbose_name='Участник #2',
    )


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
        verbose_name='ID пользователья'
    )
    added_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления пользователя'
    )
    # added_by_user = models.ForeignKey(
    #     User,
    #     related_name='added_by_user_members',
    #     on_delete=models.SET_NULL,
    #     verbose_name='ID пользователья'
    # )

    class Meta:
        verbose_name = 'Пользователь чата'
        verbose_name_plural = 'Пользователи чата'
        ordering = ['added_at']



# class Chat(models.Model):
#     """"Chat model"""
#     member_one = models.ForeignKey(
#         User,
#         related_name='member_one_chats',
#         on_delete=models.SET_NULL,
#         verbose_name='Участник чата #1',
#     )
#     member_two = models.ForeignKey(
#         User,
#         related_name='member_two_chats',
#         on_delete=models.SET_NULL,
#         verbose_name='Участник чата #2',
#     )
#     title = models.CharField(max_length=150, verbose_name='Название')
#     created_at = models.DateTimeField(
#         auto_now_add=True,
#         verbose_name='Дата создания'
#     )

#     class Meta:
#         verbose_name = 'Диалог'
#         verbose_name_plural = 'Диалоги'


# class GroupChat(models.Model):
#     """"Group Chat model

#         TO DO! Chat type: bot?
#     """
#     GROUP = 'G'
#     BLOG = 'B'
#     CHAT_TYPE = (
#         (GROUP, 'Group chat'),
#         (BLOG, 'Blog'),
#     )
#     chat_admin = models.ForeignKey(
#         User,
#         related_name='admin_chats',
#         on_delete=models.SET_NULL,
#         verbose_name='Администратор чата',
#     )
#     title = models.CharField(max_length=150, verbose_name='Название')
#     description = models.TextField(
#         verbose_name='Описание',
#         null=True,
#         blank=True,
#     )
#     created_at = models.DateTimeField(
#         auto_now_add=True,
#         verbose_name='Дата создания'
#     )
#     category = models.CharField(
#         max_length=1,
#         choices=CHAT_TYPE,
#         verbose_name='Категория'
#     )

#     class Meta:
#         verbose_name = 'Групповой чат'
#         verbose_name_plural = 'Групповые чаты'
