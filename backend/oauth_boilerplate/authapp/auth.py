from .models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
import jwt
from .utils import verify_access_token
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
                token = verify_access_token(auth, request)
                if token==None:
                    raise exceptions.PermissionDenied(detail=None, code=None)
                else: 
                    return (token, None)
            else:
                raise exceptions.AuthenticationFailed(detail="No auth token provided", code=None)
        except Exception as e:
            raise e