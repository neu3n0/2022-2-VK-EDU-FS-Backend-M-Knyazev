from django.urls import path
from settings.views import show_settings

urlpatterns = [
    path('', show_settings, name='settings'),
]