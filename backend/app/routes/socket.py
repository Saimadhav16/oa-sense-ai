from fastapi import APIRouter, Depends, HTTPException
from fastapi.websockets import WebSocket
from sqlalchemy.orm import Session

from app.database import get_db

router = APIRouter()


@router.websocket('/movement-analysis')
async def movement_analysis_websocket(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_json()
            response = {
                'knee_angle': data.get('left_knee_angle', 90),
                'gait_metrics': {'symmetry': 74},
                'posture_metrics': {'score': 76},
                'movement_status': 'ACTIVE',
            }
            await websocket.send_json(response)
        except Exception:
            break
