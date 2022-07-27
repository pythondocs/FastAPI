from pydantic import BaseModel

class AdminUser(BaseModel):
    name:str
    mobile:str
    email:str
    password:str

class LoginUser(BaseModel):
    email:str
    password:str

class UpdateAdmin(BaseModel):
    id: int
    name:str
    mobile:str
    email:str

class DeleteAdmin(BaseModel):
    user_id:int

class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
