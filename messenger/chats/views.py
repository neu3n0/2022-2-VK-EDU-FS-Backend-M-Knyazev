from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import render


@require_GET
def chat_list(request):
    chats = [1, 2, 3, 4, 5, 6]
    return JsonResponse({'chats': chats})


@require_GET
def show_chat(request, chat_id):
    return JsonResponse({'messages': [chat_id, chat_id + 1, chat_id + 2]})


@require_POST
def create_chat(request):
    name = request.POST['name']
    print(name) 
    resp = JsonResponse({'chat' : name})
    return resp


@require_GET
def show_start_menu(request):
    return render(request, 'chats/index.html')
