from bson import ObjectId
from fastapi import Depends, HTTPException ,status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from core.database.database import db
from core.auth.token_provider import verify_access_token


oauth2_schema = OAuth2PasswordBearer(tokenUrl='auth/token')


def user_logged(token:str = Depends(oauth2_schema)):
    try:
        data = verify_access_token(token)
    except JWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED , detail='token invalid')

    user = db['users'].find_one({'_id':ObjectId(data)})
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED , detail='token invalid')    
    return user