from functools import lru_cache
from typing import Generator

from sqlalchemy import Column, Integer, String, Float

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from base import Base

engine = create_engine("sqlite:///database.db")


@lru_cache
def create_session() -> scoped_session:
    session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
    return session


def get_session() -> Generator[scoped_session, None, None]:
    session = create_session()
    try:
        yield session
    finally:
        session.remove()


class Good(Base):
    """
    Good model
    """
    __tablename__ = "goods"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    name = Column(String)
    count = Column(Integer)
    image_url = Column(String)
    description = Column(String, nullable=True)
    price = Column(Float)
    seller_vk_url = Column(String, nullable=True)
    seller_tg_url = Column(String, nullable=True)

