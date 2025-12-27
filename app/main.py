from fastapi import FastAPI
from app.database import engine
from app.models import student
from app.routes import student as student_routes
from app.models import user
from app.routes import auth



student.Base.metadata.create_all(bind=engine)

from fastapi.security import OAuth2PasswordBearer

app = FastAPI(
    title="Student Management System API",
    description="Backend API with JWT Authentication",
)


app.include_router(student_routes.router)
app.include_router(auth.router)



@app.get("/")
def root():
    return {"message": "Student Management System API is running"}
