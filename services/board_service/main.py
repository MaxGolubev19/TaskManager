from fastapi import FastAPI, APIRouter, Depends

from contextlib import asynccontextmanager

from services.board_service.board import router as board_router
from services.board_service.column import router as column_router

from services.board_service.database import create_tables
from services.common.utils.api import check_api_key


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)

router = APIRouter(prefix="/board-service")
router.include_router(board_router, dependencies=[Depends(check_api_key)])
router.include_router(column_router, dependencies=[Depends(check_api_key)])

app.include_router(router)
