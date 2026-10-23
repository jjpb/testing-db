from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from film import Film

from app.core.db import Base

class Category(Base):
    __tablename__ = "category"

    category_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    films: Mapped[List["Film"]] = relationship(
        secondary="film_category",
        back_populates="categories"
    )
