from django.views.decorators.http import require_GET
from django.http import JsonResponse

@require_GET
def show_settings(request):
    return JsonResponse({'settings': {'1' : [], '2': [], '3' : []}})