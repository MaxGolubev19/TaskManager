import os

import aiohttp
from fastapi import APIRouter, Body, HTTPException, Request

from services.api_gateway.routers.router import create
from services.common.schemas.user_service.user_schemas import SUserCreate, SUserGet

router = APIRouter(
    tags=["Auth"],
)


@router.post("/auth/jwt/login")
async def login(
        grant_type: str = Body(...),
        username: str = Body(...),
        password: str = Body(...),
        scope: str = Body(...),
        client_id: str = Body(...),
        client_secret: str = Body(...),
):
    async with aiohttp.ClientSession() as client:
        response = await client.post(
            url=f"""{os.getenv("USER_SERVICE_URL")}/auth/jwt/login""",
            data={
                "grant_type": grant_type,
                "username": username,
                "password": password,
                "scope": scope,
                "client_id": client_id,
                "client_secret": client_secret,
            },
            headers={
                "x-api-key": os.getenv("INSIDE_API_KEY"),
            },
        )
    raise HTTPException(
        status_code=response.status,
        detail=await response.text(),
        headers={key: value for key, value in response.headers.items()},
    )


@router.post("/auth/jwt/logout")
async def logout(request: Request):
    async with aiohttp.ClientSession() as client:
        response = await client.post(
            url=f"""{os.getenv("USER_SERVICE_URL")}/auth/jwt/logout""",
            headers={
                "x-api-key": os.getenv("INSIDE_API_KEY"),
                "Cookie": request.headers.get("cookie"),
            },
        )
    raise HTTPException(
        status_code=response.status,
        detail=await response.text(),
        headers={key: value for key, value in response.headers.items()},
    )


@router.post("/auth/register")
async def register(
        data: SUserCreate,
) -> SUserGet:
    return await create(
        url=f"""{os.getenv("USER_SERVICE_URL")}/auth/register""",
        data=data,
        output_type=SUserGet,
    )
