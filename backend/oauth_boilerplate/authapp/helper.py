import requests
from os import environ
from .constants import FACEBOOK_CLIENT_ID, FACEBOOK_REDIRECT_URI, FACEBOOK_SECRET


def exchange_code_google(code):
    data = {
        "client_id": environ['GOOGLE_CLIENT_ID'],
        "client_secret":environ['GOOGLE_CLIENT_SECRET'],
        "code":code,
        "grant_type":"authorization_code",
        "redirect_uri":"https://127.0.0.1:8000/google/redirect",
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    response = requests.post("https://oauth2.googleapis.com/token", data=data, headers=headers)
    credentials = response.json()
    access_token = credentials["access_token"]
    response = requests.get("https://www.googleapis.com/oauth2/v1/userinfo?alt=json", headers={
        "Authorization": "Bearer %s" % access_token
    })
    user = response.json()
    return(user)


def exchange_code_fb(code):
    
    response = requests.get("https://graph.facebook.com/v12.0/oauth/access_token?" + FACEBOOK_CLIENT_ID + FACEBOOK_REDIRECT_URI + "client_secret="+ FACEBOOK_SECRET + "&code=" + str(code))
    print(response.json())
    credentials = response.json()
    access_token = credentials["access_token"]
    response = requests.get("https://graph.facebook.com/me?fields=id&access_token=" + str(access_token))
    response_json = response.json()
    response = requests.get("https://graph.facebook.com/" + str(response_json['id']) + "?fields=id,name,email&access_token=" + str(access_token))
    user = response.json()
    return(user)