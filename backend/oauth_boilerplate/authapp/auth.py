from .models import User
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

class CustomAuthentication(BaseAuthentication):

    def authenticate(self, request, **kwargs):
        """
        Authenticate user based on JWT
        """
        try:
            auth_header_value = request.META.get("HTTP_AUTHORIZATION")
            if auth_header_value:
                authmeth, auth = request.META["HTTP_AUTHORIZATION"].split(" ", 1)
                if not auth:
                    raise exceptions.AuthenticationFailed(detail="No auth token provided", code=None)
                if not authmeth.lower() == "bearer":
                    raise exceptions.AuthenticationFailed(detail="Improperly configued auth token", code=None)
                token = CustomAuthentication.verify_access_token(request, auth)
                if token==None:
                    raise exceptions.PermissionDenied(detail=None, code=None)
                else: 
                    return (token, None)
            else:
                raise exceptions.AuthenticationFailed(detail="No auth token provided", code=None)
        except Exception as e:
            raise e

    @staticmethod
    def verify_access_token(request, auth):
        """
        Verify if JWT exist in db
        """
        if User.objects.filter(jwt=auth).exists():
            user = User.objects.get(jwt=auth)
            return user
        else:
            return None