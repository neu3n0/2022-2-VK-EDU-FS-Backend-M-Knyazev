from django.urls import path
from chats.views import show_chat, chat_list, create_chat, show_start_menu

urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('<int:chat_id>/', show_chat, name='show_chat'),
    path('create/', create_chat, name='create_chat'),
]