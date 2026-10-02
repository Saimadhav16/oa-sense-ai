from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default='healthcare_worker')
    created_at = Column(DateTime, default=datetime.utcnow)


class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True, index=True)
    patient_code = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, default='Not specified')
    phone = Column(String, default='')
    location = Column(String, default='')
    occupation = Column(String, default='')
    activity_level = Column(String, default='moderate')
    previous_joint_injury = Column(Integer, default=0)
    family_history = Column(Integer, default=0)
    physically_demanding_work = Column(Integer, default=0)
    difficulty_walking = Column(Integer, default=0)
    difficulty_climbing_stairs = Column(Integer, default=0)
    morning_stiffness = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    screenings = relationship('Screening', back_populates='patient')


class Screening(Base):
    __tablename__ = 'screenings'
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    screening_date = Column(DateTime, default=datetime.utcnow)
    pain_score = Column(Float, default=0.0)
    stiffness_score = Column(Float, default=0.0)
    mobility_score = Column(Float, default=0.0)
    left_knee_rom = Column(Float, default=0.0)
    right_knee_rom = Column(Float, default=0.0)
    gait_symmetry = Column(Float, default=0.0)
    posture_score = Column(Float, default=0.0)
    movement_smoothness = Column(Float, default=0.0)
    risk_level = Column(String, default='Low Risk')
    risk_probability = Column(Float, default=0.0)
    model_version = Column(String, default='demo-v1')
    created_at = Column(DateTime, default=datetime.utcnow)
    patient = relationship('Patient', back_populates='screenings')
    reports = relationship('Report', back_populates='screening')
    movement_frames = relationship('MovementFrame', back_populates='screening')


class MovementFrame(Base):
    __tablename__ = 'movement_frames'
    id = Column(Integer, primary_key=True, index=True)
    screening_id = Column(Integer, ForeignKey('screenings.id'))
    timestamp = Column(Float, default=0.0)
    left_knee_angle = Column(Float, default=0.0)
    right_knee_angle = Column(Float, default=0.0)
    hip_angle = Column(Float, default=0.0)
    posture_value = Column(Float, default=0.0)
    screening = relationship('Screening', back_populates='movement_frames')


class Report(Base):
    __tablename__ = 'reports'
    id = Column(Integer, primary_key=True, index=True)
    screening_id = Column(Integer, ForeignKey('screenings.id'))
    file_path = Column(String, default='')
    created_at = Column(DateTime, default=datetime.utcnow)
    screening = relationship('Screening', back_populates='reports')
