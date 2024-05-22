from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse

from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from sqlalchemy.orm import scoped_session
from starlette.middleware.cors import CORSMiddleware

from security import get_password_hash, verify_password
from models import User, get_session, engine, Base
from schemas import UserSchema, UserCreateReq, UserUpdateReq, UserLogin, AccessToken

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event('startup')
def make_db():
    Base.metadata.create_all(engine)


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


@app.post('/login')
def login(data: UserLogin, authorize: AuthJWT = Depends(), db: scoped_session = Depends(get_session)):
    user = db.query(User).filter(User.username == data.username).first()
    if not user:
        print(1)
        raise HTTPException(status_code=401, detail="Bad username or password")

    if not verify_password(data.password, user.password):
        print(2)
        raise HTTPException(status_code=401, detail="Bad username or password")

    access_token = authorize.create_access_token(subject=user.id)
    return {"access_token": access_token}


@app.post('/register')
def register(user: UserCreateReq, authorize: AuthJWT = Depends(), db: scoped_session = Depends(get_session)):
    if db.query(User).filter(User.username == user.username).first():
        return HTTPException(
            status_code=400, detail="Username already registered"
        )
    user.password = get_password_hash(user.password)
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    access_token = authorize.create_access_token(subject=db_user.id)
    return {"access_token": access_token}


@app.get('/me', response_model=UserSchema)
def user(authorize: AuthJWT = Depends(), db: scoped_session = Depends(get_session)):
    authorize.jwt_required()
    subject = authorize.get_jwt_subject()
    return db.query(User).filter(User.id == int(subject)).first()


@app.patch("/", response_model=UserSchema)
def update_user(user: UserUpdateReq, authorize: AuthJWT = Depends(), db: scoped_session = Depends(get_session)):
    authorize.jwt_required()
    subject = authorize.get_jwt_subject()
    db_user = db.query(User).filter(User.id == int(subject)).first()
    if user.first_name:
        db_user.first_name = user.first_name
    if user.last_name:
        db_user.last_name = user.last_name
    if user.email:
        db_user.email = user.email
    if user.username:
        db_user.username = user.username
    if user.password:
        db_user.password = get_password_hash(user.password)
    db.commit()
    db.refresh(db_user)
    return db_user
