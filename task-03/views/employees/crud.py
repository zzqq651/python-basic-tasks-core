from dataclasses import dataclass, field

from .schemas import Employee, EmployeeCreate


@dataclass
class EmployeeStorage:
    employees: dict[int, Employee] = field(default_factory=dict)
    last_id: int = 0

    @property
    def next_id(self):
        self.last_id += 1
        return self.last_id

    def create_employee(self, employee_create: EmployeeCreate) -> Employee:
        id = self.next_id
        employee = Employee(id=id, **employee_create.dict())

        self.employees[id] = employee

        return employee

    def get_list_all_employees(self):
        return list(self.employees.values())

    def get_employee_by_id(self, id):
        return self.employees.get(id)

    def delete_employee(self, id):
        self.employees.pop(id)


storage = EmployeeStorage()

