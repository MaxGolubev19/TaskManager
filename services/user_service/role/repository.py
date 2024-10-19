from typing import Optional

from services.common.utils.repository import Repository
from services.user_service.database import new_session
from services.user_service.role.models import RoleOrm
from services.common.schemas.user_service.role_schemas import SRoleCreate, SRoleGet, SRoleSearch, SRolePatch, SRolePut


class RoleRepository:
    @classmethod
    def get_filters(cls, data: SRoleSearch) -> list:
        filters = []

        if data.name:
            filters.append(RoleOrm.name == data.name)
        if data.space_id:
            filters.append(RoleOrm.space_id == data.space_id)
        if data.space_type:
            filters.append(RoleOrm.space_type == data.space_type)

        return filters

    @classmethod
    async def create(cls, data: SRoleCreate) -> int:
        return await Repository.create(
            new_session,
            RoleOrm,
            data,
        )

    @classmethod
    async def get_one(cls, role_id: int) -> Optional[SRoleGet]:
        role = await Repository.get(
            new_session,
            RoleOrm,
            [RoleOrm.id == role_id],
            SRoleGet,
        )
        if len(role):
            return role[0]

    @classmethod
    async def get(cls, data: SRoleSearch) -> list[SRoleGet]:
        return await Repository.get(
            new_session,
            RoleOrm,
            RoleRepository.get_filters(data),
            SRoleGet,
        )

    @classmethod
    async def delete_one(cls, role_id: int):
        await Repository.delete(
            new_session,
            RoleOrm,
            [RoleOrm.id == role_id],
        )

    @classmethod
    async def delete(cls, data: SRoleSearch):
        await Repository.delete(
            new_session,
            RoleOrm,
            RoleRepository.get_filters(data),
        )

    @classmethod
    async def put(cls, role_id: int, data: SRolePut):
        await Repository.put(
            new_session,
            RoleOrm,
            [RoleOrm.id == role_id],
            data.dict()
        )

    @classmethod
    async def patch(cls, role_id: int, data: SRolePatch):
        await Repository.patch(
            new_session,
            RoleOrm,
            [RoleOrm.id == role_id],
            data.dict(exclude_none=True)
        )
