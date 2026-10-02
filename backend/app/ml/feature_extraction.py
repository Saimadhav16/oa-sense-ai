import math


def compute_knee_angle(hip, knee, ankle):
    if not all(point is not None for point in [hip, knee, ankle]):
        return 0.0
    ax, ay = hip
    bx, by = knee
    cx, cy = ankle
    vector_ab_x = ax - bx
    vector_ab_y = ay - by
    vector_cb_x = cx - bx
    vector_cb_y = cy - by
    ab_len = math.hypot(vector_ab_x, vector_ab_y)
    cb_len = math.hypot(vector_cb_x, vector_cb_y)
    if ab_len == 0 or cb_len == 0:
        return 0.0
    dot = (vector_ab_x * vector_cb_x) + (vector_ab_y * vector_cb_y)
    cos_theta = max(-1.0, min(1.0, dot / (ab_len * cb_len)))
    return float(math.degrees(math.acos(cos_theta)))
