from pydantic import BaseModel

class HrUser(BaseModel):
    name:str
    email:str
    password:str