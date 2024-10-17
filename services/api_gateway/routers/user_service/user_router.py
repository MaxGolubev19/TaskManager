import os
from typing import Annotated

import httpx
from fastapi import APIRouter, Depends, HTTPException

from services.common.schemas.user_service.user_schemas import SUserCreate, SUserResult, \
    SUserGet, SUserSearch, SUserResult, SUserPut, SUserPatch

router = APIRouter(
    prefix="/users",
    tags=["User"],
)


@router.post("")
async def create_user(
        data: SUserCreate,
) -> SUserResult:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=f"""{os.getenv("USER_SERVICE_URL")}/users""",
            json=data.dict(),
        )
    if response.status_code == 201:
        return SUserResult.model_validate(response.json())
    raise HTTPException(status_code=500)


@router.get("/{user_id}")
async def get_user(
        user_id: int,
) -> SUserGet:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=f"""{os.getenv("USER_SERVICE_URL")}/users/{user_id}""",
        )
    if response.status_code == 404:
        raise HTTPException(status_code=404)
    return SUserGet.model_validate(response.json(), from_attributes=True)


@router.get("")
async def get_users(
        data: Annotated[SUserSearch, Depends()],
) -> list[SUserGet]:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=f"""{os.getenv("USER_SERVICE_URL")}/users""",
            params=data.dict(exclude_none=True),
        )
    return [SUserGet.model_validate(user, from_attributes=True) for user in response.json()]


@router.delete("/{user_id}")
async def delete_user(
        user_id: int,
) -> SUserResult:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            url=f"""{os.getenv("USER_SERVICE_URL")}/users/{user_id}""",
        )
    return SUserResult.model_validate(response.json())


@router.delete("")
async def delete_users(
        data: Annotated[SUserSearch, Depends()],
) -> SUserResult:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            url=f"""{os.getenv("USER_SERVICE_URL")}/users""",
            params=data.dict(exclude_none=True),
        )
    return SUserResult.model_validate(response.json())


@router.put("/{user_id}")
async def update_user(
        user_id: int,
        data: SUserPut,
) -> SUserResult:
    async with httpx.AsyncClient() as client:
        response = await client.put(
            url=f"""{os.getenv("USER_SERVICE_URL")}/users/{user_id}""",
            json=data.dict(),
        )
    return SUserResult.model_validate(response.json())


@router.patch("/{user_id}")
async def update_user(
        user_id: int,
        data: SUserPatch,
) -> SUserResult:
    async with httpx.AsyncClient() as client:
        response = await client.patch(
            url=f"""{os.getenv("USER_SERVICE_URL")}/users/{user_id}""",
            json=data.dict(),
        )
    return SUserResult.model_validate(response.json())
