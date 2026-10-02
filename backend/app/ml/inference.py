from pathlib import Path
import joblib
import pandas as pd

from app.ml.feature_extraction import extract_features
from app.ml.pose_analysis import train_demo_model

MODEL_PATH = Path(__file__).resolve().parents[2] / 'models' / 'demo_oa_model.joblib'


def ensure_model_exists():
    if not MODEL_PATH.exists():
        train_demo_model()


def demo_predict(payload: dict):
    ensure_model_exists()
    features = extract_features(payload)
    feature_df = pd.DataFrame([features])
    model = joblib.load(MODEL_PATH)
    prediction = int(model.predict(feature_df)[0])
    probs = model.predict_proba(feature_df)[0]
    labels = {0: 'Low Risk', 1: 'Moderate Risk', 2: 'High Risk'}
    confidence = float(max(probs))
    return {
        'risk_level': labels.get(prediction, 'Moderate Risk'),
        'risk_probability': round(float(probs[prediction]) * 100, 2),
        'confidence': round(confidence * 100, 2),
        'demo_mode': True,
        'explanation': [
            'Pain and mobility indicators are contributing to the screening profile.',
            'Reduced gait symmetry and movement smoothness were considered in the model.',
            'This is a demo prediction using development data and is not a medical diagnosis.'
        ],
        'features': features,
    }
