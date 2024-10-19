from sqlalchemy import select, delete, and_

from services.common.utils.repository import Repository
from services.quest_service.database import new_session
from services.quest_service.dependency.models import DependencyOrm
from services.common.schemas.quest_service.dependency_schemas import SDependencyCreate, SDependencyGet, SDependencySearch


class DependencyRepository:
    @classmethod
    def get_filters(cls, data: SDependencySearch):
        filters = []

        if data.parent_id:
            filters.append(DependencyOrm.parent_id == data.parent_id)
        if data.child_id:
            filters.append(DependencyOrm.child_id == data.child_id)

        return filters

    @classmethod
    async def create(cls, data: SDependencyCreate):
        async with new_session() as session:
            dependency = DependencyOrm(**data.model_dump())
            session.add(dependency)
            await session.commit()

    @classmethod
    async def get(cls, data: SDependencySearch) -> list[SDependencyGet]:
        return await Repository.get(
            new_session,
            DependencyOrm,
            DependencyRepository.get_filters(data),
            SDependencyGet,
        )

    @classmethod
    async def delete(cls, data: SDependencySearch):
        await Repository.delete(
            new_session,
            DependencyOrm,
            DependencyRepository.get_filters(data),
        )
