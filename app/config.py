from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
class Settings(BaseSettings):
    GROQ_API_KEY: str
    DATABASE_URL: str
    MODEL_NAME: str


    model_config = SettingsConfigDict(env_file=Path(__file__).resolve().parent.parent /".env")

settings = Settings()



#Pydantic is a data validation and configuration management powerhouse. If you are bulding APIs pydantic is for this.
#BaseSettings is a special Pydantic class designed for CONFIGURATION management. It automaticaly load values from environment variables.
#SettingsconfigDict is a dict-like configruation object used in Pydantic v2 to define model-level settings.
#There is old Pydantic v1 style of configuration as : class Config: env_file = ".env"
#model_config attribute is new Pydantic v2 style of configuration
#Path(__file__).resolve().parent.parent /".env" set a path to root even tho it is in cwd 

