# OA-Sense AI

AI-Assisted Early Osteoarthritis Risk Screening System

## Overview
This project is a healthcare-focused screening prototype for early osteoarthritis risk assessment. It combines a questionnaire, pose-based movement analysis, gait/posture indicators, and a lightweight machine-learning pipeline to produce a preliminary OA risk assessment. It is designed for low-resource environments and clinical workflow prototyping, not for clinical diagnosis.

## Architecture

```text
Frontend (React + Vite)
  ↓
  FastAPI backend
  ↓
  SQLite database
  ↓
  ML + feature extraction + CV pipeline
  ↓
  Screening result + PDF report
```

## Features
- JWT-based auth with demo user
- Patient registration and history
- Mobile-friendly questionnaire
- Real-time webcam analysis through MediaPipe Pose
- Knee angle, gait and posture indicators
- ML-based OA risk prediction using demo data
- Dashboard and PDF report generation
- Offline local persistence
- SQLite + SQLAlchemy
- Demo mode for research prototypes

## Medical disclaimer
This is a research prototype and not a medical diagnosis system. It must not be used in place of clinical evaluation. Any concerning result should prompt review by a qualified healthcare professional.

## Tech stack
Frontend
- React
- TypeScript
- Vite
- Tailwind CSS
- Recharts
- Lucide React

Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn
- Pydantic

AI / CV
- scikit-learn
- NumPy
- Pandas
- OpenCV
- MediaPipe Pose

## Demo login
Email: demo@oasense.ai
Password: demo123

## Run backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Run frontend
```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0
```

## Docker
```bash
docker compose up --build
```

## API documentation
Once backend is running, open:
- http://localhost:8000/docs
- http://localhost:8000/redoc

## Notes
This project includes a DEMO MODE: ML predictions are based on synthetic development data and are intentionally labeled as non-clinical predictions.
