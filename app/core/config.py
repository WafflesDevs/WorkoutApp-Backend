from pydantic_settings import BaseSettings
PROJECT_NAME = "FastAPI CRUD App"
VERSION = "1.0.0"
class Settings(BaseSettings):
    secret_key: str
    database_name : str
    database_password : str
    database_port: str
    database_username:str
    database_user:str
    database_hostname : str
    TOKEN_EXPIRE:int
    ALGO:str
    


    class Config:
        env_file = ".env"

settings = Settings()
allowed_roles = ["Admin", "User"]