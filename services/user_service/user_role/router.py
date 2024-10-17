from typing import Annotated

from fastapi import APIRouter, Depends

from services.user_service.user_role.repository import UserRoleRepository
from services.common.schemas.user_service.user_role_schemas import SUserRoleCreate, SUserRoleResult, SUserRoleGet, \
    SUserRoleSearch, SUserRolePatch, SUserRolePut

router = APIRouter(
    prefix='/user-role',
    tags=["User-Role"],
)


@router.post("", status_code=201)
async def create_user_role(
        data: SUserRoleCreate,
) -> SUserRoleResult:
    await UserRoleRepository.create(data)
    return SUserRoleResult(
        ok=True,
    )


@router.get("")
async def get_user_roles(
        data: Annotated[SUserRoleSearch, Depends()],
) -> list[SUserRoleGet]:
    user_roles = await UserRoleRepository.get(data)
    return user_roles


@router.delete("")
async def delete_user_roles(
        data: Annotated[SUserRoleSearch, Depends()],
) -> SUserRoleResult:
    await UserRoleRepository.delete(data)
    return SUserRoleResult(
        ok=True,
    )


@router.put("")
async def update_user_role(
        data: SUserRolePut,
) -> SUserRoleResult:
    await UserRoleRepository.put(data)
    return SUserRoleResult(
        ok=True,
    )


@router.patch("")
async def update_user_role(
        data: SUserRolePatch,
) -> SUserRoleResult:
    await UserRoleRepository.patch(data)
    return SUserRoleResult(
        ok=True,
    )
