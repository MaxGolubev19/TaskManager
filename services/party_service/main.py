from fastapi import FastAPI, APIRouter

from contextlib import asynccontextmanager

from services.party_service.party import router as party_router

from services.party_service.database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)

router = APIRouter(prefix="/party-service")
router.include_router(party_router)

app.include_router(router)
