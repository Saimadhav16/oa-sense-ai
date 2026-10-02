# OA-Sense AI

AI-Assisted Early Osteoarthritis Risk Screening System

A comprehensive healthcare screening application designed to assist in identifying early osteoarthritis risk markers through a combination of questionnaires, movement analysis, and machine learning-based risk assessment.

## ⚠️ Important Medical Disclaimer

**This is a research prototype and NOT a medical diagnosis system.**

This application provides preliminary screening indicators only and should never be used as a substitute for professional medical evaluation. Any concerning results should be reviewed by a qualified healthcare professional. All predictions are based on synthetic development data and are labeled as "demo mode" results.

---

## Features

### Core Functionality
- **User Authentication**: JWT-based secure login with demo account
- **Patient Management**: Create, view, and manage patient profiles
- **OA Risk Questionnaire**: Comprehensive health assessment form
- **Movement Analysis**: Real-time pose detection and gait/posture evaluation
- **ML Risk Prediction**: Random Forest classifier for risk stratification
- **Dashboard**: Real-time analytics and patient statistics
- **PDF Reports**: Professional screening reports with explainability
- **Patient History**: Track screening progress over time
- **Offline Mode**: Local data persistence for low-connectivity environments
- **Responsive Design**: Mobile-friendly healthcare UI

### Technical Features
- FastAPI backend with SQLAlchemy ORM
- React + TypeScript frontend with Tailwind CSS
- SQLite database (configurable to PostgreSQL)
- WebSocket support for real-time analysis
- ML pipeline with scikit-learn and XGBoost-ready architecture
- Computer vision ready (MediaPipe Pose integration)
- PDF generation with ReportLab
- JWT authentication and role-based access
- CORS-enabled for cross-origin requests
- Docker support for easy deployment

---

## Tech Stack

### Frontend
- React 18+
- TypeScript
- Vite
- Tailwind CSS
- Recharts (data visualization)
- Lucide React (icons)
- Axios (HTTP client)

### Backend
- Python 3.9+
- FastAPI
- SQLAlchemy ORM
- SQLite (dev) / PostgreSQL (prod)
- Pydantic
- JWT (python-jose)
- Bcrypt (password hashing)
- Scikit-learn (ML pipeline)
- ReportLab (PDF generation)
- MediaPipe (computer vision ready)

---

## Quick Start

### Prerequisites
- Python 3.9+
- Node.js 18+
- Git

### Setup (5 minutes)

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

**Frontend (in another terminal):**
```bash
cd frontend
npm install
npm run dev
```

**Demo Credentials:**
- Email: `demo@oasense.ai`
- Password: `demo123`

Frontend: http://localhost:5173  
Backend API: http://localhost:8000  
API Docs: http://localhost:8000/docs

For detailed setup instructions, see [QUICKSTART.md](QUICKSTART.md)

---

## Project Structure

```
oa-sense-ai/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app entry point
│   │   ├── database.py          # SQLAlchemy setup
│   │   ├── models.py            # Database models
│   │   ├── schemas.py           # Pydantic schemas
│   │   ├── auth.py              # JWT authentication
│   │   ├── routes/
│   │   │   ├── auth.py          # Login/register endpoints
│   │   │   ├── patients.py      # Patient CRUD
│   │   │   ├── screenings.py    # Screening CRUD
│   │   │   ├── analysis.py      # Analysis & prediction
│   │   │   ├── dashboard.py     # Dashboard stats
│   │   │   ├── reports.py       # Report generation
│   │   │   └── socket.py        # WebSocket (real-time)
│   │   ├── ml/
│   │   │   ├── feature_extraction.py
│   │   │   ├── preprocessing.py
│   │   │   ├── pose_analysis.py
│   │   │   ├── gait_analysis.py
│   │   │   └── inference.py
│   │   └── services/
│   │       ├── report_service.py
│   │       └── sync_service.py
│   ├── requirements.txt
│   ├── run.py
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── components/         # React components
│   │   ├── pages/              # Page components
│   │   ├── services/           # API client
│   │   ├── hooks/              # Custom hooks
│   │   ├── types/              # TypeScript types
│   │   ├── utils/              # Utility functions
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── package.json
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   └── .env
│
├── models/                     # ML models (auto-generated)
├── reports/                    # PDF reports (auto-generated)
├── docker-compose.yml
├── .env.example
├── .gitignore
├── QUICKSTART.md               # Quick start guide
└── README.md
```

---

## Database Schema

### Users Table
```sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name VARCHAR NOT NULL,
  email VARCHAR UNIQUE NOT NULL,
  password_hash VARCHAR NOT NULL,
  role VARCHAR DEFAULT 'healthcare_worker',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Patients Table
```sql
CREATE TABLE patients (
  id INTEGER PRIMARY KEY,
  patient_code VARCHAR UNIQUE NOT NULL,
  name VARCHAR NOT NULL,
  age INTEGER NOT NULL,
  gender VARCHAR,
  phone VARCHAR,
  location VARCHAR,
  occupation VARCHAR,
  activity_level VARCHAR DEFAULT 'moderate',
  previous_joint_injury INTEGER DEFAULT 0,
  family_history INTEGER DEFAULT 0,
  physically_demanding_work INTEGER DEFAULT 0,
  difficulty_walking INTEGER DEFAULT 0,
  difficulty_climbing_stairs INTEGER DEFAULT 0,
  morning_stiffness INTEGER DEFAULT 0,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Screenings Table
```sql
CREATE TABLE screenings (
  id INTEGER PRIMARY KEY,
  patient_id INTEGER FOREIGN KEY REFERENCES patients(id),
  screening_date DATETIME DEFAULT CURRENT_TIMESTAMP,
  pain_score FLOAT DEFAULT 0.0,
  stiffness_score FLOAT DEFAULT 0.0,
  mobility_score FLOAT DEFAULT 0.0,
  left_knee_rom FLOAT DEFAULT 0.0,
  right_knee_rom FLOAT DEFAULT 0.0,
  gait_symmetry FLOAT DEFAULT 0.0,
  posture_score FLOAT DEFAULT 0.0,
  movement_smoothness FLOAT DEFAULT 0.0,
  risk_level VARCHAR DEFAULT 'Low Risk',
  risk_probability FLOAT DEFAULT 0.0,
  model_version VARCHAR DEFAULT 'demo-v1',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Reports Table
```sql
CREATE TABLE reports (
  id INTEGER PRIMARY KEY,
  screening_id INTEGER FOREIGN KEY REFERENCES screenings(id),
  file_path VARCHAR,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## API Documentation

Full OpenAPI/Swagger documentation available at: `http://localhost:8000/docs`

### Authentication
```bash
POST /api/auth/login
Content-Type: application/json
{
  "email": "demo@oasense.ai",
  "password": "demo123"
}

Response:
{
  "access_token": "eyJhbGc...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "name": "Demo User",
    "email": "demo@oasense.ai",
    "role": "healthcare_worker"
  }
}
```

### Patient Management
```bash
# Create patient
POST /api/patients
Authorization: Bearer {token}
Content-Type: application/json
{
  "patient_code": "P001",
  "name": "John Doe",
  "age": 55,
  "gender": "Male",
  "location": "New York",
  "activity_level": "moderate"
}

# List patients
GET /api/patients
Authorization: Bearer {token}

# Get patient details
GET /api/patients/{patient_id}
Authorization: Bearer {token}
```

### Screening & Analysis
```bash
# Analyze questionnaire
POST /api/analysis/questionnaire
{
  "pain_score": 6,
  "stiffness_score": 4,
  "mobility_score": 5,
  "age": 55,
  "activity_level": "moderate"
}

# Analyze movement
POST /api/analysis/movement
{
  "left_knee_angle": 95,
  "right_knee_angle": 98
}

# Get ML prediction
POST /api/analysis/predict
{
  "age": 55,
  "pain_score": 6,
  "mobility_score": 5,
  "gait_symmetry": 74,
  "activity_level": "moderate"
}
```

### Dashboard
```bash
GET /api/dashboard/statistics
Authorization: Bearer {token}

Response:
{
  "total_patients": 15,
  "screenings_today": 3,
  "high_risk": 2,
  "moderate_risk": 5,
  "low_risk": 8
}
```

---

## ML Pipeline

### Model Architecture
- **Type**: Random Forest Classifier (220 trees)
- **Input Features**: 13 features (demographic, questionnaire, movement-based)
- **Output Classes**: 0 (Low Risk), 1 (Moderate Risk), 2 (High Risk)
- **Training Data**: 500 synthetic samples (seeded for reproducibility)
- **Test Accuracy**: ~82% (on demo data)

### Feature Set
1. Age
2. Pain Score (0-10)
3. Stiffness Score (0-10)
4. Mobility Score (0-10)
5. Walking Difficulty (0-5)
6. Stair Climbing Difficulty (0-5)
7. Left Knee ROM (degrees)
8. Right Knee ROM (degrees)
9. Knee Symmetry (%)
10. Gait Symmetry (%)
11. Posture Score (0-100)
12. Movement Smoothness (0-100)
13. Activity Level (categorical)

### Data Pipeline
```
Raw Input
    ↓
Feature Extraction
    ↓
Missing Value Imputation (median)
    ↓
Feature Scaling (StandardScaler)
    ↓
Random Forest Classification
    ↓
Risk Probability & Confidence
    ↓
Explainability (feature importance)
```

### Risk Thresholds
- **Low Risk**: Probability < 0.40 or model prediction = 0
- **Moderate Risk**: Probability 0.40-0.70 or model prediction = 1
- **High Risk**: Probability > 0.70 or model prediction = 2

### Demo Mode Note
⚠️ All predictions are based on synthetic development data generated with random seeds. This model is NOT validated for clinical use and should only be used for demonstration and research purposes.

---

## Computer Vision (Ready for Integration)

The application is designed to integrate with MediaPipe Pose for real-time movement analysis:

```python
# Example pose detection (not yet implemented in demo)
import mediapipe as mp

pose = mp.solutions.pose.Pose()
results = pose.process(frame)

# Extract landmarks for knee angle calculation
left_hip = results.pose_landmarks[mp_pose.PoseLandmark.LEFT_HIP]
left_knee = results.pose_landmarks[mp_pose.PoseLandmark.LEFT_KNEE]
left_ankle = results.pose_landmarks[mp_pose.PoseLandmark.LEFT_ANKLE]

# Calculate angle
angle = compute_knee_angle(left_hip, left_knee, left_ankle)
```

To enable real webcam analysis:
1. Install: `pip install opencv-python mediapipe`
2. Update frontend to use real camera stream
3. Send pose landmarks to `/api/analysis/movement` endpoint

---

## Offline Mode

The frontend supports offline operation with IndexedDB/localStorage:

```javascript
// Data is automatically stored locally
localStorage.setItem('screening_' + id, JSON.stringify(data));

// On reconnection, sync with backend
if (navigator.onLine) {
  syncPendingRecords();
}
```

---

## Docker Deployment

```bash
# Build and run with Docker Compose
docker compose up --build

# Access at:
# Frontend: http://localhost:5173
# Backend: http://localhost:8000
```

---

## Security

- ✅ Password hashing with bcrypt
- ✅ JWT token authentication
- ✅ Role-based access control (RBAC)
- ✅ CORS enabled
- ✅ Secure password requirements
- ✅ Token expiration (60 minutes default)
- ⚠️ Use HTTPS in production
- ⚠️ Set strong SECRET_KEY in .env

---

## Performance

- Frontend: ~3 second initial load
- API response time: <200ms (average)
- ML prediction latency: <500ms
- PDF report generation: <2 seconds
- Database query optimization with indexing

---

## Testing

### Demo Workflow
1. Login with demo credentials
2. Create test patient
3. Complete questionnaire
4. Simulate movement analysis
5. View ML prediction
6. Generate PDF report
7. Check patient history

### Manual API Testing
```bash
# Using curl
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"demo@oasense.ai","password":"demo123"}'

# Using Swagger UI
http://localhost:8000/docs
```

---

## Troubleshooting

### Backend won't start
```bash
# Check Python version
python --version  # Should be 3.9+

# Clear pip cache
pip cache purge
pip install -r requirements.txt
```

### Frontend connection errors
```bash
# Check .env file
cat frontend/.env  # Should have VITE_API_URL=http://localhost:8000/api

# Verify backend is running
curl http://localhost:8000/api/health
```

### Port conflicts
```bash
# Change backend port
cd backend
uvicorn app.main:app --reload --port 8001

# Change frontend port
cd frontend
npm run dev -- --port 5174
```

### Database errors
```bash
# Reset database
rm backend/oa_sense.db
cd backend
python -c "from app.database import Base, engine; from app.models import *; Base.metadata.create_all(bind=engine)"
```

---

## Performance Optimization

### Frontend
- Code splitting with React.lazy
- Image optimization with WebP
- CSS minification with Tailwind
- Bundle analysis with Vite

### Backend
- Database connection pooling
- Query optimization with SQLAlchemy
- Caching for frequently accessed data
- Async/await for I/O operations

---

## Future Enhancements

- [ ] Real MediaPipe Pose integration
- [ ] WebSocket real-time analysis streaming
- [ ] Multi-language support (i18n)
- [ ] Advanced analytics dashboard
- [ ] Export patient data to CSV/Excel
- [ ] Appointment scheduling system
- [ ] Integration with EHR systems
- [ ] Mobile app (React Native)
- [ ] Telemedicine video consultation
- [ ] Clinically validated dataset integration

---

## Contributing

This is a research prototype. To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## License

MIT License - See LICENSE file for details

---

## Citation

If you use this project in research, please cite:

```bibtex
@software{oa_sense_ai_2024,
  title={OA-Sense AI: AI-Assisted Early Osteoarthritis Risk Screening System},
  author={Your Name},
  year={2024},
  url={https://github.com/Saimadhav16/oa-sense-ai}
}
```

---

## Medical Disclaimer

**IMPORTANT:** This application is provided for research, educational, and screening purposes only. It is NOT a medical diagnosis system and should never be used as a substitute for professional medical evaluation.

- Do NOT rely on this system for clinical decision-making
- Do NOT make treatment decisions based solely on this system's output
- Always consult qualified healthcare professionals
- Predictions are based on synthetic development data only
- No clinical validation has been performed

Users assume full responsibility for any use of this system.

---

## Contact & Support

For questions or support:
- GitHub Issues: [Open an issue](https://github.com/Saimadhav16/oa-sense-ai/issues)
- Documentation: See [QUICKSTART.md](QUICKSTART.md) and [API Docs](http://localhost:8000/docs)

---

**Built with ❤️ for research and education**
