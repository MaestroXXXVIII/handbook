from fastapi import Header, HTTPException, status
from environs import Env


env = Env()
env.read_env()

API_KEY = env.str("API_KEY", "default_key_if_missing")


def verify_api_key(x_api_key: str = Header(..., alias='STATIC_API_KEY', description='Статический API ключ.')):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный API ключ",
        )
