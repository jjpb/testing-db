from fastapi import FastAPI, Depends, HTTPException
from contextlib import asynccontextmanager
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import engine, get_db, Base
from app.model import Film

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

@app.get("/film/")
async def get_film(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Film))
    films = result.scalars().all()
    return [{"id": film.film_id, "title": film.title} for film in films ]

@app.get("/hello-world")
def hello_world():
    return { "value": "Hello World" }