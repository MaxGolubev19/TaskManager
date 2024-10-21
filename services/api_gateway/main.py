import os

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from fastapi import FastAPI, APIRouter, Depends

from services.api_gateway.routers import user_router, auth_router, role_router, user_role_router, quest_router, \
    dependency_router, category_router, board_router, column_router, adventure_router, party_router
from services.common.utils.api import check_api_key


routers = [
    auth_router,
    user_router,
    role_router,
    user_role_router,
    quest_router,
    dependency_router,
    category_router,
    board_router,
    column_router,
    adventure_router,
    party_router,
]

app = FastAPI()

api_router = APIRouter(prefix="/task-manager")
for router in routers:
    api_router.include_router(router, dependencies=[Depends(check_api_key)])
app.include_router(api_router)


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url(os.getenv("REDIS_URL"), encoding="utf8", decode_responce=True)
    FastAPICache.init(RedisBackend(redis), prefix="api-gateway")
