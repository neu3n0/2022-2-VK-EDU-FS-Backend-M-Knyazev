from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.shortcuts import get_object_or_404
from messagesChat.models import Message
from chats.models import Chat
from users.models import User


@require_POST
def create_message(request, user_id, chat_id):
    author = get_object_or_404(User, pk=user_id)
    chat = get_object_or_404(Chat, pk=chat_id)
    if (not request.POST.get('content')):
        return JsonResponse(
            {
                'error': 'no input',
                'content': request.POST.get('content')
            },
            status=400
        )
    message = Message.objects.create(
        chat=chat, author=author, content=request.POST['content'])
    return JsonResponse({
        'author_username': message.author.username,
        'chat_title': chat.title,
        'content': message.content,
        'pub_date': message.pub_date,
        'is_readed': message.is_readed,
    })


@require_GET
def get_message_info(request, pk):
    message = get_object_or_404(Message, pk=pk)
    return JsonResponse({
        'author_username': message.author.username,
        'message': message.content,
        'is_readed': message.is_readed,
        'pub_date': message.pub_date,
        'chat_id': message.chat.id
    })


@require_GET
def get_messages_from_chat(request, chat_pk):
    get_object_or_404(Chat, chat_pk)
    messages = Message.objects.filter(chat_id=chat_pk)
    if not request.GET.get('user'):
        return JsonResponse(
            {
                'error': 'bad input, user_id is necessary',
                'messages': []
            },
            status=400,
        )
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


@require_http_methods(["DELETE"])
def remove_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    message.delete()
    return HttpResponse()


@require_POST
def is_readed(request, pk):
    message = get_object_or_404(Message, pk=pk)
    message.is_readed = True
    message.save()
    resp = JsonResponse({
        'id': message.id,
        'content': message.content,
        'is_readed': message.is_readed,
    })
    return resp
