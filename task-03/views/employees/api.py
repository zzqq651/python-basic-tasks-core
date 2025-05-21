from fastapi import APIRouter, HTTPException, status

from .schemas import Employee, EmployeeCreate
from .crud import storage

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.get("",response_model=list[Employee])
def list_employees():
    return storage.get_list_all_employees()

@router.get("/{id}", response_model=Employee, responses={status.HTTP_404_NOT_FOUND: {"model": dict, "description": "Item not found"}})
def get_employee_by_id(id: int):
    employee = storage.get_employee_by_id(id)
    if employee:
        return employee

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"employee #{id} not found!"
    )

@router.post("", response_model=Employee)
def create_employee(employee_create: EmployeeCreate):
    return storage.create_employee(employee_create)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(id: int):
    storage.delete_employee(id)