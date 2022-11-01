import json
from unicodedata import category
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from .models import Chat
from users.models import User
from messagesChat.models import Message
from django.shortcuts import get_object_or_404


@require_POST
def create_chat(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    chat = Chat.objects.create(title=request.POST['title'], creator=user,
                               description=request.POST['description'], category=request.POST['category'])
    resp = JsonResponse({
        'title': chat.title,
        'creator_username': chat.creator.username,
        'description': chat.description,
        'created_at': chat.created_at,
        'category': chat.category,
    })
    return resp


@require_GET
def get_chat_description(request, pk):
    chat = get_object_or_404(Chat, pk=pk)
    resp = JsonResponse({
        'title': chat.title,
        'description': chat.description,
        'category': chat.category,
        'created_at': chat.created_at,
        'creator_name': chat.creator.username,
        'creator_id': chat.creator.id,
    })
    return resp


@require_GET
def chat_list(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    chats = user.chats.all()
    chats_arr = []
    for chat in chats:
        chats_arr.append({'id': chat.pk, 'title': chat.title})
    resp = JsonResponse({'chats': chats_arr})
    return resp


@require_POST
def edit_chat(request, pk):
    chat = get_object_or_404(Chat, pk=pk)
    chat.title = request.POST['title']
    chat.description = request.POST['description']
    chat.category = request.POST['category']
    chat.save()
    resp = JsonResponse({
        'title': chat.title,
        'description': chat.description,
        'category': chat.category,
    })
    return resp


@require_POST
def remove_chat(request, pk):
    chat = get_object_or_404(Chat, pk=pk)
    chat.delete()
    resp = JsonResponse({'removed': True})
    return resp


@require_GET
def show_chat(request, pk):
    chat = get_object_or_404(Chat, pk=pk)
    messages = Message.objects.filter(chat_id=pk)
    messages.order_by('-pub_date')
    messages_ar = []
    for mess in messages:
        messages_ar.append({'author': mess.author.username, 'text': mess.content,
                           'date': mess.pub_date, 'readed': mess.is_readed})
    return JsonResponse({'messages': messages_ar})
