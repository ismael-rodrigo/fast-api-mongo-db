from datetime import date
from typing import List 
from fastapi import APIRouter, Body, Depends, FastAPI, Security
from pydantic import BaseModel 
from core.auth.hash_provider import get_password_hash, verify_password

import json
from ..schemas.user_schema import ShowUser, User

from core.database.database import db

router = APIRouter()


@router.post('/user' ,response_model=ShowUser , status_code=201)
async def create_user(request:User = Body(...)):
    user = request
    user.password = get_password_hash(user.password)

    users_collection = db['users']
    new_user =   users_collection.insert_one(user.dict())
    user_created =  users_collection.find_one({'_id': new_user.inserted_id})
    
    return user_created


@router.get('/user',response_model=List[ShowUser])
async def get_users():
    users_collection = db['users']
    users = list(users_collection.find({}))
    return users




