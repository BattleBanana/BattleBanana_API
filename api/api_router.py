from fastapi.routing import APIRouter

from api.v1.api_v1_router import router as api_v1_router

router = APIRouter(
    prefix="/api"
)

router.include_router(api_v1_router)
