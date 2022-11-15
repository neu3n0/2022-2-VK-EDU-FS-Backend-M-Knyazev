from django.urls import path

from messageschat.views import create_message, edit_message, get_message_info, get_messages_from_chat, remove_message, is_readed

urlpatterns = [
    path('create/<int:user_id>/', create_message, name='create_message'),
    path('message_info/<int:pk>/', get_message_info, name='get_message_info'),
    path('chat_messages/<int:chat_pk>/',
         get_messages_from_chat, name='get_messages_from_chat'),
    path('edit/<int:pk>/', edit_message, name='edit_message'),
    path('is_readed/<int:pk>/', is_readed, name='is_readed'),
    path('remove/<int:pk>/', remove_message, name='remove_message'),
]
