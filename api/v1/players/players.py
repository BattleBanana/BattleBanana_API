from typing import Any, Dict
from fastapi.routing import APIRouter

router = APIRouter(prefix="/players")

@router.get("/{id}")
async def get_player(id: int) -> Dict[str, Any]:
    return {"player_id": id}

@router.post("/transfer/bb")
async def transfer_from_theel(player_id: int): # -> BBPlayer:
    return {"player_id": player_id}

@router.post("/transfer/theel")
async def transfer_from_bb(player_id: int): # -> TheelPlayer:
    return {"player_id": player_id}