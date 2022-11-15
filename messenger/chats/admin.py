from django.contrib import admin
from .models import Chat, ChatMember


@admin.register(ChatMember)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('user', 'chat', 'added_at')
    model = ChatMember


class ChatMemberInlie(admin.TabularInline):
    model = ChatMember


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    inlines = [ChatMemberInlie]
    list_display = ('id', 'title', 'description', 'created_at', 'chat_admin')
    model = Chat
