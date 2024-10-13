from typing import Optional

from sqlalchemy import select, delete, update

from user_service.database import new_session
from user_service.role.models import RoleOrm
from user_service.role.schemas import SRoleCreate, SRoleGet, SRoleSearch, SRoleUpdate


class RoleRepository:
    @classmethod
    async def create(cls, data: SRoleCreate) -> int:
        async with new_session() as session:
            role = RoleOrm(**data.model_dump())
            session.add(role)
            await session.commit()
            return role.id

    @classmethod
    async def get_by_id(cls, role_id: int) -> Optional[SRoleGet]:
        async with new_session() as session:
            result = await session.execute(
                select(RoleOrm)
                .where(RoleOrm.id == role_id)
            )
            role_model = result.scalars().one_or_none()
            if role_model:
                return SRoleGet.model_validate(role_model)

    @classmethod
    async def get(cls, data: SRoleSearch) -> list[SRoleGet]:
        query = select(RoleOrm)

        if data.name:
            query = query.where(RoleOrm.name == data.name)
        if data.space_id:
            query = query.where(RoleOrm.space_id == data.space_id)
        if data.space_type:
            query = query.where(RoleOrm.space_type == data.space_type)

        async with new_session() as session:
            result = await session.execute(query)
            role_models = result.scalars().all()
            return [SRoleGet.model_validate(role_model) for role_model in role_models]

    @classmethod
    async def delete_by_id(cls, role_id: int):
        async with new_session() as session:
            await session.execute(
                delete(RoleOrm)
                .where(RoleOrm.id == role_id)
            )
            await session.commit()

    @classmethod
    async def delete(cls, data: SRoleSearch):
        query = delete(RoleOrm)

        if data.name:
            query = query.where(RoleOrm.name == data.name)
        if data.space_id:
            query = query.where(RoleOrm.space_id == data.space_id)
        if data.space_type:
            query = query.where(RoleOrm.space_type == data.space_type)

        async with new_session() as session:
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, data: SRoleUpdate):
        query = update(RoleOrm).where(RoleOrm.id == data.id)

        if data.name:
            query = query.values(name=data.name)
        if data.space_id:
            query = query.values(space_id=data.space_id)
        if data.space_type:
            query = query.values(space_type=data.space_type)

        async with new_session() as session:
            await session.execute(query)
            await session.commit()
