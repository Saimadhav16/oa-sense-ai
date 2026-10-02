from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Patient, Screening

router = APIRouter()


@router.get('/statistics')
def statistics(db: Session = Depends(get_db)):
    total_patients = db.query(Patient).count()
    total_screenings = db.query(Screening).count()
    high_risk = db.query(Screening).filter(Screening.risk_level.ilike('%High%')).count()
    moderate_risk = db.query(Screening).filter(Screening.risk_level.ilike('%Moderate%')).count()
    low_risk = db.query(Screening).filter(Screening.risk_level.ilike('%Low%')).count()
    return {
        'total_patients': total_patients,
        'screenings_today': total_screenings,
        'high_risk': high_risk,
        'moderate_risk': moderate_risk,
        'low_risk': low_risk,
    }
