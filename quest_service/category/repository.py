from operator import and_
from typing import Optional

from sqlalchemy import select, delete, update

from quest_service.database import new_session
from quest_service.category.models import CategoryOrm
from quest_service.category.schemas import SCategoryCreate, SCategoryGet, SCategorySearch, SCategoryUpdate


class CategoryRepository:
    @classmethod
    async def create(cls, data: SCategoryCreate) -> int:
        async with new_session() as session:
            category = CategoryOrm(**data.model_dump())
            session.add(category)
            await session.commit()
            return category.id

    @classmethod
    async def create_many(cls, data: list[SCategoryCreate]) -> list[int]:
        async with new_session() as session:
            categories = [CategoryOrm(**category.model_dump()) for category in data]
            session.add(categories)
            await session.commit()
            return [category.id for category in categories]

    @classmethod
    async def get_one(cls, category_id: int) -> Optional[SCategoryGet]:
        async with new_session() as session:
            category = session.get(CategoryOrm, category_id)
            if category:
                return SCategoryGet.model_validate(category, from_attributes=True)

    @classmethod
    async def get(cls, data: SCategorySearch) -> list[SCategoryGet]:
        filters = []

        if data.name:
            filters.append(CategoryOrm.name == data.name)
        if data.space_id:
            filters.append(CategoryOrm.space_id == data.space_id)
        if data.space_type:
            filters.append(CategoryOrm.space_type == data.space_type)

        async with new_session() as session:
            result = await session.execute(
                select(CategoryOrm)
                .filter(and_(*filters))
            )
            category_models = result.scalars().all()
            return [SCategoryGet.model_validate(category_model, from_attributes=True) for category_model in category_models]

    @classmethod
    async def delete_one(cls, category_id: int):
        async with new_session() as session:
            await session.execute(
                delete(CategoryOrm)
                .where(CategoryOrm.id == category_id)
            )
            await session.commit()

    @classmethod
    async def delete(cls, data: SCategorySearch):
        filters = []

        if data.name:
            filters.append(CategoryOrm.name == data.name)
        if data.space_id:
            filters.append(CategoryOrm.space_id == data.space_id)
        if data.space_type:
            filters.append(CategoryOrm.space_type == data.space_type)

        async with new_session() as session:
            await session.execute(
                delete(CategoryOrm)
                .filter(and_(*filters))
            )
            await session.commit()

    @classmethod
    async def put(cls, category_id: int, data: SCategoryUpdate):
        async with new_session() as session:
            await session.execute(
                update(CategoryOrm)
                .where(CategoryOrm.id == category_id)
                .values(
                    name=data.name,
                    space_id=data.space_id,
                    space_type=data.space_type,
                )
            )
            await session.commit()

    @classmethod
    async def patch(cls, category_id: int, data: SCategoryUpdate):
        values = {}

        if data.name:
            values['name'] = data.name
        if data.space_id:
            values['space_id'] = data.space_id
        if data.space_type:
            values['space_type'] = data.space_type

        async with new_session() as session:
            await session.execute(
                update(CategoryOrm)
                .where(CategoryOrm.id == category_id)
                .values(**values)
            )
            await session.commit()


