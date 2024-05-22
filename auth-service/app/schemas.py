from pydantic import BaseModel

from fastapi_jwt_auth import AuthJWT


class Settings(BaseModel):
    authjwt_secret_key: str = "secret"


@AuthJWT.load_config
def get_config():
    return Settings()


class UserCreateReq(BaseModel):
    first_name: str
    last_name: str
    email: str
    username: str
    password: str


class UserCreateRes(BaseModel):
    access_token: str


class UserUpdateReq(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    username: str | None = None
    password: str | None = None


class UserSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    username: str

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str
    password: str


class AccessToken(BaseModel):
    access_token: str
