from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.models import student, user
from app.routes import auth
from app.routes import student as student_routes

student.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management System API",
    description="Backend API with JWT Authentication",
)

# The React frontend is hosted on a different origin, so the API must
# allow cross-origin browser requests (auth uses a bearer token, not cookies).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student_routes.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Student Management System API is running"}
