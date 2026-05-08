from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    course: str = Field(..., min_length=1)


class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    course: str
    created_at: datetime

    class Config:
        from_attributes = True