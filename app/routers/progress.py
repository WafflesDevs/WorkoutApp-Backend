from fastapi import APIRouter
from app.schemas import schemas
from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database.database import get_db
from app.core import oauth2
from app.model.model  import Workout,Users,Progress
from app.core import utils
from app.core.config import allowed_roles
router = APIRouter( 
    tags=["Progress"]
)


@router.post("/createprogress",status_code=status.HTTP_201_CREATED,response_description=schemas.GoalsResponse)
def create_goal(info: schemas.GoalsCreate, db : Session  = Depends(get_db) , current_user: Users = Depends(oauth2.require_role(allowed_roles))):
   goals = Progress(owner_id = current_user.user_id,**info.model_dump())
   db.add(goals)
   db.commit()
   db.refresh(goals)
   return goals
@router.get("/progress", status_code=status.HTTP_200_OK, response_description=schemas.GoalsResponse)
def create_goal(db: Session = Depends(get_db), current_user: Users = Depends(oauth2.require_role(allowed_roles))):
    check = db.query(Progress).filter(Progress.owner_id == current_user.user_id).first()

    if not check:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No progress found for user {current_user.user_id}"  # 👈 use current_user, not check
        )
    
    return check
@router.put("/progress/{id}", response_model=schemas.GoalsResponse,status_code=status.HTTP_202_ACCEPTED)
def update_workout(id: int, workout: schemas.GoalsCreate, db: Session = Depends(get_db), current_user: Users = Depends(oauth2.require_role(allowed_roles))):
    query = db.query(Progress).filter(Progress.id == id)
    if not query.first():
        raise HTTPException(status_code=404, detail="Workout not found")
    if query.first().owner_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not allowed")
    query.update(workout.model_dump())
    db.commit()
    return query.first()
   

