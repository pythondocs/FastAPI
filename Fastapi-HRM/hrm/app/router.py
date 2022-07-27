from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from .models import *
from fastapi_login import LoginManager 
from passlib.context import CryptContext
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from email_validator import validate_email, EmailNotValidError


router=APIRouter()
templates = Jinja2Templates(directory="hrm/app/templates")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
def get_password_hash(password):
    return pwd_context.hash(password)

@router.get("/", response_class=HTMLResponse)
async def index(request:Request):
    return templates.TemplateResponse("sign-in.html", {"request": request})

@router.post("/sign-up/", response_class=HTMLResponse)
async def create_user(request:Request, 
                 name:str=Form(...),
                 email:str=Form(...),
                 password:str=Form(...)):
    if "_messages" in request.session:
            print(request.session["_messages"][0]['username'])
            email = request.session["_messages"][0]['username']
    else:
        user_obj = await HrAdmin.create(email=email, name=name, password= get_password_hash(password))
    return templates.TemplateResponse("sign-up.html", {"request": request})

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request:Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@router.get("/viewstudents", response_class=HTMLResponse)
async def viewstudents(request:Request):
    return templates.TemplateResponse("viewstudents.html", {"request": request})

@router.get("/courses", response_class=HTMLResponse)
async def courses(request:Request):
    return templates.TemplateResponse("courses.html", {"request": request})

@router.get("/profile", response_class=HTMLResponse)
async def profile(request:Request):
    return templates.TemplateResponse("profile.html", {"request": request})
