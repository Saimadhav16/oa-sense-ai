from pathlib import Path

import numpy as np
import pandas as pd


def extract_features(payload: dict):
    return {
        'age': float(payload.get('age', 45)),
        'pain_score': float(payload.get('pain_score', 0)),
        'stiffness_score': float(payload.get('stiffness_score', 0)),
        'mobility_score': float(payload.get('mobility_score', 0)),
        'walking_difficulty': float(payload.get('walking_difficulty', 0)),
        'stair_difficulty': float(payload.get('stair_difficulty', 0)),
        'left_knee_rom': float(payload.get('left_knee_rom', 0)),
        'right_knee_rom': float(payload.get('right_knee_rom', 0)),
        'knee_symmetry': float(payload.get('knee_symmetry', 85)),
        'gait_symmetry': float(payload.get('gait_symmetry', 75)),
        'posture_score': float(payload.get('posture_score', 70)),
        'movement_smoothness': float(payload.get('movement_smoothness', 80)),
        'activity_level': payload.get('activity_level', 'moderate'),
    }
