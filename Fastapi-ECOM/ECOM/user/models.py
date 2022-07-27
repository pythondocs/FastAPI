from tortoise import Model
from tortoise import fields
class User(Model):
    id= fields.UUIDField(pk=True)
    name=fields.CharField(100)
    email= fields.CharField(50, unique=True)
    password=fields.CharField(100)