from fastapi import FastAPI

from contextlib import asynccontextmanager

from services.quest_service.quest import router as quest_router
from services.quest_service.dependency import router as dependency_router
from services.quest_service.category import router as category_router

from services.quest_service.database import create_tables

routers = [
    quest_router,
    dependency_router,
    category_router,
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)
for router in routers:
    app.include_router(router)
