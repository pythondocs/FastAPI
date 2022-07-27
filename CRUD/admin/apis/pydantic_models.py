import datetime
import email
import imp
from pydantic import BaseModel
import uuid
from typing import List, Optional

class Addsong(BaseModel):
    song_name:str

class AdminUser(BaseModel):
    fname:str
    mobile:str
    email:str
    password:str
