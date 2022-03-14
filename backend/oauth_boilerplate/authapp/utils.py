from logging import raiseExceptions
import jwt
import requests
from .models import User

def check_and_generate(user, provider):
    
    try:
        user = User.objects.get(social_id=user['id'])
    except:
        r=requests.post('https://127.0.0.1:8000/get_token', data=user, verify=False)
        r_json = r.json()
        user['jwt'] = r_json['jwt']
        user = User.objects.create_new_user(user, provider)
        print("Created new user")               
    
    return user