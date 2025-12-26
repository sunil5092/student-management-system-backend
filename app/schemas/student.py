from pydantic import BaseModel, EmailStr


class StudentCreate(BaseModel):
    name: str
    email: EmailStr


class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
class StudentUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
from typing import List


class StudentListResponse(BaseModel):
    total: int
    items: List[StudentResponse]

    class Config:
        orm_mode = True
