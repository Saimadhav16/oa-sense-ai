def posture_score(shoulder_alignment: float, hip_alignment: float, torso: float, knee_alignment: float) -> dict:
    score = round((shoulder_alignment + hip_alignment + torso + knee_alignment) / 4, 2)
    return {'posture_score': score, 'status': 'Stable' if score > 70 else 'Needs review'}
