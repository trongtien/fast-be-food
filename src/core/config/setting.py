from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME = "Food"
    SECRET_KEY = "12376781231"
    API_PREFIX = '/api'
    BACKEND_CORS_ORIGINS = ['*']
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7  # Token expired after 7 days
    SECURITY_ALGORITHM = 'HS256'

settings = Settings()