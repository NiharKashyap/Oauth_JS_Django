from typing import Optional
import requests
from django.shortcuts import redirect

from .constants import GOOGLE_CLIENT_ID 

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")



app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("test.html", {'request':request})

@app.get("login/")
def login():
    return redirect("https://accounts.google.com/o/oauth2/v2/auth?client_id=" + GOOGLE_CLIENT_ID + "&redirect_uri=https://127.0.0.1:5500/redirect/google&access_type=offline&response_type=code&scope=https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email")

@app.get("redirect/<str:provider>")
def redirect(provider):
    
    requests.get("https:127.0.0.1:8000/redirect/" + provider + "")