from fastapi import FastAPI

from contextlib import asynccontextmanager

from services.adventure_service.adventure import router as adventure_router

from services.adventure_service.database import create_tables

routers = [
    adventure_router,
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)
for router in routers:
    app.include_router(router)
