from fastapi import APIRouter
from .models import *
from blog.apis.pydantic_models import AdminUser, LoginUser, Token, UpdateAdmin, DeleteAdmin
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

@router.post("/create_user/")
async def create_user(data:AdminUser):
    try:    
        try:  # Email validation
                valid = validate_email(data.email)
        except EmailNotValidError as e:
            return {"status": False, "message": "invalid email id"}
        if len(data.mobile) != 10:
                # mobile number validation
            return {"status": False, "message": "invalid number"}
        if await Admin.exists(mobile=data.mobile):
                return {"status": False, "message": "This number already register"}
        elif await Admin.exists(email=data.email):
                return {"status": False, "message": "This email id is already registered"}
        adduser= await Admin.create(name=data.name, mobile=data.mobile, email=data.email, password=get_password_hash(data.password))
        # return{"status": True, "message": "ok"} 
        return JSONResponse({
                "status": True,
                "message": "Registered successfully"})
    except Exception as e:
        return JSONResponse({
            "status": False,
            "message": str(e)})

@manager.user_loader()
async def load_user(email: str):
    if await Admin.exists(email=email):
        user = await Admin.get(email=email)
        return user

@router.post('/user_login/', )
async def login(data: LoginUser,
                #_=Depends(get_current_user)
                ):
    email = data.email
    user = await load_user(email)
    if not user:
        return JSONResponse({'status': False, 'message': 'User not Registered'}, status_code=403)
    elif not verify_password(data.password, user.password):
        return JSONResponse({'status': False, 'message': 'Invalid password'}, status_code=403)
    access_token = manager.create_access_token(
        data={'sub': jsonable_encoder(user.email), "name": jsonable_encoder(user.name), "mobile": jsonable_encoder(user.mobile)}  # Login time
        )
    '''test  current user'''
    new_dict = jsonable_encoder(user)
    new_dict.update({"access_token": access_token})
    res = Token(access_token=access_token, token_type='bearer')
    return res
    
@router.get("/all_user/")
async def read_user():
    alluser = await Admin.all()
    return alluser

@router.put("/update_user/")
async def update_user(data:UpdateAdmin):
    if await Admin.exists(id=data.id):
        updateuser=await Admin.filter(id=data.id).update(name=data.name, email=data.email, mobile=data.mobile)
        return JSONResponse({
        "status": True,
        "message": "Updated successfully"})

@router.delete("/delete_user/")
async def delete_user(data:DeleteAdmin):
        deleteuser=await Admin.filter(id=data.user_id).delete()
        return JSONResponse({
        "status": True,
        "message": "Deleted successfully"})


