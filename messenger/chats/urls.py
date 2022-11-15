from django.urls import path
from .views import chat_list, create_chat, edit_chat, get_chat_description, remove_chat, show_chat, add_user_to_chat, remove_user_to_chat

urlpatterns = [
    path('create/<int:user_id>/', create_chat, name='create_chat'),
    path('<int:pk>/description/', get_chat_description,
         name='get_chat_description'),
    path('list/<int:user_id>/', chat_list, name='chat_list'),
    path('<int:pk>/edit/', edit_chat, name='edit_chat'),
    path('<int:pk>/remove/', remove_chat, name='remove_chat'),
    path('<int:pk>/show/', show_chat, name='show_chat'),
    path('<int:chat_id>/add/<int:user_id>', add_user_to_chat, name='add_user_to_chat'),
    path('<int:chat_id>/rm/<int:user_id>', remove_user_to_chat, name='remove_user_to_chat'),
]
