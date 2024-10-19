import os
from typing import Annotated

from fastapi import APIRouter, Depends

from services.api_gateway.routers.router import create, get_one, get, delete_one, delete, put, patch
from services.common.schemas.user_service.role_schemas import SRoleCreate, SRoleResult, SRoleGet, SRoleSearch, \
    SRolePut, SRolePatch

router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
)


@router.post("")
async def create_role(
        data: SRoleCreate,
) -> SRoleResult:
    return await create(
        url=f"""{os.getenv("USER_SERVICE_URL")}/roles""",
        data=data,
        output_type=SRoleResult,
    )


@router.get("/{role_id}")
async def get_role(
        role_id: int,
) -> SRoleGet:
    return await get_one(
        url=f"""{os.getenv("USER_SERVICE_URL")}/roles/{role_id}""",
        output_type=SRoleGet,
    )


@router.get("")
async def get_roles(
        data: Annotated[SRoleSearch, Depends()],
) -> list[SRoleGet]:
    return await get(
        url=f"""{os.getenv("USER_SERVICE_URL")}/roles""",
        data=data,
        output_type=SRoleGet,
    )


@router.delete("/{role_id}")
async def delete_role(
        role_id: int,
) -> SRoleResult:
    return await delete_one(
        url=f"""{os.getenv("USER_SERVICE_URL")}/roles/{role_id}""",
        output_type=SRoleResult,
    )


@router.delete("")
async def delete_roles(
        data: Annotated[SRoleSearch, Depends()],
) -> SRoleResult:
    return await delete(
        url=f"""{os.getenv("USER_SERVICE_URL")}/roles""",
        data=data,
        output_type=SRoleResult,
    )


@router.put("/{role_id}")
async def update_role(
        role_id: int,
        data: SRolePut,
) -> SRoleResult:
    return await put(
        url=f"""{os.getenv("USER_SERVICE_URL")}/roles/{role_id}""",
        data=data,
        output_type=SRoleResult,
    )


@router.patch("/{role_id}")
async def update_role(
        role_id: int,
        data: SRolePatch,
) -> SRoleResult:
    return await patch(
        url=f"""{os.getenv("USER_SERVICE_URL")}/roles/{role_id}""",
        data=data,
        output_type=SRoleResult,
    )
