from django.urls import path

from .views import ChatRetrieveUpdateDestroy, ChatCreate, ChatMemberCreate, UsersChatsList, ChatMemberDelete, ChatMembeSettings

urlpatterns = [
    path('<int:chat_id>/add/', ChatMemberCreate.as_view()),
    path('<int:chat_id>/rm/<int:user_id>/', ChatMemberDelete.as_view()),
    path('<int:chat_id>/<int:user_id>/', ChatMembeSettings.as_view()),
    path('<int:pk>/', ChatRetrieveUpdateDestroy.as_view()),
    path('create/', ChatCreate.as_view()),
    path('', UsersChatsList.as_view()),
]
