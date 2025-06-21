from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import relationship

from models import Base


class Department(Base):
    name = Column(String)
    address = Column(String)

    employees = relationship("Employee", back_populates="department")

    def __repr__(self):
        return f"Department(id={self.id}, name={self.name!r}, address={self.address!r})"
