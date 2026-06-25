from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr
    password: str
    role : str  = "User"

class UserResponse(BaseModel):
    user_id: int
    email: str
    created_at: datetime
    role: str 

    class Config:
        from_attributes = True
class UserLogin(BaseModel):
    email: EmailStr
    password: str
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class SameWeight(BaseModel):
    type:str
    reps:int
    weight: int
    sets:Optional[int]
class SameWeightReponse(BaseModel):
    id: int
    type:str
    reps:int
    weight: int
    created_at: datetime
    sets:Optional[int]
class WorkoutResponse(BaseModel):
    id: int
    owner_id: int
    type: str
    weight: int
    reps: int
    sets: int

    class Config:
        from_attributes = True


class GoalsCreate(BaseModel):
    goal_workouts: int
    biggest_weight: int
    goal_weight: int

class GoalsResponse(GoalsCreate):
    id: int
    owner_id: int

    class Config:
        from_attributes = True