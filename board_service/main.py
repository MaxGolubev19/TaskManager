from fastapi import FastAPI

from contextlib import asynccontextmanager

from board_service.board import router as board_router
from board_service.column import router as column_router

from board_service.database import create_tables

routers = [
    board_router,
    column_router,
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)
for router in routers:
    app.include_router(router)
