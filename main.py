from fastapi import FastAPI, Header, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")
 

@app.get("/", response_class = HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("welcome.html", {
        "request": request,
        "title": "Welcome"
    })

@app.get("/login", response_class = HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("auth/login.html", {
        "request": request,
        "title": "Welcome"
    })
