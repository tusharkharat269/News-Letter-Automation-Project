from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import List
import uuid

from db.init_db import engine
from model.User_model import Base

# Create tables
Base.metadata.create_all(bind=engine)

# -------------------
# Pydantic Schemas
# -------------------
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    categories: List[str] = []
    languages: str

class UserRead(BaseModel):
    id: uuid.UUID
    name: str
    email: EmailStr
    phone: str
    categories: List[str]
    languages: str

    class Config:
        from_attributes = True

