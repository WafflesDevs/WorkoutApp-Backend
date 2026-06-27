from fastapi import APIRouter
from app.schemas import schemas
from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from fastapi import Depends
from app.schemas import schemas
from app.database.database import get_db
from app.core import oauth2
from app.model.model  import Users,Workout,Progress
from app.core import utils
from app.core.config import allowed_roles
from app.core.config import gym_workouts
router = APIRouter(
    tags=["Workouts"]
)

@router.post("/workout",status_code=status.HTTP_201_CREATED,response_model=schemas.SameWeightReponse)
def begin_workout(workout:schemas.SameWeight,db : Session  = Depends(get_db),current_user: Users = Depends(oauth2.require_role(allowed_roles))):
    new_workout = Workout(**workout.model_dump(), owner_id=current_user.user_id)

    db.add(new_workout)
    db.commit()
    db.refresh(new_workout)
    return new_workout

@router.delete("/workout/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_workout(id: int, db: Session = Depends(get_db), current_user: Users = Depends(oauth2.require_role(allowed_roles))):
    checker = db.query(Workout).filter(Workout.id == id).first()
    if not checker:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Workout id:{id} doesn't exist")
    if checker.owner_id != current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed to delete this workout")
    db.delete(checker)
    db.commit()

@router.put("/workout/{id}", response_model=schemas.WorkoutResponse,status_code=status.HTTP_202_ACCEPTED)
def update_workout(id: int, workout: schemas.SameWeight, db: Session = Depends(get_db), current_user: Users = Depends(oauth2.require_role(allowed_roles))):
    query = db.query(Workout).filter(Workout.id == id)
    if not query.first():
        raise HTTPException(status_code=404, detail="Workout not found")
    if query.first().owner_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not allowed")
    query.update(workout.model_dump())
    db.commit()
    return query.first()

@router.get("/allworkouts",response_model=schemas.WorkoutResponse,status_code=status.HTTP_200_OK )
def all_workouts(db: Session = Depends(get_db), current_user : Users = Depends(oauth2.require_role(allowed_roles))):
   workouts = db.query(Workout).filter(Workout.owner_id == current_user.user_id).all()
   if not workouts:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Workouts not found!")
   return workouts

@router.get("/workouts")
def all_workouts_template():
    return{"Workouts": gym_workouts}

