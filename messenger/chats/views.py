from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from .models import Chat, ChatProfile
from users.models import User
from messagesChat.models import Message
from django.shortcuts import get_object_or_404


# def processing_chat(chat_id):
#     try:
#         chat = Chat.objects.get(id=chat_id)
#     except Chat.DoesNotExist:
#         chat = None
#     return chat


@require_POST
def create_chat(request):
    # берем автора и остальную инфу из request.POST?
    creator = request.POST['chat_creator']
    title = request.POST['chat_title']
    desciption = request.POST['chat_description']
    category = request.POST['chat_category']
    profile = ChatProfile.objects.create(title=title, desciption=desciption)
    Chat.objects.create(creator=creator, profile=profile, category=category)
    # что вернуть?
    resp = JsonResponse({'?': '???'})
    return resp


@require_GET
def get_chat_description(request, pk):
    chat = get_object_or_404(Chat, pk)
    description = chat.profile.description
    resp = JsonResponse({'description': description})
    return resp


@require_GET
def chat_list(request, user_id):
    user = get_object_or_404(User, user_id)
    # for chat in user.


@require_POST
def edit_chat(request, pk):
    chat = get_object_or_404(Chat, pk)
    # Тут что-то с POST запросом надо придумать?
    # меняем объект
    chat.save()
    # что вернуть, типо id чата и какую-то инфу про него,
    # чтобы на фронте отрисовать что-то по этим данным,
    # напрмиер успешно редактирован {название чата}?
    resp = JsonResponse({'chat_title': chat.profile.title})
    return resp


@require_POST
def remove_chat(request, pk):
    chat = get_object_or_404(Chat, pk)
    title = chat.profile.title
    count = chat.profile.counts_users
    chat.delete()
    # аналагично edit_chat вернуть?
    resp = JsonResponse({'chat_title': title, 'count_users': count})
    return resp


@require_GET
def show_chat(request, pk):
    chat = get_object_or_404(Chat, pk)
    messages = Message.objects.filter(chat_id=pk)
    messages.order_by('-pub_date')
    messages = messages[0:20]
    return JsonResponse({'messages': messages})
