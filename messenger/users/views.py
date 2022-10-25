# from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse, HttpResponse
# from .models import User


@require_POST
def create_user(request):
    user_name = request.POST['name']
    # User(name=user_name).save()
    return HttpResponse(status=200)


@require_GET
def show_users(request):
    names = []
    ids = []
    # for i in User.objects.all():
    #     names.append(i.name)
    #     ids.append(i.pk)
    return JsonResponse({'users': names, 'pk': ids})
