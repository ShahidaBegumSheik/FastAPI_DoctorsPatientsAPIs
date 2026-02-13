from fastapi import FastAPI, HTTPException
from models import Doctors, Patients
import re

app = FastAPI()

@app.get("/")
def greet():
    return "Doctors Patients DB"

doctors = [
    Doctors(name="Andrew Thomas",specialization="ENT",email="andrth@gmail.com"),
    Doctors(name="Sreenivasan",specialization="Pulmonology",email="sreeni@outlook.com"),
    Doctors(name="Dillon", specialization="Neurologist",email="dillon@gmail.com", is_active=False),
    Doctors(name="Gobu",specialization="Cardiology",email="drgobu@gmail.com"),
]

patients = [
    Patients(name="Samuel",age=32, phone=9841234567),
    Patients(name="Claris",age=45, phone=9801234567),
]

def is_valid_email(email: str) -> bool:
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern,email) is not None

@app.get("/doctors")
def get_doctor_details():
    return doctors

@app.post("/add_doctor")
def add_doctor_details(newdoctor: Doctors):
    if newdoctor not in doctors:
        if not is_valid_email(newdoctor.email):
            raise HTTPException(status_code=400, detail="Email id incorrect")
        doctors.append(newdoctor)
    return newdoctor

@app.get("/patients")
def get_patient_details():
    return patients

@app.post("/add_patient")
def add_patient_details(newpatient: Patients):
    if newpatient not in patients:
        patients.append(newpatient)
    return newpatient

    

