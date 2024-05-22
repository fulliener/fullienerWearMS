import shutil
import uuid

import requests

from fastapi import FastAPI, Request, HTTPException, Depends, Form, UploadFile, File
from fastapi.staticfiles import StaticFiles

from sqlalchemy.orm import scoped_session
from starlette.middleware.cors import CORSMiddleware

from models import Good, get_session, engine, Base
from schemas import GoodSchema

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

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


def get_user(request: Request):
    response = requests.get("http://auth-service:8000/me",
                            headers={"Authorization": request.headers.get("Authorization", "None")})
    if response.status_code == 200:
        return response.json()
    raise HTTPException(
        status_code=401, detail="Unauthorized"
    )


@app.get("/", response_model=list[GoodSchema])
def get_all(db: scoped_session = Depends(get_session)):
    return db.query(Good).all()


@app.get("/{good_id}", response_model=GoodSchema)
def get_by_id(good_id: int, db: scoped_session = Depends(get_session)):
    if good := db.query(Good).filter(Good.id == good_id).first():
        return good
    raise HTTPException(
        status_code=404,
        detail="Good not found"
    )


@app.post("/", response_model=GoodSchema)
def create(request: Request,
           name: str = Form(),
           count: int = Form(),
           image: UploadFile = File(...),
           description: str | None = Form(),
           price: float = Form(),
           seller_vk_url: str | None = Form(),
           seller_tg_url: str | None = Form(),
           db: scoped_session = Depends(get_session)):
    user = get_user(request)
    photo_uuid = uuid.uuid4()
    filename = f"{photo_uuid}.{image.filename.split('.')[-1]}"
    with open(f"./static/{filename}", "w+b") as f:
        shutil.copyfileobj(image.file, f)
    good = Good(
        user_id=user["id"],
        name=name,
        count=count,
        image_url=f"/static/{filename}",
        description=description,
        price=price,
        seller_vk_url=seller_vk_url,
        seller_tg_url=seller_tg_url
    )
    db.add(good)
    db.commit()
    db.refresh(good)
    return good


@app.patch("/{good_id}", response_model=GoodSchema)
def update(request: Request,
           good_id: int,
           name: str | None = Form(None),
           count: int | None = Form(None),
           image: UploadFile | None = File(None),
           description: str | None = Form(None),
           price: float | None = Form(None),
           seller_vk_url: str | None = Form(None),
           seller_tg_url: str | None = Form(None),
           db: scoped_session = Depends(get_session)):
    user = get_user(request)
    if not (good := db.query(Good).filter(Good.id == good_id).first()):
        raise HTTPException(
            status_code=404,
            detail="Good not found"
        )
    if name:
        good.name = name
    if count:
        good.count = count
    if description:
        good.description = description
    if price:
        good.price = price
    if seller_vk_url:
        good.seller_vk_url = seller_vk_url
    if seller_tg_url:
        good.seller_tg_url = seller_tg_url
    if image:
        photo_uuid = uuid.uuid4()
        filename = f"{photo_uuid}.{image.filename.split('.')[-1]}"
        with open(f"./static/{filename}", "w+b") as f:
            shutil.copyfileobj(image.file, f)
        good.image_url = f"/static/{filename}"
    db.add(good)
    db.commit()
    db.refresh(good)
    return good
