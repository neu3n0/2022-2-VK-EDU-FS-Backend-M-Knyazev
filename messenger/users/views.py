from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from messagesChat.models import Message
from chats.models import Chat
from .models import User


@require_POST
def create_user(request):
    if (not request.POST.get('username') and not request.POST.get('mobile')):
        return JsonResponse(
            {
                'error': 'username and mobile are necessary',
                'username': request.POST.get('username'),
                'mobile': request.POST.get('mobile')
            },
            status=400
        )
    user = User.objects.create(
        username=request.POST['username'],
        mobile=request.POST['mobile'],
        description=request.POST.get('description')
    )
    if request.POST.get('age') and request.POST.get('age') in range(7, 120):
        user.age = request.POST.get('age')
    return JsonResponse({
        'username': user.username,
        'age': user.age,
        'mobile': user.mobile,
        'description': user.description,
    })


@require_GET
def get_user_info(request, pk):
    user = get_object_or_404(User, pk=pk)
    return JsonResponse({
        'username': user.username,
        'id': user.pk,
        'age': user.age,
        'mobile': user.mobile,
        'description': user.description,
    })
