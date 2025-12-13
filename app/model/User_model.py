from typing import List
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.dialects.postgresql import UUID,ARRAY,ENUM # If you're using PostgreSQL
from app.schemas.news_schema import NewsCategory
from enum import StrEnum

news_category_enum = ENUM(NewsCategory, name="news_category", create_type=True)


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(15), unique=True, nullable=False)

    categories: Mapped[list[NewsCategory]] = mapped_column(ARRAY(news_category_enum),nullable=False,default=[NewsCategory.HEALTH])
    languages: Mapped[str] = mapped_column(String(20))

    def __repr__(self) -> str:
        return (
            f"User(id={self.id!r}, name={self.name!r}, fullname={self.name!r}, "
            f"email={self.email!r}, phone={self.phone!r}, "
            f"categories={self.categories!r}, languages={self.languages!r})"
        )
