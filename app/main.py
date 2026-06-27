from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import progress, user_router,auth,workouts,admin

app = FastAPI(title="FastAPI CRUD App", version="1.0.0")



app.include_router(user_router.router)
app.include_router(auth.router)
app.include_router(workouts.router)
app.include_router(progress.router)
app.include_router(admin.router)


origins = [
    "http://localhost",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"Welcome!","To the workout app "}
    