from sqlalchemy import select, delete, update

from user_service.database import new_session
from user_service.user_role.models import UserRoleOrm
from user_service.user_role.schemas import SUserRoleCreate, SUserRoleGet, SUserRoleSearch, SUserRoleUpdate


class UserRoleRepository:
    @classmethod
    async def create(cls, data: SUserRoleCreate):
        async with new_session() as session:
            user_role = UserRoleOrm(**data.model_dump())
            session.add(user_role)
            await session.commit()

    @classmethod
    async def get(cls, data: SUserRoleSearch) -> list[SUserRoleGet]:
        query = select(UserRoleOrm)

        if data.user_id:
            query = query.where(UserRoleOrm.user_id == data.user_id)
        if data.space_id:
            query = query.where(UserRoleOrm.space_id == data.space_id)
        if data.space_type:
            query = query.where(UserRoleOrm.space_type == data.space_type)
        if data.role_id:
            query = query.where(UserRoleOrm.role_id == data.role_id)

        async with new_session() as session:
            result = await session.execute(query)
            user_role_models = result.scalars().all()
            return [SUserRoleGet.model_validate(user_role_model) for user_role_model in user_role_models]

    @classmethod
    async def delete(cls, data: SUserRoleSearch):
        query = delete(UserRoleOrm)

        if data.user_id:
            query = query.where(UserRoleOrm.user_id == data.user_id)
        if data.space_id:
            query = query.where(UserRoleOrm.space_id == data.space_id)
        if data.space_type:
            query = query.where(UserRoleOrm.space_type == data.space_type)
        if data.role_id:
            query = query.where(UserRoleOrm.role_id == data.role_id)

        async with new_session() as session:
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, data: SUserRoleUpdate):
        query = update(UserRoleOrm).where(UserRoleOrm.user_id == data.user_id,
                                          UserRoleOrm.space_id == data.space_id,
                                          UserRoleOrm.space_type == data.space_type)

        if data.role_id:
            query = query.values(role_id=data.role_id)

        async with new_session() as session:
            await session.execute(query)
            await session.commit()
