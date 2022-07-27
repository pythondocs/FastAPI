
TORTOISE_ORM = {
    "connections": {"default": "mysql://root@localhost:3306/test"},
    "apps": {
        "models": {
            "models": ["AddUser.models","aerich.models"],
            "default_connection": "default",
        },
    },
}