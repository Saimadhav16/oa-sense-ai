import json
from pathlib import Path
from typing import Dict, List
import joblib
import numpy as np
import pandas as pd

MODEL_PATH = Path(__file__).resolve().parents[2] / 'models' / 'demo_oa_model.joblib'


def generate_demo_dataset(size: int = 300) -> pd.DataFrame:
    rng = np.random.default_rng(42)
    rows = []
    for _ in range(size):
        age = int(rng.integers(25, 80))
        pain_score = int(rng.integers(0, 10))
        stiffness_score = int(rng.integers(0, 10))
        mobility_score = int(rng.integers(0, 10))
        walking_difficulty = int(rng.integers(0, 5))
        stair_difficulty = int(rng.integers(0, 5))
        left_knee_rom = round(float(rng.uniform(70, 140)), 2)
        right_knee_rom = round(float(rng.uniform(70, 140)), 2)
        knee_symmetry = round(float(rng.uniform(60, 100)), 2)
        gait_symmetry = round(float(rng.uniform(55, 95)), 2)
        posture_score = round(float(rng.uniform(50, 95)), 2)
        movement_smoothness = round(float(rng.uniform(55, 95)), 2)
        activity_level = int(rng.integers(0, 3))

        score = (
            pain_score * 2 + stiffness_score * 1.8 + mobility_score * 1.5 + walking_difficulty * 3
            + stair_difficulty * 2.5 + (100 - knee_symmetry) * 0.8 + (100 - gait_symmetry) * 0.8
            + (100 - posture_score) * 0.6
        )
        if score > 70:
            risk_level = 2
        elif score > 40:
            risk_level = 1
        else:
            risk_level = 0
        rows.append({
            'age': age,
            'pain_score': pain_score,
            'stiffness_score': stiffness_score,
            'mobility_score': mobility_score,
            'walking_difficulty': walking_difficulty,
            'stair_difficulty': stair_difficulty,
            'left_knee_rom': left_knee_rom,
            'right_knee_rom': right_knee_rom,
            'knee_symmetry': knee_symmetry,
            'gait_symmetry': gait_symmetry,
            'posture_score': posture_score,
            'movement_smoothness': movement_smoothness,
            'activity_level': activity_level,
            'risk_level': risk_level,
        })
    return pd.DataFrame(rows)


def train_demo_model():
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import Pipeline
    from sklearn.impute import SimpleImputer
    from sklearn.preprocessing import StandardScaler
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score, classification_report

    df = generate_demo_dataset(400)
    X = df.drop(columns=['risk_level'])
    y = df['risk_level']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler()),
        ('clf', RandomForestClassifier(n_estimators=200, random_state=42))
    ])
    model.fit(X_train, y_train)
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    return {'accuracy': round(float(accuracy_score(y_test, model.predict(X_test))), 3)}
