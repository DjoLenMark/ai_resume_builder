from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/resume", response_class=HTMLResponse)
def resume(request: Request,
           name: str = Form(...),
           profession: str = Form(...),
           education: str = Form(...),
           experience: str = Form(...),
           skills: str = Form(...),
           contacts: str = Form(...)):
    return templates.TemplateResponse("resume.html", {
        "request": request,
        "name": name,
        "profession": profession,
        "education": education,
        "experience": experience,
        "skills": skills,
        "contacts": contacts
    }) 