from typing import Optional, List

from services.board_service.database import new_session
from services.board_service.column.models import ColumnOrm, ColumnSpaceType
from services.common.schemas.board_service.column_schemas import SColumnCreate, SColumnGet, SColumnSearch, SColumnPatch, \
    SColumnPut
from services.common.utils.repository import Repository


class ColumnRepository:
    @classmethod
    def get_filters(cls, data: SColumnSearch) -> List[bool]:
        filters = []

        if data.space_id:
            filters.append(ColumnOrm.space_id == data.space_id)
        if data.space_type:
            filters.append(ColumnOrm.space_type == data.space_type)
        if data.order:
            filters.append(ColumnOrm.order == data.order)
        if data.name:
            filters.append(ColumnOrm.name == data.name)

        return filters

    @classmethod
    async def create(cls, data: SColumnCreate) -> int:
        return await Repository.create(
            new_session,
            ColumnOrm,
            data,
        )

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
        column = await Repository.get(
            new_session,
            ColumnOrm,
            [ColumnOrm.id == column_id],
            SColumnGet,
        )
        if len(column):
            return column[0]

    @classmethod
    async def get(cls, data: SColumnSearch) -> list[SColumnGet]:
        return await Repository.get(
            new_session,
            ColumnOrm,
            filters,
            SColumnGet,
        )

    @classmethod
    async def delete_one(cls, column_id: int):
        await Repository.delete(
            new_session,
            ColumnOrm,
            [ColumnOrm.id == column_id],
        )

    @classmethod
    async def delete(cls, data: SColumnSearch):
        await Repository.delete(
            new_session,
            ColumnOrm,
            ColumnRepository.get_filters(data),
        )

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
        await Repository.delete(
            new_session,
            ColumnOrm,
            [
                ColumnOrm.space_type == ColumnSpaceType.BOARD,
                ColumnOrm.space_id.in_(board_ids),
            ]
        )

    @classmethod
    async def put(cls, column_id: int, data: SColumnPut):
        await Repository.put(
            new_session,
            ColumnOrm,
            [ColumnOrm.id == column_id],
            data.dict(),
        )

    @classmethod
    async def patch(cls, column_id, data: SColumnPatch):
        await Repository.patch(
            new_session,
            ColumnOrm,
            [ColumnOrm.id == column_id],
            data.dict(exclude_none=True),
        )
