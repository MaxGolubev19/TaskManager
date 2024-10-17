import os
from typing import Annotated

import httpx
from fastapi import APIRouter, Depends, HTTPException

from services.common.schemas.user_service.user_role_schemas import SUserRoleCreate, SUserRoleGet, SUserRoleSearch, \
    SUserRoleResult, SUserRolePut, SUserRolePatch

router = APIRouter(
    prefix="/user-role",
    tags=["User-Role"],
)


@router.post("")
async def create_user_role(
        data: SUserRoleCreate,
) -> SUserRoleResult:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=f"""{os.getenv("USER_SERVICE_URL")}/user-role""",
            json=data.dict(),
        )
    if response.status_code == 201:
        return SUserRoleResult.model_validate(response.json())
    raise HTTPException(status_code=500)


@router.get("")
async def get_user_roles(
        data: Annotated[SUserRoleSearch, Depends()],
) -> list[SUserRoleGet]:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=f"""{os.getenv("USER_SERVICE_URL")}/user-role""",
            params=data.dict(exclude_none=True),
        )
    return [SUserRoleGet.model_validate(user_role, from_attributes=True) for user_role in response.json()]


@router.delete("")
async def delete_user_roles(
        data: Annotated[SUserRoleSearch, Depends()],
) -> SUserRoleResult:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            url=f"""{os.getenv("USER_SERVICE_URL")}/user-role""",
            params=data.dict(exclude_none=True),
        )
    return SUserRoleResult.model_validate(response.json())


@router.put("")
async def update_user_role(
        data: SUserRolePut,
) -> SUserRoleResult:
    async with httpx.AsyncClient() as client:
        response = await client.put(
            url=f"""{os.getenv("USER_SERVICE_URL")}/user-role""",
            json=data.dict(),
        )
    return SUserRoleResult.model_validate(response.json())


@router.patch("")
async def update_user_role(
        data: SUserRolePatch,
) -> SUserRoleResult:
    async with httpx.AsyncClient() as client:
        response = await client.patch(
            url=f"""{os.getenv("USER_SERVICE_URL")}/user-role""",
            json=data.dict(),
        )
    return SUserRoleResult.model_validate(response.json())
