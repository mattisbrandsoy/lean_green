import secrets
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    PROJECT_NAME: str = "Lean Green APP"
    PROJECT_VERSION: str = "0.0.1"

    POSTGRES_USER: str = Field(..., env='POSTGRES_USER')
    POSTGRES_PASSWORD: str = Field(..., env="POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = Field(..., env="POSTGRES_SERVER")
    POSTGRES_PORT: str = Field(..., env="POSTGRES_PORT")
    POSTGRES_DB: str = Field(..., env="POSTGRES_DB")
    DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    class Config:
      case_sensitive = True
      env_file = ".env"


settings = Settings(_env_file='.env')
