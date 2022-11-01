from django.urls import path

from messagesChat.views import create_message, edit_message, get_message_info, get_messages_from_chat, remove_message

urlpatterns = [
    path('create/<int:user_id>/', create_message, name='create_message'),
    path('message_info/<int:pk>/', get_message_info, name='get_message_info'),
    path('chat_messages/<int:chat_pk>/',
         get_messages_from_chat, name='get_messages_from_chat'),
    path('edit/<int:pk>/', edit_message, name='edit_message'),
    path('remove/<int:pk>/', remove_message, name='remove_message'),
]
