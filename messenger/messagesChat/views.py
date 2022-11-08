from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from messagesChat.models import Message
from chats.models import Chat
from users.models import User


@require_POST
def create_message(request, user_id: int, chat_id: int):
    author = get_object_or_404(User, pk=user_id)
    chat = get_object_or_404(Chat, pk=chat_id)
    if (not request.POST.get('content')):
        return JsonResponse({'bad_input': True})
    message = Message.objects.create(
        chat=chat, author=author, content=request.POST['content'])

    resp = JsonResponse({
        'author_username': message.author.username,
        'author_id': message.author.id,
        'chat_id': chat.id,
        'content': message.content,
        'pub_date': message.pub_date,
        'is_readed': message.is_readed,
    })
    return resp


@require_GET
def get_message_info(request, pk):
    message = get_object_or_404(Message, pk=pk)
    resp = JsonResponse({
        'author_username': message.author.username,
        'message': message.content,
        'is_readed': message.is_readed,
        'pub_date': message.pub_date,
        'chat_id': message.chat.id
    })
    return resp


@require_GET
def get_messages_from_chat(request, chat_pk):
    messages = Message.objects.filter(chat_id=chat_pk)
    if not messages.exists():
        return JsonResponse({'exist chat': False})
    if not request.GET.get('user'):
        return JsonResponse({'messages': []})
    messages = messages.filter(author_id=request.GET['user'])
    messages_ar = []
    for mess in messages:
        messages_ar.append({'text': mess.content,
                           'date': mess.pub_date, 'readed': mess.is_readed})
    return JsonResponse({'messages': messages_ar})


@require_POST
def edit_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if (request.POST.get('content')):
        message.content = request.POST['content']
    message.save()
    resp = JsonResponse({
        'id': message.id,
        'author': message.author,
        'content': message.content,
    })
    return resp


def remove_message(request, pk):
    if request.method != "DELETE":
        return JsonResponse({'removed_message': False})
    message = get_object_or_404(Message, pk=pk)
    message.delete()
    resp = JsonResponse({'removed_message': True})
    return resp

@require_POST
def edit_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    message.is_readed = True
    message.save()
    resp = JsonResponse({
        'id': message.id,
        'content': message.content,
        'is_readed': message.is_readed,
    })
    return resp