from typing import List
from pydantic import BaseModel
from decouple import config

#
DEBUG = config('DEBUG',cast=bool)


#---CORS CONFIGS---
CORS_ORIGINS_DEBUG_TRUE = [
        '*',
    ]

CORS_ORIGINS_DEBUG_FALSE =  [
        "http://site-frontend.com",
        "https://site-frontend.com",
    ]


#---JWT CONFIGS---
ACCESS_EXPIRES_IN_MIN  = 10
REFRESH_EXPIRES_IN_MIN = 50


USERNAME_MONGO_DB = config('USERNAME_MONGO_DB')
PASSWORD_MONGO_DB = config('PASSWORD_MONGO_DB')
DATABASE_URL_MONGO_DB = config('DATABASE_URL_MONGO_DB')


class Settings(BaseModel):

    CORS_ORIGINS: List[str] = CORS_ORIGINS_DEBUG_FALSE if not DEBUG else CORS_ORIGINS_DEBUG_TRUE

    SECRET_KEY: str = config('SECRET_KEY')
    REFRESH_SECRET_KEY: str = config('REFRESH_SECRET_KEY')
    ALGORITHM: str = config('ALGORITHM')
    ACCESS_EXPIRES_IN_MIN: int = ACCESS_EXPIRES_IN_MIN
    REFRESH_EXPIRES_IN_MIN: int = REFRESH_EXPIRES_IN_MIN

    DATABASE_URL: str = f'mongodb+srv://{USERNAME_MONGO_DB}:{PASSWORD_MONGO_DB}@{DATABASE_URL_MONGO_DB}/?retryWrites=true&w=majority'


settings = Settings()



