from fastapi import APIRouter
from .models import *
from hrm.app.pydantic_models import HrUser
from fastapi_login import LoginManager 
from passlib.context import CryptContext
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from email_validator import validate_email, EmailNotValidError

router=APIRouter()

SECRET = 'your-secret-key'
manager = LoginManager(SECRET, token_url='/user_login/')
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
def get_password_hash(password):
    return pwd_context.hash(password)

@router.post("/create/")
async def create(data:HrUser):
    try:    
        try:  # Email validation
                valid = validate_email(data.email)
        except EmailNotValidError as e:
            return {"status": False, "message": "invalid email id"}
        if await HrAdmin.exists(email=data.email):
                return {"status": False, "message": "This email id is already registered"}
        adduser= await HrAdmin.create(name=data.name, email=data.email, password=get_password_hash(data.password))
        return JSONResponse({
                "status": True,
                "message": "Registered successfully"})
    except Exception as e:
        return JSONResponse({
            "status": False,
            "message": str(e)})