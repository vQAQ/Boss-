from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, redirect


class UserMW(MiddlewareMixin):
    def process_request(self, request):
        path = request.path_info
        if path == '/myApp/login/' or path == '/myApp/registry/':
            return None
        else:
            if not request.session.get('username'):
                return redirect('login')
        return None

    def process_view(self, request, callback, callback_arge, callback_kwargs):
        return None

    def process_response(self, request, response):
        return response
