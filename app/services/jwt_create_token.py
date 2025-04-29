from jose import jwt
import os
from dotenv import load_dotenv
load_dotenv()
from datetime import datetime,timedelta

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))



def crear_token2(user):
    token_data = {
        "sub": user.st_usuario,  # puedes usar también el id
        "id": user.id_med_user  # si tienes ese campo
    }
    if token_data:
        to_encode = token_data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
