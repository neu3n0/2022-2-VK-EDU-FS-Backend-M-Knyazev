from django.urls import path

from .views import MessageCreate, MessageRetrieveUpdateDestroy

urlpatterns = [
    path('create/', MessageCreate.as_view()),
    path('<int:pk>/', MessageRetrieveUpdateDestroy.as_view()),
]
