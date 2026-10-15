from pydantic import BaseModel, ConfigDict

class FilmRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    film_id: int 
    title: str
    description: str