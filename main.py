from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models
import crud
from database import engine, get_db
from schemas import StudentCreate, StudentResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Registration API",
    description="A simple FastAPI backend for registering students.",
    version="1.0.0"
)


@app.post("/students/register")
def register_student(student: StudentCreate, db: Session = Depends(get_db)):
    existing_student = crud.get_student_by_email(db, student.email)

    if existing_student:
        raise HTTPException(
            status_code=400,
            detail="A student with this email already exists."
        )

    saved_student = crud.create_student(db, student)

    return {
        "message": "Student registered successfully.",
        "student": saved_student
    }


@app.get("/students", response_model=List[StudentResponse])
def fetch_all_students(db: Session = Depends(get_db)):
    return crud.get_all_students(db)


@app.get("/students/{student_id}", response_model=StudentResponse)
def fetch_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student_by_id(db, student_id)

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found."
        )

    return student


@app.delete("/students/{student_id}")
def remove_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.delete_student(db, student_id)

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found."
        )

    return {
        "message": "Student deleted successfully."
    }