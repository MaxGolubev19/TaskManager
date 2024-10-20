import os
from typing import Annotated

from fastapi import APIRouter, Depends

from services.api_gateway.routers.router import create, get_one, get, delete_one, delete, put, patch
from services.common.schemas.user_service.user_schemas import SUserCreate, SUserCreateResult, SUserResult, SUserGet, \
    SUserSearch, SUserPut, SUserPatch, SUserCreateResult

router = APIRouter(
    prefix="/users",
    tags=["User"],
)


@router.get("/{user_id}")
async def get_user(
        user_id: int,
) -> SUserGet:
    return await get_one(
        url=f"""{os.getenv("USER_SERVICE_URL")}/users/{user_id}""",
        output_type=SUserGet,
    )


@router.get("")
async def get_users(
        data: Annotated[SUserSearch, Depends()],
) -> list[SUserGet]:
    return await get(
        url=f"""{os.getenv("USER_SERVICE_URL")}/users""",
        data=data,
        output_type=SUserGet,
    )


@router.delete("/{user_id}")
async def delete_user(
        user_id: int,
) -> SUserResult:
    return await delete_one(
        url=f"""{os.getenv("USER_SERVICE_URL")}/users/{user_id}""",
        output_type=SUserResult,
    )


@router.delete("")
async def delete_users(
        data: Annotated[SUserSearch, Depends()],
) -> SUserResult:
    return await delete(
        url=f"""{os.getenv("USER_SERVICE_URL")}/users""",
        data=data,
        output_type=SUserResult,
    )


@router.put("/{user_id}")
async def update_user(
        user_id: int,
        data: SUserPut,
) -> SUserResult:
    return await put(
        url=f"""{os.getenv("USER_SERVICE_URL")}/users/{user_id}""",
        data=data,
        output_type=SUserResult,
    )


@router.patch("/{user_id}")
async def update_user(
        user_id: int,
        data: SUserPatch,
) -> SUserResult:
    return await patch(
        url=f"""{os.getenv("USER_SERVICE_URL")}/users/{user_id}""",
        data=data,
        output_type=SUserResult,
    )
