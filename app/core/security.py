from datetime import datetime, timezone, timedelta
from jose import jwt, JWTError
from app.core.config import settings


def create_token(data: dict, expire_minutes=30):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc)+timedelta(minutes=expire_minutes)
    to_encode.update({'exp':expire})
    return jwt.incode(
        to_encode,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )
def verify_token(token:str):
    try:
        payload = jwt.decode
        token, settings.jwt
        pass
    except JWTError:
        return None

    