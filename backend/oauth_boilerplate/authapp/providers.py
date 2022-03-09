'''
List of Providers:

1. Google
2. Facebook
3. Discord
4. Linkedin

'''


import requests
from os import environ
from .models import User

from .constants import (GOOGLE_ACCESS_TYPE, GOOGLE_AUTH_URL,GOOGLE_CLIENT_SECRET, GOOGLE_CLIENT_ID, GOOGLE_REDIRECT_URI, GOOGLE_RESPONSE_TYPE, GOOGLE_SCOPE, 
                        FACEBOOK_AUTH_URL, FACEBOOK_CLIENT_ID, FACEBOOK_REDIRECT_URI, FACEBOOK_SCOPE, FACEBOOK_STATE, FACEBOOK_SECRET,
                        DISCORD_CLIENT_SECRET, DISCORD_AUTH_URL, DISCORD_CLIENT_ID, DISCORD_REDIRECT_URL, DISCORD_SCOPE, LINKEDIN_CLIENT_ID,
                        LINKEDIN_AUTH_URL, LINKEDIN_REDIRECT_URI, LINKEDIN_RESPONSE_TYPE, LINKEDIN_SCOPE, LINKEDIN_SECRET
                        )

class CodeHandler:
    def __init__(self, id, secret, code=None, redirect=None, scope=None):
        self.client_id = id
        self.client_secret = secret
        self.code=code
        self.redirect_uri = redirect
        self.scope = scope
        
    def get_token(self, url):
        data = {
        "client_id": self.client_id ,
        "client_secret":self.client_secret,
        "code":self.code,
        "grant_type":"authorization_code",
        "redirect_uri":self.redirect_uri,
        "scope":self.scope
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        response = requests.post(url, data=data, headers=headers)
        return response
    
    def refresh_token(self,url, refresh_token):
        data = {
        
        "client_id": self.client_id ,
        "client_secret":self.client_secret,
        "grant_type":"refresh_token",
        "refresh_token":refresh_token,
        }
        
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    
        response = requests.post(url, data=data, headers=headers)
        credentials = response.json()
        
        if "error" in credentials:
            return "Error"
        else:
            print("Refreshed creds\n",credentials)
            return credentials
    

def login_handler(provider):
    if provider=="fb":
        url = FACEBOOK_AUTH_URL + FACEBOOK_CLIENT_ID + FACEBOOK_REDIRECT_URI + FACEBOOK_STATE + FACEBOOK_SCOPE
    elif provider=="discord":
        url = DISCORD_AUTH_URL + 'client_id=' + DISCORD_CLIENT_ID + "&redirect_uri=" + DISCORD_REDIRECT_URL + "&response_type=code&scope=" + DISCORD_SCOPE
    elif provider=="google":
        url = GOOGLE_AUTH_URL + "?client_id=" + GOOGLE_CLIENT_ID + "&redirect_uri=" + GOOGLE_REDIRECT_URI + "&access_type=" + GOOGLE_ACCESS_TYPE + "&response_type=" + GOOGLE_RESPONSE_TYPE + "&scope=" + GOOGLE_SCOPE
    elif provider=="linkedin":
        url = LINKEDIN_AUTH_URL + 'response_type=' + LINKEDIN_RESPONSE_TYPE + '&client_id=' + LINKEDIN_CLIENT_ID + '&redirect_uri=' + LINKEDIN_REDIRECT_URI + '&state=foobar' + '&scope=' + LINKEDIN_SCOPE

    return url


def exchange_code_handler(code, provider):
    if provider=="fb":
        user = exchange_code_fb(code)
    elif provider=="discord":
        user = exchange_code_discord(code)
    elif provider=="google":
        user = exchange_code_google(code)
    elif provider=='linkedin':
        user = exchange_code_linkedin(code)    
    
    return user
        
    

def exchange_code_google(code):
    
    google_exchange = CodeHandler(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, code, GOOGLE_REDIRECT_URI)
    response = google_exchange.get_token("https://oauth2.googleapis.com/token")
    credentials = response.json()
    access_token = credentials["access_token"]
    print(credentials)
    response = requests.get("https://www.googleapis.com/oauth2/v1/userinfo?alt=json", headers={
        "Authorization": "Bearer %s" % access_token
    })
    user = response.json()
    print(user)
    user['auth_token'] = credentials["access_token"]
    user['refresh_token'] = credentials['refresh_token']
    user['first_name'] = user.pop('given_name')
    user['last_name'] = user.pop('family_name')
    return(user)


def exchange_code_fb(code):
    
    response = requests.get("https://graph.facebook.com/v12.0/oauth/access_token?" + FACEBOOK_CLIENT_ID + FACEBOOK_REDIRECT_URI + "client_secret="+ FACEBOOK_SECRET + "&code=" + str(code))
    credentials = response.json()
    access_token = credentials["access_token"]
    response = requests.get("https://graph.facebook.com/me?fields=id&access_token=" + str(access_token))
    response_json = response.json()
    response = requests.get("https://graph.facebook.com/" + str(response_json['id']) + "?fields=id,name,email,first_name,last_name&access_token=" + str(access_token))
    user = response.json()
    user['auth_token'] = credentials["access_token"]
    user['refresh_token'] = ''
    
    return(user)

def exchange_code_discord(code):
    handler = CodeHandler(DISCORD_CLIENT_ID, DISCORD_CLIENT_SECRET, code, "https://127.0.0.1:5500/frontend/redirect.html", DISCORD_SCOPE)
    response = handler.get_token("https://discord.com/api/oauth2/token")
    credentials = response.json()
    access_token = credentials['access_token']
    response = requests.get("https://discord.com/api/v6/users/@me", headers={
        "Authorization": "Bearer %s" % access_token
    })
    
    user = response.json()
    user['first_name'] = user['username']
    user['last_name'] = ''
    user['auth_token'] = credentials["access_token"]
    user['refresh_token'] = credentials['refresh_token']
    return(user)

def exchange_code_linkedin(code):
    
    handler = CodeHandler(LINKEDIN_CLIENT_ID, LINKEDIN_SECRET, code, LINKEDIN_REDIRECT_URI)
    
    response = handler.get_token("https://www.linkedin.com/oauth/v2/accessToken")
    credentials = response.json()
    access_token = credentials['access_token']
    
    response = requests.get("https://api.linkedin.com/v2/me", headers={
        "Authorization": "Bearer %s" % access_token
    })
    
    user = response.json()
    user_dict = {}
    user_dict['first_name'] = user['localizedFirstName']
    user_dict['last_name'] = user['localizedLastName']
    user_dict['id'] = user['id']
    user_api = requests.get("https://api.linkedin.com/v2/emailAddress?q=members&projection=(elements*(handle~))", headers={"Authorization": "Bearer %s" % access_token})
    user_email = user_api.json()
    user_dict['email'] = user_email['elements'][0]['handle~']['emailAddress']
    
    user_dict['auth_token'] = credentials["access_token"]
    user_dict['refresh_token'] = ''
    return user_dict


def refresh_token_google(id, refresh_token):
    handler = CodeHandler(id=GOOGLE_CLIENT_ID, secret=GOOGLE_CLIENT_SECRET)
    response = handler.refresh_token("https://oauth2.googleapis.com/token", refresh_token)
    User.objects.filter(id=id).update(auth_token=response['access_token'])

def refresh_token_discord(id, refresh_token):
    handler = CodeHandler(id=DISCORD_CLIENT_ID, secret=DISCORD_CLIENT_SECRET)
    response = handler.refresh_token("https://discord.com/api/oauth2/token", refresh_token)
    User.objects.filter(id=id).update(auth_token=response['access_token'])

def refresh_token_fb(id):
    user = User.objects.get(id=id)
    response = requests.get("https://graph.facebook.com/v12.0/oauth/access_token?" + "grant_type=fb_exchange_token" + "&client_id=" + FACEBOOK_CLIENT_ID + "&client_secret=" + FACEBOOK_SECRET + "&fb_exchange_token=" + user.auth_token)
    user.auth_token = response['access_token']
    
    