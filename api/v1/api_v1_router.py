
from fastapi.routing import APIRouter

from .players import players

router = APIRouter(
    prefix="/v1",
)

router.include_router(players.router)
