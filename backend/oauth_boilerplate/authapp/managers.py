from django.contrib.auth.models import UserManager
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status

class UserSocialManager(UserManager):
    def create_new_user(self, user, provider):
        try:
            new_user = self.create(
                    username = user['first_name'] + user['last_name'] + "@" + provider,
                    first_name = user['first_name'],
                    last_name = user['last_name'],
                    social_id = user['id'],
                    provider=provider,
                    email = user['email'],
                    auth_token=user['auth_token'],
                    refresh_token=user['refresh_token'],
                    jwt = user['jwt'],
                    extra_data=user
                )
            return new_user
        except Exception as e:
            # print('EXception from ' + __file__, e)
            # raise e
            return e
            
            
