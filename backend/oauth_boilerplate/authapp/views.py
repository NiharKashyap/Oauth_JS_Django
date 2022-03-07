#TODO: 1. Create custom authentication based on this url: https://stackoverflow.com/questions/32844784/django-rest-framework-custom-authentication
#TODO: 2. Reference custom auth repo: https://github.com/anu37/DjangoCustomAuthentication/blob/master/customauth/auth.py 

from .models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import redirect, render
from .providers import login_handler, exchange_code_handler,refresh_token_google
from rest_framework.decorators import api_view
import requests

from .serializers import UserSerializer
from django.contrib.auth import logout
from django.http import  HttpResponse, JsonResponse
import jwt
from .utils import check_and_generate

from .auth import CustomAuthentication


class GetTokenView(APIView):
    def post(self, request):
        """
        Create jwt token from user social id and email
        """
    
        id = request.data['id']
        fname = request.data['email']
        
        encoded_jwt = jwt.encode({"id":id, "fname":fname}, "secret", algorithm="HS256")
        jwt_dict = {'jwt':encoded_jwt}
        return JsonResponse(jwt_dict)

class LoginView(APIView):
    """
    Login API
    """
    
    def get(self, request, provider):
        print('000')
        url = login_handler(provider)
        print(url)
        # return Response(url)
        return redirect(url)
    
class RedirectView(APIView):
    """
    Redirect API
    """
    def get(self, request, provider):
        print('111')
        code = request.GET.get('code')
        user = exchange_code_handler(code, provider)
        token = check_and_generate(user, provider)
    
        user = UserSerializer(token)
        response_data = user.data
        print(response_data)
        return Response({"User":response_data, "token":response_data['jwt']})

class RestrictedAccessView(APIView):
    
    authentication_classes = [CustomAuthentication]
    
    
    def get(self, request):
        user = User.objects.filter(id = request.user.id).first()
        serializer = UserSerializer(user)
        try:    
            return Response(serializer.data)
        except Exception as err:
            return Response(
                {
                    "error": str(err)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
class TestTokenView(APIView):
    def get(self, request):
            import requests
            access_token = request.META.get('HTTP_AUTHORIZATION')
            access_token= access_token.split(' ')[1]
            
            response = requests.get("https://www.googleapis.com/oauth2/v1/userinfo?alt=json", headers={"Authorization": "Bearer %s" % access_token})
            
            response_json = response.json()
            
            if 'error' in response_json:
                if response.json()['error']['status']=='UNAUTHENTICATED':
                    try:
                        user = User.objects.get(auth_token=access_token)
                        id=user.id
                        refresh_token=user.refresh_token
                        refresh_token_google(id, refresh_token)
                    except Exception as e:
                        return Response({'error': str(e)})
            return Response({'Response':response_json})

@api_view(['GET'])
def logout_view(request):
    logout(request)
    return request('/')
    # Redirect to a success page.


@api_view(['GET'])
def test_db(request):
    obj = User.objects.latest()
    print(obj)
    return Response('Done')
    # Redirect to a success page.

@api_view(['GET'])
def get_code(request):
    code = request.GET.get('code')
    print(code)
    return Response('Success')
        