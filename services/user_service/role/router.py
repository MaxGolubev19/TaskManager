from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from services.user_service.role.repository import RoleRepository
from services.user_service.role.schemas import SRoleCreate, SRoleResult, SRoleGet, SRoleSearch, SRoleUpdate, SRoleCreateResult

router = APIRouter(
    prefix='/roles',
    tags=["Roles"],
)


@router.post("")
async def create_role(
        data: Annotated[SRoleCreate, Depends()],
) -> SRoleCreateResult:
    role_id = await RoleRepository.create(data)
    return SRoleCreateResult(
        ok=True,
        id=role_id,
    )


@router.get("/{role_id}")
async def get_role_by_id(
        role_id: int,
) -> SRoleGet:
    role = await RoleRepository.get_one(role_id)
    if role is None:
        raise HTTPException(status_code=404)
    return role


@router.get("")
async def get_roles(
        data: Annotated[SRoleSearch, Depends()],
) -> list[SRoleGet]:
    roles = await RoleRepository.get(data)
    return roles


@router.delete("/{role_id}")
async def delete_role_by_id(
        role_id: int,
) -> SRoleResult:
    await RoleRepository.delete_one(role_id)
    return SRoleResult(
        ok=True,
    )


@router.delete("")
async def delete_roles(
        data: Annotated[SRoleSearch, Depends()],
) -> SRoleResult:
    await RoleRepository.delete(data)
    return SRoleResult(
        ok=True,
    )


@router.put("/{role_id}")
async def update_role(
        role_id: int,
        data: Annotated[SRoleUpdate, Depends()],
) -> SRoleResult:
    await RoleRepository.put(role_id, data)
    return SRoleResult(
        ok=True,
    )


@router.patch("/{role_id}")
async def update_role(
        role_id: int,
        data: Annotated[SRoleUpdate, Depends()],
) -> SRoleResult:
    await RoleRepository.patch(role_id, data)
    return SRoleResult(
        ok=True,
    )
