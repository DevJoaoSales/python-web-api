from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Configurar o Jinja2 para templates
templates = Jinja2Templates(directory='templates')

@app.get('/home', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})
