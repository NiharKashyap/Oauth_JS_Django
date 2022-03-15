from logging import raiseExceptions
import jwt
import requests
from .models import User

def check_and_generate(user, provider):
    
    try:
        old_user = User.objects.get(social_id=user['id'])
        verify = verify_access_token(old_user.jwt)
        if verify==None:
            r=requests.post('https://127.0.0.1:8000/get_token', data=user, verify=False)
            old_user.jwt = r.json()['jwt']
            old_user.save()
        
        return old_user
            
    except:
        r=requests.post('https://127.0.0.1:8000/get_token', data=user, verify=False)
        r_json = r.json()
        user['jwt'] = r_json['jwt']
        new_user = User.objects.create_new_user(user, provider)
        print("Created new user")               
    
        return new_user

def verify_access_token(auth, request=None):
    """
    Verify if JWT exist in db
    """
    try:
        payload = jwt.decode(auth, "secret", algorithms=["HS256"])
        print('Payload ', payload)
        return User.objects.get(social_id=payload["id"])
    except Exception as e:
        # Signature has expired
        print('Exception ', str(e))
        return None