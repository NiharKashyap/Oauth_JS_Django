# class UserCookieMiddleWare:
#     """
#     Middleware to set user cookie
#     If user is authenticated and there is no cookie, set the cookie,
#     If the user is not authenticated and the cookie remains, delete it
#     """

#     def process_response(self, request, response):
#         #if user and no cookie, set cookie
#         if request.user.is_authenticated() and not request.COOKIES.get('user'):
#             response.set_cookie("user", 'Hello Cookie')
#         elif not request.user.is_authenticated() and request.COOKIES.get('user'):
#             #else if if no user and cookie remove user cookie, logout
#             response.delete_cookie("user")
#         return response
    
from rest_framework.response import Response
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
    
class corsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = "*"
        
        print('In Cors middleware')
        return response