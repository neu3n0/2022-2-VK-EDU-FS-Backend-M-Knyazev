import imp
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from messagesChat.models import Message
from chats.models import Chat


@require_POST
def create_message(request, sender_id: int, chat_id: int, message_text: str):
    # creator = request.POST['chat_creator']
    # title = request.POST['chat_title']
    # desciption = request.POST['chat_description']
    # category = request.POST['chat_category']
    # profile = ChatProfile.objects.create(title=title, desciption=desciption)
    # Chat.objects.create(creator=creator, profile=profile, category=category)
    # # что вернуть?
    resp = JsonResponse({'?': '???'})
    return resp


@require_GET
def get_message_info(request, pk):
    message = get_object_or_404(Message, pk)
    resp = JsonResponse({'author': message.author, 'message': message.content,
                        'is_readed': message.is_readed, 'pub_date': message.pub_date})
    return resp

@require_GET
def get_messages_from_chat(request, chat_index):
    chat = get_object_or_404(Chat, pk=chat_index)
    messages = Message.objects.filter(chat_id=chat_index)
    messages.order_by('-pub_date')
