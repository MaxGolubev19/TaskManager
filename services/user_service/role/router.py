from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from services.common.utils import check_api_key
from services.user_service.role.repository import RoleRepository
from services.common.schemas.user_service.role_schemas import SRoleCreate, SRoleResult, SRoleGet, SRoleSearch, \
    SRolePatch, \
    SRoleCreateResult, SRolePut

router = APIRouter(
    prefix='/roles',
    tags=["Roles"],
)


@router.post("", status_code=201)
async def create_role(
        data: SRoleCreate,
        api_key=Depends(check_api_key),
) -> SRoleCreateResult:
    role_id = await RoleRepository.create(data)
    return SRoleCreateResult(
        ok=True,
        id=role_id,
    )


@router.get("/{role_id}", status_code=200)
async def get_role_by_id(
        role_id: int,
        api_key=Depends(check_api_key),
) -> SRoleGet:
    role = await RoleRepository.get_one(role_id)
    if role is None:
        raise HTTPException(status_code=404)
    return role


@router.get("", status_code=200)
async def get_roles(
        data: Annotated[SRoleSearch, Depends()],
        api_key=Depends(check_api_key),
) -> list[SRoleGet]:
    roles = await RoleRepository.get(data)
    return roles


@router.delete("/{role_id}", status_code=200)
async def delete_role_by_id(
        role_id: int,
        api_key=Depends(check_api_key),
) -> SRoleResult:
    await RoleRepository.delete_one(role_id)
    return SRoleResult(
        ok=True,
    )


@router.delete("", status_code=200)
async def delete_roles(
        data: Annotated[SRoleSearch, Depends()],
        api_key=Depends(check_api_key),
) -> SRoleResult:
    await RoleRepository.delete(data)
    return SRoleResult(
        ok=True,
    )


@router.put("/{role_id}", status_code=200)
async def update_role(
        role_id: int,
        data: SRolePut,
        api_key=Depends(check_api_key),
) -> SRoleResult:
    await RoleRepository.put(role_id, data)
    return SRoleResult(
        ok=True,
    )


@router.patch("/{role_id}", status_code=200)
async def update_role(
        role_id: int,
        data: SRolePatch,
        api_key=Depends(check_api_key),
) -> SRoleResult:
    await RoleRepository.patch(role_id, data)
    return SRoleResult(
        ok=True,
    )
