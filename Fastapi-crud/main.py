from fastapi import FastAPI
# from blog.apis import router as AdminRoute
from tortoise.contrib.fastapi import register_tortoise

app=FastAPI()
# app.include_router(AdminRoute.router)

register_tortoise(
    app,
    db_url='mysql://root@localhost:3306/mydb',
    modules={'models': ['blog.apis.models']},
    generate_schemas=True,
    add_exception_handlers=True
)