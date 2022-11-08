import json
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from .models import Chat
from users.models import User
from messagesChat.models import Message
from django.shortcuts import get_object_or_404


@require_POST
def create_chat(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if (not request.POST.get('title') and not request.POST.get('category')):
        return JsonResponse({'bad_input': True})
    chat = Chat.objects.create(title=request.POST['title'], creator=user)
    if request.POST.get('description'):
        chat.description = request.POST['description']
    if request.POST.get('category') and request.POST['category'] in ('G', 'B', 'D'):
        chat.category = request.POST['category']
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
    if request.POST.get('title'):
        chat.title = request.POST['title']
    if request.POST.get('description'):
        chat.description = request.POST['description']
    if request.POST.get('category') and request.POST['category'] in ('G', 'B', 'D'):
        chat.category = request.POST['category']
    chat.save()
    resp = JsonResponse({
        'title': chat.title,
        'description': chat.description,
        'category': chat.category,
    })
    return resp


def remove_chat(request, pk):
    if request.method != "DELETE":
        return JsonResponse({'removed': False})
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

@require_POST
def add_user_to_chat(request, chat_id, user_id):
    chat = get_object_or_404(Chat, pk=chat_id)
    user = get_object_or_404(User, pk=user_id)
    if chat.members.filter(pk=user.pk).exists():
        return JsonResponse({'exits': True})
    chat.members.add(user)
    resp = JsonResponse({
        'username': user.username,
        'chat': chat.title,
    })
    return resp

def remove_user_to_chat(request, chat_id, user_id):
    chat = get_object_or_404(Chat, pk=chat_id)
    user = get_object_or_404(User, pk=user_id)
    if request.method != "DELETE":
        return JsonResponse({'removed_user': False})
    if not chat.members.filter(pk=user.pk).exists():
        return JsonResponse({'exits': False})
    chat.members.remove(user)
    resp = JsonResponse({
        'username': user.username,
        'chat': chat.title,
    })
    return resp