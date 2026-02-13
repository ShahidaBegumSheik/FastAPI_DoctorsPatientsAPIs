from pydantic import BaseModel, field_validator

class Doctors(BaseModel):
    name: str
    specialization: str
    email: str
    is_active: bool = True

class Patients(BaseModel):
    name: str
    age: int
    phone: int

    @field_validator('age')
    @classmethod
    def check_age(cls, value: int):
        if value < 0:
            raise ValueError('Age cannot be less than 0')
        return value


