from fastapi import APIRouter, WebSocket

router = APIRouter()


@router.websocket('/movement-analysis')
async def movement_analysis_socket(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_json()
            await websocket.send_json({
                'knee_angle': data.get('left_knee_angle', 90),
                'gait_metrics': {'symmetry': 74},
                'posture_metrics': {'score': 76},
                'movement_status': 'ACTIVE',
            })
        except Exception:
            break
