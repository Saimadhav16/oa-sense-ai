from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.ml.inference import demo_predict

router = APIRouter()


@router.post('/questionnaire')
def questionnaire_analysis(payload: dict, db: Session = Depends(get_db)):
    features = {
        'age': payload.get('age', 40),
        'pain_score': payload.get('pain_score', 0),
        'stiffness_score': payload.get('stiffness_score', 0),
        'mobility_score': payload.get('mobility_score', 0),
        'walking_difficulty': payload.get('walking_difficulty', 0),
        'stair_difficulty': payload.get('stair_difficulty', 0),
        'activity_level': payload.get('activity_level', 'moderate'),
    }
    summary = {
        'questionnaire_score': sum(features.values()) if isinstance(features['age'], (int, float)) else 0,
        'status': 'recorded',
        'message': 'Questionnaire captured for preliminary screening.'
    }
    return {'features': features, 'summary': summary}


@router.post('/movement')
def movement_analysis(payload: dict):
    left = payload.get('left_knee_angle', 90)
    right = payload.get('right_knee_angle', 90)
    return {
        'left_knee_angle': left,
        'right_knee_angle': right,
        'movement_status': 'ACTIVE' if left > 20 and right > 20 else 'LOW',
        'gait_symmetry': min(99, max(40, round((100 - abs(left - right)) * 0.9, 2))),
        'posture_score': 72,
        'message': 'Movement analysis completed for screening.'
    }


@router.post('/predict')
def predict(payload: dict):
    result = demo_predict(payload)
    return result
