from fastapi import FastAPI
from app.database import engine
from app.models import student

student.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management System API")


@app.get("/")
def root():
    return {"message": "Student Management System API is running"}
