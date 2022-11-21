from django.urls import path
from .views import create_user, get_user_info, UserChatListView

urlpatterns = [
    path('create/', create_user, name='create_user'),
    path('get_info/<int:pk>/', get_user_info, name='get_user_info'),
    path('chat_list/', UserChatListView.as_view()),
]
