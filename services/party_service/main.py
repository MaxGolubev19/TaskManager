from fastapi import FastAPI

from contextlib import asynccontextmanager

from services.party_service.party import router as party_router

from services.party_service.database import create_tables

routers = [
    party_router,
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)
for router in routers:
    app.include_router(router)
