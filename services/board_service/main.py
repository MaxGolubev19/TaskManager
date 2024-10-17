from fastapi import FastAPI, APIRouter

from contextlib import asynccontextmanager

from services.board_service.board import router as board_router
from services.board_service.column import router as column_router

from services.board_service.database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)

router = APIRouter(prefix="/board-service")
router.include_router(board_router)
router.include_router(column_router)

app.include_router(router)
