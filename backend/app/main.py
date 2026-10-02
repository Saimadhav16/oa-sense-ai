from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.database import Base, engine
from app.routes import auth, dashboard, patients, reports, screenings, analysis, socket

app = FastAPI(title='OA-Sense AI', version='0.1.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix='/api/auth', tags=['auth'])
app.include_router(patients.router, prefix='/api/patients', tags=['patients'])
app.include_router(screenings.router, prefix='/api/screenings', tags=['screenings'])
app.include_router(analysis.router, prefix='/api/analysis', tags=['analysis'])
app.include_router(dashboard.router, prefix='/api/dashboard', tags=['dashboard'])
app.include_router(reports.router, prefix='/api/reports', tags=['reports'])
app.include_router(socket.router, tags=['websocket'])

@app.get('/api/health')
def health_check():
    return {'status': 'ok', 'service': 'oa-sense-ai'}

@app.get('/')
def root():
    return {'message': 'OA-Sense AI backend is running'}
