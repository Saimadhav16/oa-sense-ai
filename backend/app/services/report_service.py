def gait_score(symmetry: float, smoothness: float, cadence: float = 0.0):
    score = round(((symmetry * 0.5) + (smoothness * 0.5)), 2)
    if score >= 75:
        label = 'Low'
    elif score >= 55:
        label = 'Moderate'
    else:
        label = 'High'
    return {
        'gait_score': score,
        'gait_indicator': label,
        'movement_consistency': min(100, max(0, int(smoothness))),
        'gait_symmetry': min(100, max(0, int(symmetry))),
        'cadence_estimate': round(cadence, 2),
    }


def posture_summary(shoulder_alignment: float, hip_alignment: float, torso_inclination: float, knee_alignment: float):
    score = round((shoulder_alignment + hip_alignment + torso_inclination + knee_alignment) / 4, 2)
    return {'posture_score': score, 'status': 'Stable' if score > 70 else 'Needs review'}
