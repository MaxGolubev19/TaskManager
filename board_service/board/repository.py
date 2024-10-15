from typing import Optional

from sqlalchemy import select, delete, update, and_

from board_service.column.repository import ColumnRepository
from board_service.column.schemas import SColumnSearch
from board_service.database import new_session
from board_service.board.models import BoardOrm
from board_service.board.schemas import SBoardCreate, SBoardGet, SBoardSearch, SBoardUpdate


class BoardRepository:
    @classmethod
    async def create(cls, data: SBoardCreate) -> int:
        async with new_session() as session:
            board = BoardOrm(**data.model_dump())
            session.add(board)
            await session.flush()
            await ColumnRepository.create_for_board(data.adventure_id, board.id)
            await session.commit()
            return board.id

    @classmethod
    async def get_one(cls, board_id: int) -> Optional[SBoardGet]:
        async with new_session() as session:
            board = session.get(BoardOrm, board_id)
            if board:
                return SBoardGet.model_validate(board, from_attributes=True)

    @classmethod
    async def get(cls, data: SBoardSearch) -> list[SBoardGet]:
        filters = []

        if data.name:
            filters.append(BoardOrm.name == data.name)
        if data.adventure_id:
            filters.append(BoardOrm.adventure_id == data.adventure_id)
        if data.party_id:
            filters.append(BoardOrm.party_id == data.party_id)

        async with new_session() as session:
            result = await session.execute(
                select(BoardOrm)
                .filter(and_(*filters))
            )
            board_models = result.scalars().all()
            return [SBoardGet.model_validate(board_model, from_attributes=True) for board_model in board_models]

    @classmethod
    async def delete_one(cls, board_id: int):
        async with new_session() as session:
            await session.execute(
                delete(BoardOrm)
                .where(BoardOrm.id == board_id)
            )
            await ColumnRepository.delete_for_board(board_id)
            await session.commit()

    @classmethod
    async def delete(cls, data: SBoardSearch):
        filters = []

        if data.name:
            filters.append(BoardOrm.name == data.name)
        if data.adventure_id:
            filters.append(BoardOrm.adventure_id == data.adventure_id)
        if data.party_id:
            filters.append(BoardOrm.party_id == data.party_id)

        async with new_session() as session:
            deleted = await session.execute(
                select(BoardOrm.id)
                .filter(and_(*filters))
            )
            await session.execute(
                delete(BoardOrm)
                .filter(and_(*filters))
            )
            await ColumnRepository.delete_for_boards(deleted.scalars().all())
            await session.commit()

    @classmethod
    async def update(cls, data: SBoardUpdate):
        query = update(BoardOrm).where(BoardOrm.id == data.id)

        if data.name:
            query = query.values(name=data.name)
        if data.adventure_id:
            query = query.values(adventure_id=data.adventure_id)
        if data.party_id:
            query = query.values(party_id=data.party_id)

        async with new_session() as session:
            await session.execute(query)
            await session.commit()
