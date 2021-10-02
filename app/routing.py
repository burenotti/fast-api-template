from fastapi import APIRouter


global_router = APIRouter()

'''
This file is used to include routers from your modules like this:

from app import (
    auth
)

global_router.include_router(auth.router)
'''
