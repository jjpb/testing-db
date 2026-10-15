from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

from app.core.db import get_db
from app.crud import film as film_crud
from app.schemas.film import FilmRead

router = APIRouter(
    prefix="/films"
)

@router.get("/")
@router.get("/{skip}")
@router.get("/{skip}/{limit}")
async def get_films(
    skip: Optional[int] = 0,
    limit: Optional[int] = 10,
    db: AsyncSession = Depends(get_db)
):
    return await film_crud.get_films(
        db,
        skip=skip,
        limit=limit
    )