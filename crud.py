from sqlalchemy.orm import Session
from models import Student
from schemas import StudentCreate


def get_student_by_email(db: Session, email: str):
    return db.query(Student).filter(Student.email == email).first()


def create_student(db: Session, student: StudentCreate):
    new_student = Student(
        name=student.name.strip(),
        email=student.email,
        course=student.course.strip()
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


def get_all_students(db: Session):
    return db.query(Student).all()


def get_student_by_id(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()


def delete_student(db: Session, student_id: int):
    student = get_student_by_id(db, student_id)

    if student:
        db.delete(student)
        db.commit()

    return student