from django.urls import path
from .views import create_chat, edit_chat, get_chat_description, remove_chat, show_chat

urlpatterns = [
    path('create/<int:user_id>/', create_chat, name='create_chat'),
    path('description/<int:pk>/', get_chat_description,
         name='get_chat_description'),
    path('delete/<int:pk>/', remove_chat, name='remove_chat'),
    path('show/<int:pk>/', show_chat, name='show_chat'),
    path('edit/<int:pk>/', edit_chat, name='edit_chat'),
]
