from typing import Optional

from sqlalchemy import select, delete, update, and_

from services.board_service.database import new_session
from services.board_service.column.models import ColumnOrm, ColumnSpaceType
from services.common.schemas.board_service.column_schemas import SColumnCreate, SColumnGet, SColumnSearch, SColumnPatch, \
    SColumnPut


class ColumnRepository:
    @classmethod
    async def create(cls, data: SColumnCreate) -> int:
        async with new_session() as session:
            column = ColumnOrm(**data.model_dump())
            session.add(column)
            await session.commit()
            return column.id

    @classmethod
    async def create_many(cls, data: list[SColumnCreate]) -> list[int]:
        async with new_session() as session:
            columns = [ColumnOrm(**column.model_dump()) for column in data]
            session.add_all(columns)
            await session.commit()
            return [column.id for column in columns]

    @classmethod
    async def create_for_board(cls, adventure_id: int, board_id: int):
        columns = await cls.get(SColumnSearch(space_id=adventure_id, space_type=ColumnSpaceType.ADVENTURE))
        await cls.create_many([
            SColumnCreate(
                space_id=board_id,
                space_type=ColumnSpaceType.BOARD,
                order=column.order,
                name=column.name,
            ) for column in columns
        ])

    @classmethod
    async def get_one(cls, column_id: int) -> Optional[SColumnGet]:
        async with new_session() as session:
            column = await session.get(ColumnOrm, column_id)
            if column:
                return SColumnGet.model_validate(column, from_attributes=True)

    @classmethod
    async def get(cls, data: SColumnSearch) -> list[SColumnGet]:
        filters = []

        if data.space_id:
            filters.append(ColumnOrm.space_id == data.space_id)
        if data.space_type:
            filters.append(ColumnOrm.space_type == data.space_type)
        if data.order:
            filters.append(ColumnOrm.order == data.order)
        if data.name:
            filters.append(ColumnOrm.name == data.name)

        async with new_session() as session:
            result = await session.execute(
                select(ColumnOrm)
                .filter(and_(*filters))
            )
            column_models = result.scalars().all()
            return [SColumnGet.model_validate(column_model, from_attributes=True) for column_model in column_models]

    @classmethod
    async def delete_one(cls, column_id: int):
        async with new_session() as session:
            await session.execute(
                delete(ColumnOrm)
                .where(ColumnOrm.id == column_id)
            )
            await session.commit()

    @classmethod
    async def delete(cls, data: SColumnSearch):
        filters = []

        if data.space_id:
            filters.append(ColumnOrm.space_id == data.space_id)
        if data.space_type:
            filters.append(ColumnOrm.space_type == data.space_type)
        if data.order:
            filters.append(ColumnOrm.order == data.order)
        if data.name:
            filters.append(ColumnOrm.name == data.name)

        async with new_session() as session:
            await session.execute(
                delete(ColumnOrm)
                .filter(and_(*filters))
            )
            await session.commit()

    @classmethod
    async def delete_for_board(cls, board_id: int):
        await cls.delete(
            SColumnSearch(
                space_id=board_id,
                space_type=ColumnSpaceType.BOARD,
            )
        )

    @classmethod
    async def delete_for_boards(cls, board_ids: list[int]):
        async with new_session() as session:
            await session.execute(
                delete(ColumnOrm)
                .where(ColumnOrm.space_type == ColumnSpaceType.BOARD)
                .where(ColumnOrm.space_id.in_(board_ids))
            )
            await session.commit()

    @classmethod
    async def put(cls, column_id: int, data: SColumnPut):
        async with new_session() as session:
            await session.execute(
                update(ColumnOrm)
                .where(ColumnOrm.id == column_id)
                .valuse(
                    space_id=data.space_id,
                    space_type=data.space_type,
                    order=data.order,
                    name=data.name,
                )
            )
            await session.commit()

    @classmethod
    async def patch(cls, column_id, data: SColumnPatch):
        values = {}

        if data.space_id:
            values['space_id'] = data.space_id
        if data.space_type:
            values['space_type'] = data.space_type
        if data.order:
            values['order'] = data.order
        if data.name:
            values['name'] = data.name

        async with new_session() as session:
            await session.execute(
                update(ColumnOrm)
                .where(ColumnOrm.id == column_id)
                .values(**values)
            )
            await session.commit()
