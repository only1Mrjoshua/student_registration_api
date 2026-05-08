README for Python FastAPI Version

# Student Registration API - FastAPI

A simple REST API for student registration built with Python, FastAPI, SQLite, SQLAlchemy, and Pydantic.

## Features

- Register a student
- Get all registered students
- Get one student by ID
- Delete a student
- Validate input data
- Prevent duplicate email registration
- Store submissions in SQLite database

## Tech Stack

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- Uvicorn

## Project Structure

```txt
student_registration_api/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
└── requirements.txt

Installation
pip install -r requirements.txt
Run the Server
uvicorn main:app --reload

Server runs on:

http://127.0.0.1:8000
API Documentation

Open Swagger UI:

http://127.0.0.1:8000/docs
Endpoints
Register Student
POST /students/register

Request body:

{
  "name": "John Doe",
  "email": "john@example.com",
  "course": "Computer Science"
}
Get All Students
GET /students
Get One Student
GET /students/{student_id}
Delete Student
DELETE /students/{student_id}
Error Handling
400 - Duplicate email
404 - Student not found
422 - Invalid input

Author
Joshua

```
