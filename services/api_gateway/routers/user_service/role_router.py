import os
from typing import Annotated

import httpx
from fastapi import APIRouter, Depends, HTTPException

from services.common.schemas.user_service.role_schemas import SRoleCreate, SRoleResult, \
    SRoleGet, SRoleSearch, SRoleResult, SRolePut, SRolePatch

router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
)


@router.post("")
async def create_role(
        data: SRoleCreate,
) -> SRoleResult:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=f"""{os.getenv("USER_SERVICE_URL")}/roles""",
            json=data.dict(),
        )
    if response.status_code == 201:
        return SRoleResult.model_validate(response.json())
    raise HTTPException(status_code=500)


@router.get("/{role_id}")
async def get_role(
        role_id: int,
) -> SRoleGet:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=f"""{os.getenv("USER_SERVICE_URL")}/roles/{role_id}""",
        )
    if response.status_code == 404:
        raise HTTPException(status_code=404)
    return SRoleGet.model_validate(response.json(), from_attributes=True)


@router.get("")
async def get_roles(
        data: Annotated[SRoleSearch, Depends()],
) -> list[SRoleGet]:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=f"""{os.getenv("USER_SERVICE_URL")}/roles""",
            params=data.dict(exclude_none=True),
        )
    return [SRoleGet.model_validate(role, from_attributes=True) for role in response.json()]


@router.delete("/{role_id}")
async def delete_role(
        role_id: int,
) -> SRoleResult:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            url=f"""{os.getenv("USER_SERVICE_URL")}/roles/{role_id}""",
        )
    return SRoleResult.model_validate(response.json())


@router.delete("")
async def delete_roles(
        data: Annotated[SRoleSearch, Depends()],
) -> SRoleResult:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            url=f"""{os.getenv("USER_SERVICE_URL")}/roles""",
            params=data.dict(exclude_none=True),
        )
    return SRoleResult.model_validate(response.json())


@router.put("/{role_id}")
async def update_role(
        role_id: int,
        data: SRolePut,
) -> SRoleResult:
    async with httpx.AsyncClient() as client:
        response = await client.put(
            url=f"""{os.getenv("USER_SERVICE_URL")}/roles/{role_id}""",
            json=data.dict(),
        )
    return SRoleResult.model_validate(response.json())


@router.patch("/{role_id}")
async def update_role(
        role_id: int,
        data: SRolePatch,
) -> SRoleResult:
    async with httpx.AsyncClient() as client:
        response = await client.patch(
            url=f"""{os.getenv("USER_SERVICE_URL")}/roles/{role_id}""",
            json=data.dict(),
        )
    return SRoleResult.model_validate(response.json())
