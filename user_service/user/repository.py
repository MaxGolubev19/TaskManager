from typing import Optional

from sqlalchemy import select, delete, update

from user_service.user.models import UserOrm
from user_service.user.schemas import SUserCreate, SUserGet, SUserSearch, SUserUpdate
from user_service.database import new_session



class UserRepository:
    @classmethod
    async def create(cls, data: SUserCreate) -> int:
        async with new_session() as session:
            user = UserOrm(**data.model_dump())
            session.add(user)
            await session.commit()
            return user.id

    @classmethod
    async def get_by_id(cls, user_id: int) -> Optional[SUserGet]:
        async with new_session() as session:
            result = await session.execute(
                select(UserOrm)
                .where(UserOrm.id == user_id)
            )
            user_model = result.scalars().one_or_none()
            if user_model:
                return SUserGet.model_validate(user_model)

    @classmethod
    async def get(cls, data: SUserSearch) -> list[SUserGet]:
        query = select(UserOrm)

        if data.name:
            query = query.where(UserOrm.name == data.name)
        if data.role_id:
            query = query.where(UserOrm.role_id == data.role_id)

        async with new_session() as session:
            result = await session.execute(query)
            user_models = result.scalars().all()
            return [SUserGet.model_validate(user_model) for user_model in user_models]

    @classmethod
    async def delete_by_id(cls, user_id: int):
        async with new_session() as session:
            await session.execute(
                delete(UserOrm)
                .where(UserOrm.id == user_id)
            )
            await session.commit()

    @classmethod
    async def delete(cls, data: SUserSearch):
        query = delete(UserOrm)

        if data.name:
            query = query.where(UserOrm.name == data.name)
        if data.role_id:
            query = query.where(UserOrm.role_id == data.role_id)

        async with new_session() as session:
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, data: SUserUpdate):
        query = update(UserOrm).where(UserOrm.id == data.id)

        if data.name:
            query = query.values(name=data.name)

        async with new_session() as session:
            await session.execute(query)
            await session.commit()
