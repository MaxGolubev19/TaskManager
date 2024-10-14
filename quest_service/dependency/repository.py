from typing import Optional

from sqlalchemy import select, delete, update

from quest_service.database import new_session
from quest_service.dependency.models import DependencyOrm
from quest_service.dependency.schemas import SDependencyCreate, SDependencyGet, SDependencySearch


class DependencyRepository:
    @classmethod
    async def create_dependency(cls, data: SDependencyCreate):
        async with new_session() as session:
            dependency = DependencyOrm(**data.model_dump())
            session.add(dependency)
            await session.commit()

    @classmethod
    async def get_dependencies(cls, data: SDependencySearch) -> list[SDependencyGet]:
        query = select(DependencyOrm)

        if data.parent_id:
            query = query.where(DependencyOrm.parent_id == data.parent_id)
        if data.child_id:
            query = query.where(DependencyOrm.child_id == data.child_id)

        async with new_session() as session:
            result = await session.execute(query)
            dependency_models = result.scalars().all()
            return [SDependencyGet.model_validate(dependency_model) for dependency_model in dependency_models]

    @classmethod
    async def delete_dependencies(cls, data: SDependencySearch):
        query = delete(DependencyOrm)

        if data.parent_id:
            query = query.where(DependencyOrm.parent_id == data.parent_id)
        if data.child_id:
            query = query.where(DependencyOrm.child_id == data.child_id)

        async with new_session() as session:
            await session.execute(query)
            await session.commit()
