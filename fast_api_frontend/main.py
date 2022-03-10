
import requests
from credentials.constants import GOOGLE_CLIENT_ID 

from fastapi import FastAPI, Request, Response, Header
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")



app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("test.html", {'request':request})

@app.get("/login/")
def login():
    return RedirectResponse("https://accounts.google.com/o/oauth2/v2/auth?client_id=" + GOOGLE_CLIENT_ID + "&redirect_uri=https://127.0.0.1:5500/redirect/google&access_type=offline&response_type=code&scope=https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email")

@app.get("/redirect/{provider}")
def redirect(provider, request:Request, code:str):
    print("Provider ", provider)
    print("Code", code)
    res = requests.get("https://127.0.0.1:8000/redirect/" + provider + "?code=" + code, verify=False)
    print(res.json()['token'])
    token = res.json()['token']
    return templates.TemplateResponse("redirect.html", {'request':request, 'token':token})

@app.get("/access/")
def access(request:Request, Authorization: str | None = Header(None)):
    print("Extered", Authorization)
    authmeth, auth = Authorization.split(" ", 1)
    headers = {'Authorization': 'Bearer ' + auth}
    res = requests.get("https://127.0.0.1:8000/access/", headers=headers, verify=False)
    print(res.json())
    return JSONResponse(res.json())
    # return templates.TemplateResponse("restricted.html", {'request':request})
