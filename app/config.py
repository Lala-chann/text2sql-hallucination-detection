from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
class Settings(BaseSettings):
    GROQ_API_KEY: str
    DATABASE_URL: str
    MODEL_NAME: str


    model_config = SettingsConfigDict(env_file=Path(__file__).resolve().parent.parent /".env")

settings = Settings()

