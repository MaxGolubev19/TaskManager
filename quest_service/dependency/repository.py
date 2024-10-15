from sqlalchemy import select, delete, and_

from quest_service.database import new_session
from quest_service.dependency.models import DependencyOrm
from quest_service.dependency.schemas import SDependencyCreate, SDependencyGet, SDependencySearch


class DependencyRepository:
    @classmethod
    async def create(cls, data: SDependencyCreate):
        async with new_session() as session:
            dependency = DependencyOrm(**data.model_dump())
            session.add(dependency)
            await session.commit()

    @classmethod
    async def get(cls, data: SDependencySearch) -> list[SDependencyGet]:
        filters = []

        if data.parent_id:
            filters.append(DependencyOrm.parent_id == data.parent_id)
        if data.child_id:
            filters.append(DependencyOrm.child_id == data.child_id)

        async with new_session() as session:
            result = await session.execute(
                select(DependencyOrm)
                .filter(and_(*filters))
            )
            dependency_models = result.scalars().all()
            return [SDependencyGet.model_validate(dependency_model, from_attributes=True) for dependency_model in dependency_models]

    @classmethod
    async def delete(cls, data: SDependencySearch):
        filters = []

        if data.parent_id:
            filters.append(DependencyOrm.parent_id == data.parent_id)
        if data.child_id:
            filters.append(DependencyOrm.child_id == data.child_id)

        async with new_session() as session:
            await session.execute(
                delete(DependencyOrm)
                .filter(and_(*filters))
            )
            await session.commit()
