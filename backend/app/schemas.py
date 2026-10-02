from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, List


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str = 'healthcare_worker'


class UserLogin(BaseModel):
    email: str
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    email: str
    role: str
    created_at: datetime


class PatientCreate(BaseModel):
    patient_code: str
    name: str
    age: int
    gender: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    occupation: Optional[str] = None
    activity_level: Optional[str] = 'moderate'


class PatientUpdate(PatientCreate):
    pass


class PatientOut(PatientCreate):
    id: int
    created_at: datetime


class QuestionnaireInput(BaseModel):
    patient_id: Optional[int] = None
    pain_score: float = 0.0
    stiffness_score: float = 0.0
    mobility_score: float = 0.0
    walking_difficulty: float = 0.0
    stair_difficulty: float = 0.0
    difficulty_bending: float = 0.0
    pain_after_activity: float = 0.0
    pain_rating: float = 0.0
    mobility_rating: float = 0.0
    age: int = 40
    activity_level: str = 'moderate'


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
