from sqlalchemy.orm import Session
from app.models.student import Student


def get_students(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    name: str | None = None
):
    query = db.query(Student)

    if name:
        query = query.filter(Student.name.ilike(f"%{name}%"))

    total = query.count()
    students = query.offset(skip).limit(limit).all()

    return {
        "total": total,
        "items": students
    }
