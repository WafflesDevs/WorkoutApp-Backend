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
    tags=["Admins"]
)

@router.get("/allworkouts", status_code=status.HTTP_200_OK)
def get_all_workouts(userid_search: int, db: Session = Depends(get_db), current_user: Users = Depends(oauth2.require_role(["Admin"]))):
    print(f"searching for user: {userid_search}")  # 👈
    query = db.query(Workout).filter(Workout.owner_id == userid_search).all()
    print(f"query result: {query}")  # 👈
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Theres no workouts under user id {userid_search}")
    return query