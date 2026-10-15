from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.databaseproject.db import Base

class Film(Base):
    __tablename__ = "film"

    film_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str] = mapped_column(String)