from datetime import timedelta, timezone, datetime
from src.config import settings
import jwt


def encode_jwt(
        payload: dict,
        expire_timedelta: timedelta | None = None
) -> str:
    to_encode = payload.copy()
    now = datetime.now(tz=timezone.utc)
    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=settings.auth.access_token_expire_minutes)
    to_encode.update(
        exp=expire,
        iat=now,
    )
    encoded = jwt.encode(
        to_encode,
        settings.auth.jwt_private_key.read_text(),
        algorithm=settings.ALGORITHM,
    )
    return encoded


def decode_jwt(
    token: str | bytes
) -> dict:
    decoded = jwt.decode(
        jwt=token,
        key=settings.auth.jwt_public_key.read_text(),
        algorithms=settings.ALGORITHM,
    )
    return decoded
