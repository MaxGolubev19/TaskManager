from services.common.utils.repository import Repository
from services.user_service.database import new_session
from services.user_service.user_role.models import UserRoleOrm
from services.common.schemas.user_service.user_role_schemas import SUserRoleCreate, SUserRoleGet, SUserRoleSearch, \
    SUserRolePatch, SUserRolePut


class UserRoleRepository:
    @classmethod
    def get_filters(cls, data: SUserRoleSearch) -> list:
        filters = []

        if data.user_id:
            filters.append(UserRoleOrm.user_id == data.user_id)
        if data.space_id:
            filters.append(UserRoleOrm.space_id == data.space_id)
        if data.space_type:
            filters.append(UserRoleOrm.space_type == data.space_type)
        if data.role_id:
            filters.append(UserRoleOrm.role_id == data.role_id)

        return filters

    @classmethod
    async def create(cls, data: SUserRoleCreate):
        await Repository.create(
            new_session,
            UserRoleOrm,
            data,
        )

    @classmethod
    async def get(cls, data: SUserRoleSearch) -> list[SUserRoleGet]:
        return await Repository.get(
            new_session,
            UserRoleOrm,
            UserRoleRepository.get_filters(data),
            SUserRoleGet,
        )

    @classmethod
    async def delete(cls, data: SUserRoleSearch):
        await Repository.delete(
            new_session,
            UserRoleOrm,
            UserRoleRepository.get_filters(data),
        )

    @classmethod
    async def put(cls, data: SUserRolePut):
        await Repository.put(
            new_session,
            UserRoleOrm,
            [
                UserRoleOrm.user_id == data.user_id,
                UserRoleOrm.space_id == data.space_id,
                UserRoleOrm.space_type == data.space_type,
            ],
            data.dict(),
        )

    @classmethod
    async def patch(cls, data: SUserRolePatch):
        await Repository.patch(
            new_session,
            UserRoleOrm,
            [
                UserRoleOrm.user_id == data.user_id,
                UserRoleOrm.space_id == data.space_id,
                UserRoleOrm.space_type == data.space_type,
            ],
            data.dict(exclude_none=True),
        )
