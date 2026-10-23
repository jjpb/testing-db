from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.core.db import Base

class FilmCategory(Base):
    __tablename__ = "film_category"

    film_id: Mapped[int] = mapped_column(
        ForeignKey("film.film_id"), 
        primary_key=True
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey("category.category_id"), 
        primary_key=True
    )