from msilib.schema import Directory
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from hrm.app import router as UserRoute
from hrm.app import apis as apiRoute
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware import Middleware

middleware = [
    Middleware(SessionMiddleware, secret_key='super-secret')
]

app=FastAPI()
app.include_router(UserRoute.router)
app.include_router(apiRoute.router, prefix = "/apis",tags = ["api"])    
app.mount("/static", StaticFiles(directory="hrm/static"), name="static")


register_tortoise(
    app,
    db_url='mysql://root@localhost:3306/hrmm',
    modules={'models': ['hrm.app.models']},
    generate_schemas=True,
    add_exception_handlers=True
)