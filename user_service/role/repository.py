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
    async def get_one(cls, role_id: int) -> Optional[SRoleGet]:
        async with new_session() as session:
            role = session.get(RoleOrm, role_id)
            if role:
                return SRoleGet.model_validate(role, from_attributes=True)

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
            return [SRoleGet.model_validate(role_model, from_attributes=True) for role_model in role_models]

    @classmethod
    async def delete_one(cls, role_id: int):
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
    async def put(cls, role_id: int, data: SRoleUpdate):
        async with new_session() as session:
            await session.execute(
                update(RoleOrm)
                .where(RoleOrm.id == role_id)
                .values(
                    name=data.name,
                    space_id=data.space_id,
                    space_type=data.space_type,
                )
            )
            await session.commit()

    @classmethod
    async def patch(cls, role_id: int, data: SRoleUpdate):
        values = {}

        if data.name:
            values['name'] = data.name
        if data.space_id:
            values['space_id'] = data.space_id
        if data.space_type:
            values['space_type'] = data.space_type

        async with new_session() as session:
            await session.execute(
                update(RoleOrm)
                .where(RoleOrm.id == role_id)
                .values(**values)
            )
            await session.commit()
