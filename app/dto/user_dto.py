from fastapi import FastAPI
from pydantic import BaseModel, EmailStr,Field
from typing import List
import uuid

from app.db.init_db import engine
from app.model.User_model import Base
from app.schemas.news_schema import NewsCategory

# Create tables
Base.metadata.create_all(bind=engine)

# -------------------
# Pydantic Schemas
# -------------------
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    categories: List[NewsCategory]
    languages: str

class UserRead(BaseModel):
    id: uuid.UUID
    name: str
    email: EmailStr
    phone: str
    categories: List[NewsCategory]
    languages: str

    class Config:
        from_attributes = True

