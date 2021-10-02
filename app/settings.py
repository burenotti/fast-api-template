from pydantic import BaseSettings


class Settings(BaseSettings):

	# Uvicorn

	HOST: str = "localhost"
	PORT: int = 5000
	UVICORN_RELOAD: bool = 1
	UVICORN_WORKERS: int = 1

	# Database

	DB_URL: str


settings = Settings(
	_env_file='.env',
	_env_file_encoding='utf-8',
)
