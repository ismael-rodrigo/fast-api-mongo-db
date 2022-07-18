

from pydantic import BaseModel


class RefreshToken(BaseModel):
    refresh:str


class LoginToken(BaseModel):
    username:str
    password:str

    class Config:
        orm_mode = True