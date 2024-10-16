from typing import Optional

from sqlalchemy import select, delete, update, and_

from services.user_service.user.models import UserOrm
from services.common.schemas.user_service.user_schemas import SUserCreate, SUserGet, SUserSearch, SUserPatch, SUserPut
from services.user_service.database import new_session


class UserRepository:
    @classmethod
    async def create(cls, data: SUserCreate):
        async with new_session() as session:
            user = UserOrm(**data.model_dump())
            session.add(user)
            await session.commit()

    @classmethod
    async def get_one(cls, user_name: str) -> Optional[SUserGet]:
        async with new_session() as session:
            user = await session.get(UserOrm, user_name)
            if user:
                return SUserGet.model_validate(user, from_attributes=True)

    @classmethod
    async def get(cls, data: SUserSearch) -> list[SUserGet]:
        query = select(UserOrm)

        if data.role_id:
            query = query.where(UserOrm.role_id == data.role_id)

        async with new_session() as session:
            result = await session.execute(query)
            user_models = result.scalars().all()
            return [SUserGet.model_validate(user_model, from_attributes=True) for user_model in user_models]

    @classmethod
    async def delete_one(cls, user_name: str):
        async with new_session() as session:
            await session.execute(
                delete(UserOrm)
                .where(UserOrm.name == user_name)
            )
            await session.commit()

    @classmethod
    async def delete(cls, data: SUserSearch):
        filters = []

        if data.role_id:
            filters.append(UserOrm.role_id == data.role_id)

        async with new_session() as session:
            await session.execute(
                delete(UserOrm)
                .filter(and_(*filters))
            )
            await session.commit()

    @classmethod
    async def put(cls, user_name: str, data: SUserPut):
        async with new_session() as session:
            await session.execute(
                update(UserOrm)
                .where(UserOrm.name == user_name)
                .values(
                    role_id=data.role_id,
                )
            )
            await session.commit()

    @classmethod
    async def patch(cls, user_name: str, data: SUserPatch):
        values = {}

        if data.role_id:
            values['role_id'] = data.role_id

        async with new_session() as session:
            await session.execute(
                update(UserOrm)
                .where(UserOrm.name == user_name)
                .values(**values)
            )
            await session.commit()
