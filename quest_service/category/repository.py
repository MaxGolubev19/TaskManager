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
    async def get_by_id(cls, category_id: int) -> Optional[SCategoryGet]:
        async with new_session() as session:
            result = await session.execute(
                select(CategoryOrm)
                .where(CategoryOrm.id == category_id)
            )

            category_model = result.scalars().one_or_none()
            if category_model:
                return SCategoryGet.model_validate(category_model)

    @classmethod
    async def get(cls, data: SCategorySearch) -> list[SCategoryGet]:
        query = select(CategoryOrm)

        if data.name:
            query = query.where(CategoryOrm.name == data.name)
        if data.space_id:
            query = query.where(CategoryOrm.space_id == data.space_id)
        if data.space_type:
            query = query.where(CategoryOrm.space_type == data.space_type)

        async with new_session() as session:
            result = await session.execute(query)
            category_models = result.scalars().all()
            return [SCategoryGet.model_validate(category_model) for category_model in category_models]

    @classmethod
    async def delete_by_id(cls, category_id: int):
        async with new_session() as session:
            await session.execute(
                delete(CategoryOrm)
                .where(CategoryOrm.id == category_id)
            )
            await session.commit()

    @classmethod
    async def delete(cls, data: SCategorySearch):
        query = delete(CategoryOrm)

        if data.name:
            query = query.where(CategoryOrm.name == data.name)
        if data.space_id:
            query = query.where(CategoryOrm.space_id == data.space_id)
        if data.space_type:
            query = query.where(CategoryOrm.space_type == data.space_type)

        async with new_session() as session:
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, data: SCategoryUpdate):
        query = update(CategoryOrm).where(CategoryOrm.id == data.id)

        if data.name:
            query = query.values(name=data.name)
        if data.space_id:
            query = query.values(space_id=data.space_id)
        if data.space_type:
            query = query.values(space_type=data.space_type)

        async with new_session() as session:
            await session.execute(query)
            await session.commit()


