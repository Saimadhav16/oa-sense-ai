from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Report, Screening
from app.services.report_service import generate_pdf_report

router = APIRouter()


@router.post('/generate')
def generate_report(payload: dict, db: Session = Depends(get_db)):
    screening_id = payload.get('screening_id')
    screening = db.query(Screening).filter(Screening.id == screening_id).first()
    if not screening:
        raise HTTPException(status_code=404, detail='Screening not found')
    file_path = generate_pdf_report(screening)
    record = Report(screening_id=screening.id, file_path=file_path)
    db.add(record)
    db.commit()
    db.refresh(record)
    return {'message': 'Report generated', 'report_id': record.id, 'file_path': file_path}


@router.get('/{report_id}')
def get_report(report_id: int, db: Session = Depends(get_db)):
    report = db.query(Report).filter(Report.id == report_id).first()
    if not report:
        raise HTTPException(status_code=404, detail='Report not found')
    return {'id': report.id, 'screening_id': report.screening_id, 'file_path': report.file_path}
