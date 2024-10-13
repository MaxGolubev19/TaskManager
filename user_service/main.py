from fastapi import FastAPI

from contextlib import asynccontextmanager

from user_service.user import router as user_router
from user_service.role import router as role_router

from user_service.database import create_tables

routers = [
    user_router,
    role_router,
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)
for router in routers:
    app.include_router(router)
