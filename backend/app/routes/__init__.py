from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import get_db
from app.models import Patient, Screening

router = APIRouter()


@router.get('')
def get_screenings(db: Session = Depends(get_db)):
    screenings = db.query(Screening).all()
    return [
        {
            'id': s.id,
            'patient_id': s.patient_id,
            'screening_date': s.screening_date,
            'pain_score': s.pain_score,
            'risk_level': s.risk_level,
            'risk_probability': s.risk_probability,
        }
        for s in screenings
    ]
