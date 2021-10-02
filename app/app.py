import fastapi
from .routing import global_router

app = fastapi.FastAPI()

app.include_router(global_router)
