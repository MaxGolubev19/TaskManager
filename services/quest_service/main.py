from fastapi import FastAPI, APIRouter, Depends

from contextlib import asynccontextmanager

from services.common.utils.api import check_api_key
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
router.include_router(quest_router, dependencies=[Depends(check_api_key)])
router.include_router(dependency_router, dependencies=[Depends(check_api_key)])
router.include_router(category_router, dependencies=[Depends(check_api_key)])

app.include_router(router)
