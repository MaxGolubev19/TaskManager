from fastapi import FastAPI, APIRouter, Depends

from contextlib import asynccontextmanager

from services.adventure_service.adventure import router as adventure_router

from services.adventure_service.database import create_tables
from services.common.utils.api import check_api_key


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)

router = APIRouter(prefix="/adventure-service")
router.include_router(adventure_router, dependencies=[Depends(check_api_key)])

app.include_router(router)
