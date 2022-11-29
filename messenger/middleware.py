from django.shortcuts import redirect
from django.conf import settings

EXEMPT_URLS = [settings.LOGIN_URL.lstrip('/')]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [url for url in settings.LOGIN_EXEMPT_URLS]

class LoginRequired(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            return None
        for path in EXEMPT_URLS:
            print(path, request.path.startswith(path))
            if request.path.startswith(path):
                return None 
        # if request.path.startswith('/login/') or request.path.startswith('/social-auth/') or request.path.startswith('/admin/'):
        #     return None
        return redirect('login')
