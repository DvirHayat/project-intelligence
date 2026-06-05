"""Application configuration."""
import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    app_name: str = "Project Intelligence Backend"
    debug: bool = os.getenv("DEBUG", False)
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    api_v1_str: str = "/api/v1"

    class Config:
        env_file = ".env"


settings = Settings()
