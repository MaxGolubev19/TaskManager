from typing import Optional

from sqlalchemy import select, delete, update

from board_service.database import new_session
from board_service.column.models import ColumnOrm
from board_service.column.schemas import SColumnCreate, SColumnGet, SColumnSearch, SColumnUpdate


class ColumnRepository:
    @classmethod
    async def create(cls, data: SColumnCreate) -> int:
        async with new_session() as session:
            column = ColumnOrm(**data.model_dump())
            session.add(column)
            await session.commit()
            return column.id

    @classmethod
    async def get_by_id(cls, column_id: int) -> Optional[SColumnGet]:
        async with new_session() as session:
            result = await session.execute(
                select(ColumnOrm)
                .where(ColumnOrm.id == column_id)
            )

            column_model = result.scalars().one_or_none()
            if column_model:
                return SColumnGet.model_validate(column_model)

    @classmethod
    async def get(cls, data: SColumnSearch) -> list[SColumnGet]:
        query = select(ColumnOrm)

        if data.space_id:
            query = query.where(ColumnOrm.space_id == data.space_id)
        if data.space_type:
            query = query.where(ColumnOrm.space_type == data.space_type)
        if data.order:
            query = query.where(ColumnOrm.order == data.order)
        if data.name:
            query = query.where(ColumnOrm.name == data.name)

        async with new_session() as session:
            result = await session.execute(query)
            column_models = result.scalars().all()
            return [SColumnGet.model_validate(column_model) for column_model in column_models]

    @classmethod
    async def delete_by_id(cls, column_id: int):
        async with new_session() as session:
            await session.execute(
                delete(ColumnOrm)
                .where(ColumnOrm.id == column_id)
            )
            await session.commit()

    @classmethod
    async def delete(cls, data: SColumnSearch):
        query = delete(ColumnOrm)

        if data.space_id:
            query = query.where(ColumnOrm.space_id == data.space_id)
        if data.space_type:
            query = query.where(ColumnOrm.space_type == data.space_type)
        if data.order:
            query = query.where(ColumnOrm.order == data.order)
        if data.name:
            query = query.where(ColumnOrm.name == data.name)

        async with new_session() as session:
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, data: SColumnUpdate):
        query = update(ColumnOrm).where(ColumnOrm.id == data.id)

        if data.space_id:
            query = query.values(space_id=data.space_id)
        if data.space_type:
            query = query.values(space_type=data.space_type)
        if data.order:
            query = query.values(order=data.order)
        if data.name:
            query = query.values(name=data.name)

        async with new_session() as session:
            await session.execute(query)
            await session.commit()
