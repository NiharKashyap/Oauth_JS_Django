from rest_framework.exceptions import AuthenticationFailed
import requests
from django.http import HttpResponse
from django.urls import reverse

class TokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        allowed_url = ['/login/', '/verify/', '/register/', '/']
        
        if request.path not in allowed_url:
        
            if request.META.get('HTTP_AUTHORIZATION') is not None:
                token = request.META.get('HTTP_AUTHORIZATION')
                token = token.split(' ')
                url = "http://127.0.0.1:8000/verify/"
                headers = {"Authorization": "Token " + token[1]}
                res = requests.get(url, headers=headers)
                if res.status_code!=200:
                    return HttpResponse("Auth token invalid", status=400)
            else:
                return HttpResponse("No Auth token provided", status=400)
        
        response = self.get_response(request)
        return response
    