from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Patient, Screening
from app.schemas import ScreeningCreate

router = APIRouter()


@router.post('')
def create_screening(payload: ScreeningCreate, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == payload.patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail='Patient not found')
    screening = Screening(**payload.model_dump())
    db.add(screening)
    db.commit()
    db.refresh(screening)
    return {'message': 'Screening created', 'screening_id': screening.id}


@router.get('')
def list_screenings(db: Session = Depends(get_db)):
    screenings = db.query(Screening).all()
    return [
        {
            'id': item.id,
            'patient_id': item.patient_id,
            'screening_date': item.screening_date,
            'pain_score': item.pain_score,
            'risk_level': item.risk_level,
            'risk_probability': item.risk_probability,
            'model_version': item.model_version,
        }
        for item in screenings
    ]


@router.get('/{screening_id}')
def get_screening(screening_id: int, db: Session = Depends(get_db)):
    screening = db.query(Screening).filter(Screening.id == screening_id).first()
    if not screening:
        raise HTTPException(status_code=404, detail='Screening not found')
    return {
        'id': screening.id,
        'patient_id': screening.patient_id,
        'screening_date': screening.screening_date,
        'pain_score': screening.pain_score,
        'stiffness_score': screening.stiffness_score,
        'mobility_score': screening.mobility_score,
        'left_knee_rom': screening.left_knee_rom,
        'right_knee_rom': screening.right_knee_rom,
        'gait_symmetry': screening.gait_symmetry,
        'posture_score': screening.posture_score,
        'movement_smoothness': screening.movement_smoothness,
        'risk_level': screening.risk_level,
        'risk_probability': screening.risk_probability,
        'model_version': screening.model_version,
    }
