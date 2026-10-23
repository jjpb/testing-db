from sqlalchemy import String, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from decimal import Decimal
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .category import Category

from app.core.db import Base

class Film(Base):
    __tablename__ = "film"

    film_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str] = mapped_column(String)
    rental_rate: Mapped[Decimal] = mapped_column(Numeric)

    categories: Mapped[List["Category"]] = relationship(
        secondary="film_category",
        back_populates="films"
    )
    
