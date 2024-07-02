from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


class AuthJWT(BaseModel):
    jwt_public_key: Path = BASE_DIR / "certificates" / "jwt-public.pem"
    jwt_private_key: Path = BASE_DIR / "certificates" / "jwt-private.pem"
    access_token_expire_minutes: int = 15


class Settings(BaseSettings):
    DB_URL: str = "sqlite+aiosqlite:///db.sqlite3"
    ALGORITHM: str = "HS256"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    RELOAD: bool = False
    auth: AuthJWT = AuthJWT()

    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/config.env")


settings = Settings()
