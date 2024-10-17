from sqlalchemy import select, delete, update, and_

from services.user_service.database import new_session
from services.user_service.user_role.models import UserRoleOrm
from services.common.schemas.user_service.user_role_schemas import SUserRoleCreate, SUserRoleGet, SUserRoleSearch, \
    SUserRolePatch, SUserRolePut


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

        if data.user_name:
            query = query.where(UserRoleOrm.user_name == data.user_name)
        if data.space_id:
            query = query.where(UserRoleOrm.space_id == data.space_id)
        if data.space_type:
            query = query.where(UserRoleOrm.space_type == data.space_type)
        if data.role_id:
            query = query.where(UserRoleOrm.role_id == data.role_id)

        async with new_session() as session:
            result = await session.execute(query)
            user_role_models = result.scalars().all()
            return [SUserRoleGet.model_validate(user_role_model, from_attributes=True) for user_role_model in user_role_models]

    @classmethod
    async def delete(cls, data: SUserRoleSearch):
        filters = []

        if data.user_name:
            filters.append(UserRoleOrm.user_name == data.user_name)
        if data.space_id:
            filters.append(UserRoleOrm.space_id == data.space_id)
        if data.space_type:
            filters.append(UserRoleOrm.space_type == data.space_type)
        if data.role_id:
            filters.append(UserRoleOrm.role_id == data.role_id)

        async with new_session() as session:
            await session.execute(
                delete(UserRoleOrm)
                .filter(and_(*filters))
            )
            await session.commit()

    @classmethod
    async def put(cls, data: SUserRolePut):
        async with new_session() as session:
            await session.execute(
                update(UserRoleOrm)
                .where(
                    UserRoleOrm.user_name == data.user_name,
                    UserRoleOrm.space_id == data.space_id,
                    UserRoleOrm.space_type == data.space_type
                ).values(
                    role_id=data.role_id,
                )
            )
            await session.commit()

    @classmethod
    async def patch(cls, data: SUserRolePatch):
        values = {}

        if data.role_id:
            values['role_id'] = data.role_id

        async with new_session() as session:
            await session.execute(
                update(UserRoleOrm).where(
                    UserRoleOrm.user_name == data.user_name,
                    UserRoleOrm.space_id == data.space_id,
                    UserRoleOrm.space_type == data.space_type
                ).values(**values)
            )
            await session.commit()
