from fastapi import FastAPI

from contextlib import asynccontextmanager

from quest_service.quest import router as quest_router
from quest_service.category import router as category_router
from quest_service.column import router as column_roter
from quest_service.board import router as board_router
from quest_service.adventure import router as adventure_router
from quest_service.party import router as party_router

from quest_service.database import create_tables

routers = [
    quest_router,
    category_router,
    column_roter,
    board_router,
    adventure_router,
    party_router,
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)
for router in routers:
    app.include_router(router)
