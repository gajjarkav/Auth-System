from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from pathlib import Path

class Settings(BaseSettings):

    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / ".env",
        env_file_encoding="utf-8",
        case_sensitive=True
    )


settings = Settings()
