from functools import lru_cache
from typing import Generator

from sqlalchemy import Column, Integer, String, Boolean

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


class User(Base):
    """
    User model
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    username = Column(String, unique=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)
