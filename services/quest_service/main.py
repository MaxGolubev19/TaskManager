from fastapi import FastAPI, APIRouter

from contextlib import asynccontextmanager

from services.quest_service.quest import router as quest_router
from services.quest_service.dependency import router as dependency_router
from services.quest_service.category import router as category_router

from services.quest_service.database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)

router = APIRouter(prefix='/quest-service')
router.include_router(quest_router)
router.include_router(dependency_router)
router.include_router(category_router)

app.include_router(router)
