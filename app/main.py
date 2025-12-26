from fastapi import FastAPI
from app.database import engine
from app.models import student
from app.routes import student as student_routes

student.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management System API")

app.include_router(student_routes.router)


@app.get("/")
def root():
    return {"message": "Student Management System API is running"}
