from typing import Optional

from services.common.utils.repository import Repository
from services.user_service.user.models import UserOrm
from services.common.schemas.user_service.user_schemas import SUserCreate, SUserGet, SUserSearch, SUserPatch, SUserPut
from services.user_service.database import new_session


class UserRepository:
    @classmethod
    def get_filters(cls, data: SUserSearch) -> list:
        filters = []

        if data.name:
            filters.append(UserOrm.name == data.name)
        if data.role_id:
            filters.append(UserOrm.role_id == data.role_id)
        if data.email:
            filters.append(UserOrm.email == data.email)

        return filters

    @classmethod
    async def get_one(cls, user_id: int) -> Optional[SUserGet]:
        user = await Repository.get(
            new_session,
            UserOrm,
            [UserOrm.id == user_id],
            SUserGet,
        )
        if len(user):
            return user[0]

    @classmethod
    async def get(cls, data: SUserSearch) -> list[SUserGet]:
        return await Repository.get(
            new_session,
            UserOrm,
            UserRepository.get_filters(data),
            SUserGet,
        )

    @classmethod
    async def delete_one(cls, user_id: int):
        await Repository.delete(
            new_session,
            UserOrm,
            [UserOrm.id == user_id],
        )

    @classmethod
    async def delete(cls, data: SUserSearch):
        await Repository.delete(
            new_session,
            UserOrm,
            UserRepository.get_filters(data),
        )

    @classmethod
    async def put(cls, user_id: int, data: SUserPut):
        await Repository.put(
            new_session,
            UserOrm,
            [UserOrm.id == user_id],
            data.dict()
        )

    @classmethod
    async def patch(cls, user_id: int, data: SUserPatch):
        await Repository.patch(
            new_session,
            UserOrm,
            [UserOrm.id == user_id],
            data.dict(exclude_none=True)
        )
