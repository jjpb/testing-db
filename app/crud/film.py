from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.film import Film
from app.models.category import Category
from app.models.filmcategory import FilmCategory

async def get_films(
    db: AsyncSession,
    skip: int = 0,
    limit: int = 10
) -> list[Film]:
    result = await db.execute(select(Film).offset(skip).limit(limit))
    return list(result.scalars().all())

async def get_home_films(
    db: AsyncSession,
    skip: int = 0,
    limit: int = 10
) -> list[Film]:

    result = await db.execute(
        select(
            Film.film_id,
            Film.title,
            Film.rental_rate,
            func.array_agg(Category.name).label("category_name")
        )
        .join(FilmCategory, Film.film_id == FilmCategory.film_id)
        .join(Category, Category.category_id == FilmCategory.category_id)
        .group_by(Film.film_id)
        .order_by(Film.film_id.asc())
        .limit(limit)
        .offset(skip)
    )

    return list(result.mappings().all())