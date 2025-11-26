from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=False)

    app_env: str = Field(default="development", description="Application environment")
    database_url: str = Field(
        default="postgresql+psycopg://smartfitly:smartfitly@localhost:5432/smartfitly",
        description="Database connection string",
    )
    tz: str = Field(default="UTC", description="Default timezone")


settings = Settings()
