from django.contrib import admin
from .models import Chat

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    filter_horizontal = ('members',)
    list_display = ('id', 'title', 'description', 'created_at', 'creator')
    model = Chat