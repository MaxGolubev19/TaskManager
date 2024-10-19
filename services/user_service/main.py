from fastapi import FastAPI, APIRouter, Depends

from contextlib import asynccontextmanager

from services.common.utils.api import check_api_key
from services.user_service.user import router as user_router, auth_router
from services.user_service.role import router as role_router
from services.user_service.user_role import router as user_role_router

from services.user_service.database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)

router = APIRouter(prefix="/user-service")
router.include_router(user_router, dependencies=[Depends(check_api_key)])
router.include_router(auth_router, dependencies=[Depends(check_api_key)])
router.include_router(role_router, dependencies=[Depends(check_api_key)])
router.include_router(user_role_router, dependencies=[Depends(check_api_key)])

app.include_router(router)
