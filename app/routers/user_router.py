from fastapi import APIRouter
from app.schemas import schemas
from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database.database import get_db
from app.core import oauth2
from app.model.model  import Users,Workout
from app.core import utils
from app.core.config import allowed_roles
router = APIRouter(
    prefix="/users", 
    tags=["Users"]
)
@router.post('/create_user', response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def user_login(info: schemas.UserBase , db : Session = Depends(get_db)):
    user_check = db.query(Users).filter(Users.email == info.email).first()
    if user_check:
        raise HTTPException(status_code=status.HTTP_226_IM_USED,detail=f"Email {info.email} in use, Try again")
    info.password = utils.hash_password(info.password) #make sure to hash plz :sob:
    new_user = Users(**info.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/user/workouts", response_model=list[schemas.WorkoutResponse], status_code=status.HTTP_200_OK)
def get_workouts(db: Session = Depends(get_db), current_user: Users = Depends(oauth2.require_role(allowed_roles))):
    workouts = db.query(Workout).filter(Workout.owner_id == current_user.user_id).all()
    if not workouts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No workouts found")
    return workouts
