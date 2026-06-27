from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from app.database.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey

class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, nullable=False, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    role = Column(String, nullable=False, default="User", server_default="User")

class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, nullable=False, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    type = Column(String, nullable=False)
    weight = Column(Integer, nullable=False)
    reps = Column(Integer, nullable=False)
    sets = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class Progress(Base):
    __tablename__ =  "Progress"
    id = Column(Integer, nullable=False, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    goal_workouts = Column(Integer, nullable=False)
    biggest_weight = Column(Integer, nullable=False) # Ill grab the max weight produced in the workout table under the owner_id
    goal_weight = Column(Integer,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),server_default=text('now()'),nullable=False)


# model.py - add this
class BlacklistedToken(Base):
    __tablename__ = "blacklisted_tokens"
    id = Column(Integer, primary_key=True)
    token = Column(String, nullable=False, unique=True)
    blacklisted_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))