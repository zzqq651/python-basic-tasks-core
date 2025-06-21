from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    func,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from models import Base


class Employee(Base):
    full_name = Column(String)
    date = Column(
        DateTime,
        default=datetime.utcnow,
        server_default=func.now(),
        nullable=False,
    )

    department_id = Column(
        Integer, ForeignKey("departments.id"), nullable=False, unique=False
    )

    department = relationship("Department", back_populates="employees")

    def __repr__(self):
        return f"Employee(id={self.id}, full_name={self.full_name}, date={self.date!r}, department_id={self.department_id})"
