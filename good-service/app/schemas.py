from pydantic import BaseModel


class GoodSchema(BaseModel):
    id: int
    name: str
    count: int
    image_url: str
    description: str | None = None
    price: float
    seller_vk_url: str | None = None
    seller_tg_url: str | None = None

    class Config:
        orm_mode = True


class GoodDeleteRes(BaseModel):
    id: int
