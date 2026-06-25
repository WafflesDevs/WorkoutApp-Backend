from fastapi import APIRouter
from app.schemas import schemas
from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database.database import get_db
from app.core import oauth2
from app.model.model  import Users
from app.core import utils
from app.core.config import allowed_roles
router = APIRouter(
    tags=["Authenication"]
)



@router.post("/login")
def login_user(info: schemas.UserLogin, db: Session = Depends(get_db)):
    email_check = db.query(Users).filter(Users.email == info.email).first()
    if not email_check:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Login Invalid, Try again")
    
    verify_pwd = utils.verify_password(info.password, email_check.password)
    if not verify_pwd:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Login Invalid, Try again")
    
    access_token = oauth2.create_access_token(data={ #Add to token! IMPORTANT!!!!
        "user_id": email_check.user_id,
        "role": email_check.role        # 👈 only change
    })
    return {"access_token": access_token, "token_type": "bearer"}

