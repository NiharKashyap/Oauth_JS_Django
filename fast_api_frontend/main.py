import requests
from credentials.constants import GOOGLE_CLIENT_ID 

from fastapi import FastAPI, Request, Response, Header
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

templates = Jinja2Templates(directory="templates")

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )



@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("test.html", {'request':request})

@app.get("/login/{provider}")
def login(provider):
    return RedirectResponse("https://127.0.0.1:8000/login/" + provider)
    
@app.get("/redirect/{provider}")
def redirect(provider, request:Request, code:str):
    print("Provider ", provider)
    print("Code", code)
    res = requests.get("https://127.0.0.1:8000/redirect/" + provider + "?code=" + code, verify=False)
    res = res.json()
    print(res.keys())
    
    if 'Error' in res.keys():
        print('Error', res['Error'])
        error=res['Error']
        token='None'
    else:
        error='None'
        token = res['token']
    return templates.TemplateResponse("redirect.html", {'request':request, 'token':token, 'error':error})

@app.get("/access/")
def access(request:Request, Authorization: str | None = Header(None)):
    print("Extered", Authorization)
    authmeth, auth = Authorization.split(" ", 1)
    headers = {'Authorization': 'Bearer ' + auth}
    res = requests.get("https://127.0.0.1:8000/access/", headers=headers, verify=False)
    print(res.json())
    return JSONResponse(res.json())
    # return templates.TemplateResponse("restricted.html", {'request':request})
