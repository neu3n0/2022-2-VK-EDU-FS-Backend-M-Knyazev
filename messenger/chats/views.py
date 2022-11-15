import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Chat, ChatMember
from users.models import User
from messageschat.models import Message
from django.shortcuts import get_object_or_404
from django.db.models import Q


@require_POST
def create_chat(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if (not request.POST.get('title') or
        not (request.POST.get('category') and
             request.POST.get('category') in ('G', 'B', 'D'))):
        return JsonResponse(
            {
                'error': 'title and category are necessary',
                'title': request.POST.get('title'),
                'category': request.POST.get('category')
            },
            status=400
        )
    chat = Chat.objects.create(
        title=request.POST['title'], category=request.POST['category'])
    if request.POST.get('description'):
        chat.description = request.POST['description']
    if chat.category in ('G', 'B'):
        chat.chat_admin = user
    return JsonResponse({
        'title': chat.title,
        'category': chat.category,
        'description': chat.description,
        'created_at': chat.created_at,
        'admin_username': chat.chat_admin.username if chat.chat_admin else None,
        'admin_id': chat.chat_admin.pk if chat.chat_admin else None,
    })


@require_GET
def get_chat_description(request, pk):
    chat = get_object_or_404(Chat, pk=pk)
    return JsonResponse({
        'title': chat.title,
        'category': chat.category,
        'description': chat.description,
        'created_at': chat.created_at,
        'admin_username': chat.chat_admin.username if chat.chat_admin else None,
        'admin_id': chat.chat_admin.pk if chat.chat_admin else None,
    })


@require_GET
def chat_list(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    chat_members = user.user_members.all()
    chats = []
    for chat in chat_members:
        chats.append({'id': chat.chat.id, 'title': chat.chat.title})
    return JsonResponse({'chats': chats})


@require_POST
def edit_chat(request, pk):
    get_object_or_404(Chat, pk=pk)
    chat = Chat.objects.filter(pk=pk)
    chat_title = request.POST['title'] if request.POST.get(
        'title') else chat.first().title
    chat_description = request.POST['description'] if request.POST.get(
        'description') else chat.first().description
    chat_category = request.POST['category'] if request.POST.get(
        'category') else chat.first().category
    chat.update(
        title=chat_title,
        description=chat_description,
        category=chat_category,
    )
    return JsonResponse({
        'title': chat_title,
        'description': chat_description,
        'category': chat_category,
    })


@require_http_methods(["DELETE"])
def remove_chat(request, pk):
    chat = get_object_or_404(Chat, pk=pk)
    chat.delete()
    return HttpResponse()


@require_GET
def show_chat(request, pk):
    get_object_or_404(Chat, pk=pk)
    messages = Message.objects.filter(chat_id=pk)
    messages_ar = []
    for mess in messages:
        messages_ar.append(
            {
                'author': mess.author.username,
                'text': mess.text,
                'date': mess.pub_date,
                'readed': mess.is_readed
            }
        )
    return JsonResponse({'messages': messages_ar})


@require_POST
def add_user_to_chat(request, chat_id, user_id):
    chat = get_object_or_404(Chat, pk=chat_id)
    user = get_object_or_404(User, pk=user_id)
    if chat.chat_members.filter(user_id=user.pk).exists():
        return JsonResponse(
            {
                'error': 'this user is already in the chat',
                'username': user.username,
                'chat': chat.title,
            },
            status=400
        )
    ChatMember.objects.create(chat=chat, user=user)
    return JsonResponse({
        'username': user.username,
        'chat': chat.title,
    })


@require_http_methods(["DELETE"])
def remove_user_to_chat(request, chat_id, user_id):
    member = ChatMember.objects.filter(Q(user_id=user_id) & Q(chat_id=chat_id))
    member.delete()
    return JsonResponse({
        'user_id': user_id,
        'chat_id': chat_id,
    })
