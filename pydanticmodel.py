from datetime import date
from pydantic import BaseModel


class EmployeePydantic(BaseModel):
    id: int
    name: str
    profile_path: str
    gender: str
    department: str
    salary: float
    start_date: date
    notes: str
