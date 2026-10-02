from __future__ import annotations
import math


def compute_knee_angle(hip, knee, ankle):
    if not all(point is not None for point in [hip, knee, ankle]):
        return 0.0
    ax, ay = hip
    bx, by = knee
    cx, cy = ankle
    ba_x = ax - bx
    ba_y = ay - by
    bc_x = cx - bx
    bc_y = cy - by
    cosine = (ba_x * bc_x + ba_y * bc_y) / (
        ((ba_x**2 + ba_y**2) ** 0.5) * ((bc_x**2 + bc_y**2) ** 0.5)
    )
    cosine = max(-1.0, min(1.0, cosine))
    angle = math.degrees(math.acos(cosine))
    return float(angle)
