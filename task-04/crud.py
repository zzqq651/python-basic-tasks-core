from sqlalchemy import (
    create_engine,
)
from models import Department, Employee
from sqlalchemy.orm import Session as SessionType, sessionmaker, selectinload
import config


def create_department(
    session: SessionType, name: str, address: str
) -> Department:
    department = Department(name=name, address=address)
    session.add(department)
    session.commit()

    return department


def create_employees(
    session: SessionType, *names: str, department: Department
) -> list[Employee]:
    employees = []

    for name in names:
        employee = Employee(full_name=name, department_id=department.id)
        employees.append(employee)

    session.add_all(employees)
    session.commit()
    return employees


def get_departments(session: SessionType) -> list[Department]:
    return session.query(Department).order_by(Department.id).all()


def get_employees(session: SessionType) -> list[Employee]:
    return (
        session.query(Employee)
        .options(selectinload(Employee.department))
        .order_by(Employee.id)
        .all()
    )


def main():
    engine = create_engine(config.DB_URL, echo=config.DB_ECHO)
    session_factory = sessionmaker(bind=engine)
    with session_factory() as session:
        sales = create_department(session, "sales", "Yaroslavl Puskina st")
        it = create_department(session, "IT", "Saint P")
        employees = create_employees(
            session,
            "Daniil",
            "Svyat",
            "Denis",
            "Volodya",
            "Dimas",
            department=it,
        )
        print("Get Departments:", get_departments(session))
        print("Get Employees:", get_employees(session))


if __name__ == "__main__":
    main()
