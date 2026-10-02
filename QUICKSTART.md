# OA-Sense AI - Quick Start Guide

## Prerequisites
- Python 3.9+
- Node.js 18+
- npm or yarn
- Git

## Project Structure
```
oa-sense-ai/
├── backend/          # Python FastAPI backend
├── frontend/         # React + TypeScript frontend
├── models/           # ML models (auto-generated)
├── reports/          # PDF reports (auto-generated)
└── README.md
```

---

## Backend Setup (Python)

### 1. Navigate to backend directory
```bash
cd backend
```

### 2. Create and activate virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create .env file
```bash
cp ../.env.example .env
```

### 5. Run the backend server
```bash
python run.py
```

The backend will start at: **http://localhost:8000**

API documentation available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## Frontend Setup (React)

### 1. Navigate to frontend directory (in a NEW terminal)
```bash
cd frontend
```

### 2. Install dependencies
```bash
npm install
```

### 3. Create .env file
```bash
echo "VITE_API_URL=http://localhost:8000/api" > .env
```

### 4. Run the development server
```bash
npm run dev
```

The frontend will start at: **http://localhost:5173**

---

## Demo Login Credentials

**Email:** `demo@oasense.ai`  
**Password:** `demo123`

---

## Using Docker (Optional)

If you have Docker installed:

```bash
# From the root directory
docker compose up --build
```

Then:
- Frontend: http://localhost:5173
- Backend: http://localhost:8000

---

## First Time Setup - Complete Walkthrough

### Terminal 1 - Backend
```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python run.py
```

### Terminal 2 - Frontend
```bash
cd frontend
npm install
npm run dev
```

### Terminal 3 - Optional: Initialize Database
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
python -c "from app.database import Base, engine; from app.models import *; Base.metadata.create_all(bind=engine); print('Database initialized')"
```

---

## Application Workflow

1. **Login** → Use demo credentials
2. **Dashboard** → View patient stats and recent screenings
3. **Register Patient** → Create a new patient record
4. **Start Screening** → Begin OA risk assessment
5. **Questionnaire** → Answer health questions
6. **Movement Test** → Simulate webcam analysis (or use real camera)
7. **ML Prediction** → Get risk assessment (Low/Moderate/High)
8. **View Results** → See detailed screening dashboard
9. **Generate Report** → Create PDF report
10. **Patient History** → View previous screenings

---

## API Endpoints (Available after backend starts)

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/register` - Register new user

### Patients
- `GET /api/patients` - List all patients
- `POST /api/patients` - Create new patient
- `GET /api/patients/{id}` - Get patient details
- `PUT /api/patients/{id}` - Update patient

### Screenings
- `GET /api/screenings` - List all screenings
- `POST /api/screenings` - Create new screening
- `GET /api/screenings/{id}` - Get screening details

### Analysis
- `POST /api/analysis/questionnaire` - Process questionnaire
- `POST /api/analysis/movement` - Analyze movement
- `POST /api/analysis/predict` - Get ML risk prediction

### Reports
- `POST /api/reports/generate` - Generate PDF report
- `GET /api/reports/{id}` - Get report info

### Dashboard
- `GET /api/dashboard/statistics` - Get dashboard stats

---

## Troubleshooting

### Port Already in Use

**Backend (Port 8000):**
```bash
# Find process using port 8000
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill the process or use a different port
uvicorn app.main:app --reload --port 8001
```

**Frontend (Port 5173):**
```bash
npm run dev -- --port 5174
```

### Dependencies Not Installing

```bash
# Clear pip cache and reinstall
pip cache purge
pip install --upgrade pip
pip install -r requirements.txt
```

### Database Issues

```bash
# Delete database and reinitialize
rm backend/oa_sense.db
cd backend
python -c "from app.database import Base, engine; from app.models import *; Base.metadata.create_all(bind=engine)"
```

### CORS Errors

Ensure backend is running and `.env` in frontend has correct API URL:
```
VITE_API_URL=http://localhost:8000/api
```

---

## Development Commands

### Backend
```bash
cd backend

# Run with auto-reload
python run.py

# Run tests (if available)
python -m pytest

# Access interactive shell
python -i -c "from app.database import SessionLocal; db = SessionLocal()"
```

### Frontend
```bash
cd frontend

# Development server
npm run dev

# Production build
npm run build

# Preview production build
npm run preview

# Lint code
npm run lint
```

---

## Production Deployment

### Backend (with Gunicorn)
```bash
cd backend
pip install gunicorn
gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Frontend (build and serve)
```bash
cd frontend
npm run build
npm install -g serve
serve -s dist -l 3000
```

---

## Features

✅ JWT Authentication  
✅ Patient Registration & Management  
✅ OA Risk Questionnaire  
✅ Real-time Movement Analysis (simulated)  
✅ ML-based Risk Prediction (Random Forest)  
✅ Dashboard with Charts  
✅ PDF Report Generation  
✅ Patient History & Comparisons  
✅ Offline Mode Support  
✅ Responsive Mobile UI  
✅ Demo Mode for Testing  

---

## Important Medical Disclaimer

⚠️ **This is a research prototype and educational tool only.**

Never use this system for clinical diagnosis. It provides preliminary screening indicators based on synthetic development data. Always consult qualified healthcare professionals for medical evaluation.

This system is **NOT** a replacement for professional medical diagnosis or treatment.

---

## Support & Issues

For questions or issues:
1. Check the troubleshooting section above
2. Review API docs at http://localhost:8000/docs (after starting backend)
3. Check browser console for errors (press F12)
4. Ensure both frontend and backend are running

---

## Next Steps

1. Start the backend and frontend as described above
2. Login with demo credentials
3. Create a demo patient
4. Run through the complete screening workflow
5. Generate a PDF report
6. Explore the API documentation

**Happy screening! 🏥**
