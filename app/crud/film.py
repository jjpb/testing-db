from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.film import Film
from app.schemas.film import FilmRead

async def get_films(
    db: AsyncSession,
    skip: int = 0,
    limit: int = 10
) -> list[Film]:
    result = await db.execute(select(Film).offset(skip).limit(limit))
    return list(result.scalars().all())