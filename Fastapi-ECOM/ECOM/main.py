from fastapi import FastAPI
# from starlette.middleware.sessions import SessionMiddleware
# from starlette.middleware import Middleware
from tortoise.contrib.fastapi import register_tortoise
from user import route as UserRoute
from fastapi.staticfiles import StaticFiles


# middleware = [
#     Middleware(SessionMiddleware, secret_key='super-secret')
# ]

app=FastAPI()
app.include_router(UserRoute.router)

app.mount("/static", StaticFiles(directory="static"), name="static")



register_tortoise(
    app,
    db_url='mysql://root@localhost:3306/ecomm',
    modules={'models': ['user.models']},
    generate_schemas=True,
    add_exception_handlers=True
)