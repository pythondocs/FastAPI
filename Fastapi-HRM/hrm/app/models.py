from tortoise.models import Model
from tortoise import fields 


class HrAdmin(Model):
    id = fields.IntField(pk=True)
    name= fields.CharField(100)
    email= fields.CharField(100)
    password= fields.TextField()
