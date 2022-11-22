from django.shortcuts import redirect


class LoginRequired(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path.startswith('/login/') or request.path.startswith('/social-auth/') or request.path.startswith('/admin/'):
            return None
        if request.user.is_authenticated:
            return None
        return redirect('login')
