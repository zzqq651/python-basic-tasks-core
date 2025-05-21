from pydantic import BaseModel, EmailStr, Field


class EmployeeBase(BaseModel):
    full_name: str = Field(..., example="Sokolov Daniil")
    email: EmailStr = Field(..., example="pu@pu.pu")


class EmployeeCreate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    id: int
