from django.urls import path

from .views import MessageCreate, MessageRetrieveUpdateDestroy, MessageList, TestCreate

urlpatterns = [
    path('create/', MessageCreate.as_view()),
    path('<int:pk>/', MessageRetrieveUpdateDestroy.as_view()),
    path('chat/<int:chat_id>/', MessageList.as_view()),
    path('cr/', TestCreate.as_view()),
]
