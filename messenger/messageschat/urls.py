from django.urls import path

from .views import MessageCreate, MessageRetrieveUpdateDestroy, MessageListList

urlpatterns = [
    path('create/', MessageCreate.as_view()),
    path('<int:pk>/', MessageRetrieveUpdateDestroy.as_view()),
    path('chat/<int:chat_id>/', MessageListList.as_view()),
]
