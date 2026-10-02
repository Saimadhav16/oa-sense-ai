from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str = 'healthcare_worker'


class UserLogin(BaseModel):
    email: str
    password: str


class PatientCreate(BaseModel):
    patient_code: str
    name: str
    age: int
    gender: Optional[str] = 'Not specified'
    phone: Optional[str] = ''
    location: Optional[str] = ''
    occupation: Optional[str] = ''
    activity_level: Optional[str] = 'moderate'
    previous_joint_injury: Optional[int] = 0
    family_history: Optional[int] = 0
    physically_demanding_work: Optional[int] = 0
    difficulty_walking: Optional[int] = 0
    difficulty_climbing_stairs: Optional[int] = 0
    morning_stiffness: Optional[int] = 0


class PatientUpdate(PatientCreate):
    pass


class QuestionnaireInput(BaseModel):
    patient_id: Optional[int] = None
    age: int = 40
    activity_level: str = 'moderate'
    pain_score: float = 0.0
    stiffness_score: float = 0.0
    mobility_score: float = 0.0
    walking_difficulty: float = 0.0
    stair_difficulty: float = 0.0
    difficulty_bending: float = 0.0
    pain_after_activity: float = 0.0
    pain_rating: float = 0.0
    mobility_rating: float = 0.0


class MovementMetrics(BaseModel):
    left_knee_angle: float = 0.0
    right_knee_angle: float = 0.0
    left_knee_rom: float = 0.0
    right_knee_rom: float = 0.0
    gait_symmetry: float = 0.0
    posture_score: float = 0.0
    movement_smoothness: float = 0.0
    movement_status: str = 'active'


class ScreeningCreate(BaseModel):
    patient_id: int
    pain_score: float = 0.0
    stiffness_score: float = 0.0
    mobility_score: float = 0.0
    left_knee_rom: float = 0.0
    right_knee_rom: float = 0.0
    gait_symmetry: float = 0.0
    posture_score: float = 0.0
    movement_smoothness: float = 0.0
    risk_level: str = 'Low Risk'
    risk_probability: float = 0.0
    model_version: str = 'demo-v1'


class ScreeningOut(ScreeningCreate):
    id: int
    screening_date: datetime
    created_at: datetime


class DashboardStats(BaseModel):
    total_patients: int
    screenings_today: int
    high_risk: int
    moderate_risk: int
    low_risk: int


class ReportRequest(BaseModel):
    screening_id: int
