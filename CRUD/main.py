from fastapi import FastAPI
from admin.apis import routers as AdminRoute
from tortoise import fields
from tortoise.contrib.fastapi import register_tortoise

app=FastAPI()
app.include_router(AdminRoute.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}

register_tortoise(
    app,
    db_url='mysql://root@localhost:3306/mydb',
    modules={'models': ['admin.apis.models']},
    generate_schemas=True,
    add_exception_handlers=True
)