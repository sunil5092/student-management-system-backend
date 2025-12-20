from fastapi import FastAPI

app = FastAPI(title="Student Management System API")


@app.get("/")
def root():
    return {"message": "Student Management System API is running"}
