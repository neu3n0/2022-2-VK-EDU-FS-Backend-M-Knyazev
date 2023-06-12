from django.urls import path
from .views import UserView, MeUserView

urlpatterns = [
    path('<int:pk>/', UserView.as_view(), name='user_info'),
    path('', MeUserView.as_view(), name='meuser_info'),
]
