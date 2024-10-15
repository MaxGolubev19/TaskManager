from typing import Annotated

from fastapi import APIRouter, Depends

from user_service.user_role.repository import UserRoleRepository
from user_service.user_role.schemas import SUserRoleCreate, SUserRoleResult, SUserRoleGet, SUserRoleSearch, \
    SUserRoleUpdate

router = APIRouter(
    prefix='/user_roles',
    tags=["UserRoles"],
)


@router.post("")
async def create_user_role(
        data: Annotated[SUserRoleCreate, Depends()],
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
        data: Annotated[SUserRoleUpdate, Depends()],
) -> SUserRoleResult:
    await UserRoleRepository.put(data)
    return SUserRoleResult(
        ok=True,
    )


@router.patch("")
async def update_user_role(
        data: Annotated[SUserRoleUpdate, Depends()]
) -> SUserRoleResult:
    await UserRoleRepository.patch(data)
    return SUserRoleResult(
        ok=True,
    )
