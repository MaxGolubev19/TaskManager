from typing import Optional, List

from services.common.utils.repository import Repository
from services.quest_service.database import new_session
from services.quest_service.category.models import CategoryOrm
from services.common.schemas.quest_service.category_schemas import SCategoryCreate, SCategoryGet, SCategorySearch, \
    SCategoryPatch, SCategoryPut


class CategoryRepository:
    @classmethod
    def get_filters(cls, data: SCategorySearch) -> List[bool]:
        filters = []

        if data.name:
            filters.append(CategoryOrm.name == data.name)
        if data.space_id:
            filters.append(CategoryOrm.space_id == data.space_id)
        if data.space_type:
            filters.append(CategoryOrm.space_type == data.space_type)

        return filters

    @classmethod
    async def create(cls, data: SCategoryCreate) -> int:
        return await Repository.create(
            new_session,
            CategoryOrm,
            data,
        )

    @classmethod
    async def create_many(cls, data: list[SCategoryCreate]) -> list[int]:
        async with new_session() as session:
            categories = [CategoryOrm(**category.model_dump()) for category in data]
            session.add(categories)
            await session.commit()
            return [category.id for category in categories]

    @classmethod
    async def get_one(cls, category_id: int) -> Optional[SCategoryGet]:
        category = await Repository.get(
            new_session,
            CategoryOrm,
            [CategoryOrm.id == category_id],
            SCategoryGet,
        )
        if len(category):
            return category[0]

    @classmethod
    async def get(cls, data: SCategorySearch) -> list[SCategoryGet]:
        return await Repository.get(
            new_session,
            CategoryOrm,
            CategoryRepository.get_filters(data),
            SCategoryGet,
        )

    @classmethod
    async def delete_one(cls, category_id: int):
        await Repository.delete(
            new_session,
            CategoryOrm,
            [CategoryOrm.id == category_id],
        )

    @classmethod
    async def delete(cls, data: SCategorySearch):
        await Repository.delete(
            new_session,
            CategoryOrm,
            CategoryRepository.get_filters(data),
        )

    @classmethod
    async def put(cls, category_id: int, data: SCategoryPut):
        await Repository.put(
            new_session,
            CategoryOrm,
            [CategoryOrm.id == category_id],
            data.dict(),
        )

    @classmethod
    async def patch(cls, category_id: int, data: SCategoryPatch):
        values = {}

        if data.name:
            values['name'] = data.name
        if data.space_id:
            values['space_id'] = data.space_id
        if data.space_type:
            values['space_type'] = data.space_type

        await Repository.patch(
            new_session,
            CategoryOrm,
            [CategoryOrm.id == category_id],
            data.dict(exclude_none=True),
        )
