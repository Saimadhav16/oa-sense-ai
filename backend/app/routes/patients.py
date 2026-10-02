from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Patient
from app.schemas import PatientCreate, PatientUpdate

router = APIRouter()


@router.get('')
def list_patients(db: Session = Depends(get_db)):
    patients = db.query(Patient).all()
    return [
        {
            'id': p.id,
            'patient_code': p.patient_code,
            'name': p.name,
            'age': p.age,
            'gender': p.gender,
            'phone': p.phone,
            'location': p.location,
            'occupation': p.occupation,
            'activity_level': p.activity_level,
            'created_at': p.created_at,
        }
        for p in patients
    ]


@router.post('')
def create_patient(payload: PatientCreate, db: Session = Depends(get_db)):
    if db.query(Patient).filter(Patient.patient_code == payload.patient_code).first():
        raise HTTPException(status_code=400, detail='Patient code already exists')
    patient = Patient(**payload.model_dump())
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return {'message': 'Patient created successfully', 'patient': patient.id}


@router.get('/{patient_id}')
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail='Patient not found')
    return {
        'id': patient.id,
        'patient_code': patient.patient_code,
        'name': patient.name,
        'age': patient.age,
        'gender': patient.gender,
        'phone': patient.phone,
        'location': patient.location,
        'occupation': patient.occupation,
        'activity_level': patient.activity_level,
        'created_at': patient.created_at,
    }


@router.put('/{patient_id}')
def update_patient(patient_id: int, payload: PatientUpdate, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail='Patient not found')
    for field, value in payload.model_dump().items():
        setattr(patient, field, value)
    db.commit()
    return {'message': 'Patient updated successfully'}
