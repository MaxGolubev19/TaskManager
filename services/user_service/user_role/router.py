from typing import Annotated

from fastapi import APIRouter, Depends

from services.common.utils import check_api_key
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
        api_key=Depends(check_api_key),
) -> SUserRoleResult:
    await UserRoleRepository.create(data)
    return SUserRoleResult(
        ok=True,
    )


@router.get("", status_code=200)
async def get_user_roles(
        data: Annotated[SUserRoleSearch, Depends()],
        api_key=Depends(check_api_key),
) -> list[SUserRoleGet]:
    user_roles = await UserRoleRepository.get(data)
    return user_roles


@router.delete("", status_code=200)
async def delete_user_roles(
        data: Annotated[SUserRoleSearch, Depends()],
        api_key=Depends(check_api_key),
) -> SUserRoleResult:
    await UserRoleRepository.delete(data)
    return SUserRoleResult(
        ok=True,
    )


@router.put("", status_code=200)
async def update_user_role(
        data: SUserRolePut,
        api_key=Depends(check_api_key),
) -> SUserRoleResult:
    await UserRoleRepository.put(data)
    return SUserRoleResult(
        ok=True,
    )


@router.patch("", status_code=200)
async def update_user_role(
        data: SUserRolePatch,
        api_key=Depends(check_api_key),
) -> SUserRoleResult:
    await UserRoleRepository.patch(data)
    return SUserRoleResult(
        ok=True,
    )
