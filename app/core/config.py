from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    database_url: str = "postgresql+asyncpg://postgres:123456@localhost:5432/pagila"

    app_name: str = "Test App"
    debug: bool = False

    db_pool_size: int = 20
    db_max_overflow: int = 10
    db_pool_recycle: int = 3600

@lru_cache
def get_settings() -> Settings:
    return Settings()