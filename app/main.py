from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from .models import Base
from .database import engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Setup templates
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/api/health")
def health_check():
    return {"status": "ok", "app": "SeeQoL"}

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
