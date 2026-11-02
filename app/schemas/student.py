from typing import List

from pydantic import BaseModel, ConfigDict, EmailStr


class StudentCreate(BaseModel):
    name: str
    email: EmailStr


class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


class StudentUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None


class StudentListResponse(BaseModel):
    total: int
    items: List[StudentResponse]

    model_config = ConfigDict(from_attributes=True)
