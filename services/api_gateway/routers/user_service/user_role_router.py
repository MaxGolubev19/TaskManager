import os
from typing import Annotated

from fastapi import APIRouter, Depends

from services.api_gateway.routers.router import create, get, delete, put, patch
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
    return await create(
        url=f"""{os.getenv("USER_SERVICE_URL")}/user-role""",
        data=data,
        output_type=SUserRoleResult
    )


@router.get("")
async def get_user_roles(
        data: Annotated[SUserRoleSearch, Depends()],
) -> list[SUserRoleGet]:
    return await get(
        url=f"""{os.getenv("USER_SERVICE_URL")}/user-role""",
        data=data,
        output_type=SUserRoleGet,
    )


@router.delete("")
async def delete_user_roles(
        data: Annotated[SUserRoleSearch, Depends()],
) -> SUserRoleResult:
    return await delete(
        url=f"""{os.getenv("USER_SERVICE_URL")}/user-role""",
        data=data,
        output_type=SUserRoleResult,
    )


@router.put("")
async def update_user_role(
        data: SUserRolePut,
) -> SUserRoleResult:
    return await put(
        url=f"""{os.getenv("USER_SERVICE_URL")}/user-role""",
        data=data,
        output_type=SUserRoleResult,
    )


@router.patch("")
async def update_user_role(
        data: SUserRolePatch,
) -> SUserRoleResult:
    return await patch(
        url=f"""{os.getenv("USER_SERVICE_URL")}/user-role""",
        data=data,
        output_type=SUserRoleResult,
    )
