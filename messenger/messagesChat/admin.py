from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'content', 'pub_date', 'is_readed', 'chat')
    model = Message