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
templates = Jinja2Templates(directory="user/templates")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
def get_password_hash(password):
    return pwd_context.hash(password)

@router.post("/Create_User/", response_class=HTMLResponse)
async def create_user(request:Request, 
                 name:str=Form(...),
                 email:str=Form(...),
                 password:str=Form(...)):
    if "_messages" in request.session:
        print(request.session["_messages"][0]['username'])
        email = request.session["_messages"][0]['username']
    else:
        user_obj = await User.create(email=email,name=name
                                     ,password= get_password_hash(password))
    return templates.TemplateResponse("customerregistration.html", {"request": request})
