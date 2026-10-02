from pathlib import Path

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

FEATURE_COLUMNS = [
    'age', 'pain_score', 'stiffness_score', 'mobility_score', 'walking_difficulty',
    'stair_difficulty', 'left_knee_rom', 'right_knee_rom', 'knee_symmetry',
    'gait_symmetry', 'posture_score', 'movement_smoothness', 'activity_level'
]


class DemoPreprocessor:
    def __init__(self):
        self.numeric_columns = [
            'age', 'pain_score', 'stiffness_score', 'mobility_score', 'walking_difficulty',
            'stair_difficulty', 'left_knee_rom', 'right_knee_rom', 'knee_symmetry',
            'gait_symmetry', 'posture_score', 'movement_smoothness'
        ]
        self.preprocessor = ColumnTransformer([
            ('num', Pipeline([
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ]), self.numeric_columns),
        ], remainder='passthrough')

    def fit(self, X, y=None):
        self.preprocessor.fit(X)
        return self

    def transform(self, X):
        return self.preprocessor.transform(X)


def build_demo_model():
    model = Pipeline([
        ('preprocessor', DemoPreprocessor()),
        ('classifier', RandomForestClassifier(n_estimators=200, random_state=42))
    ])
    return model
