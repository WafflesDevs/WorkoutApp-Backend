from jose import jwt,JWTError
from datetime import datetime,timedelta
from app.schemas.schemas import TokenData
from app.schemas import schemas
from sqlalchemy.orm import Session
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings
from app.database.database import get_db
from app.model import model
from app.database import database
from typing import List



oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login') #Extracts the token and the login is where the token is made (THE ROUTE)
# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = settings.secret_key
ALGORITHM = settings.ALGO
ACCESS_TOKEN_EXPIRE_MINUTES = settings.TOKEN_EXPIRE

def create_access_token(data:dict):
   to_encode = data.copy()
   expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
   to_encode.update({"exp":expire})
   jwt_encoded = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
   return jwt_encoded

def verify_access_token(token:str,credit_exception):
  try:
    decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    id: str = decoded_jwt.get('user_id')
    if id is None:
        raise credit_exception
    token_data = schemas.TokenData(id=str(id))
  except JWTError:
        raise credit_exception
  return token_data

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)): #checks if user matches token, If it is then it returns true and stuff
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_access_token(token, credentials_exception)
    user = db.query(model.Users).filter(model.Users.user_id == int(token_data.id)).first()
    if user is None:
        raise credentials_exception
    return user


def require_role(allowed_roles: List[str]): #RUN THIS
    def role_checker(current_user=Depends(get_current_user)):
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access denied. Required roles: {allowed_roles}"
            )
        return current_user
    return role_checker