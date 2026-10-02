from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.ml.inference import demo_predict

router = APIRouter()


@router.post('/questionnaire')
def questionnaire_analysis(payload: dict, db: Session = Depends(get_db)):
    questionnaire_total = (
        float(payload.get('pain_score', 0)) +
        float(payload.get('stiffness_score', 0)) +
        float(payload.get('mobility_score', 0)) +
        float(payload.get('walking_difficulty', 0)) +
        float(payload.get('stair_difficulty', 0))
    )
    return {
        'features': {
            'pain_score': payload.get('pain_score', 0),
            'stiffness_score': payload.get('stiffness_score', 0),
            'mobility_score': payload.get('mobility_score', 0),
            'walking_difficulty': payload.get('walking_difficulty', 0),
            'stair_difficulty': payload.get('stair_difficulty', 0),
            'age': payload.get('age', 45),
            'activity_level': payload.get('activity_level', 'moderate'),
        },
        'summary': {
            'questionnaire_score': round(questionnaire_total, 2),
            'status': 'recorded',
            'message': 'Questionnaire captured for preliminary screening.'
        }
    }


@router.post('/movement')
def movement_analysis(payload: dict):
    left_angle = float(payload.get('left_knee_angle', 90))
    right_angle = float(payload.get('right_knee_angle', 90))
    gait_symmetry = max(0, min(100, round((100 - abs(left_angle - right_angle)) * 0.9, 2)))
    return {
        'left_knee_angle': left_angle,
        'right_knee_angle': right_angle,
        'movement_status': 'ACTIVE' if left_angle > 25 and right_angle > 25 else 'LOW',
        'gait_symmetry': gait_symmetry,
        'posture_score': 74,
        'message': 'Movement analysis completed for screening.'
    }


@router.post('/predict')
def predict(payload: dict):
    return demo_predict(payload)
