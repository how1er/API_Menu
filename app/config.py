from pydantic import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_HOSTNAME: str

    POSTGRES_TESTDB: str

    class Config:
        env_file = f"{Path(__file__).resolve().parent.parent}/.env"


settings = Settings()
