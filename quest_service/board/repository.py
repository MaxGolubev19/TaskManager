from typing import Optional

from sqlalchemy import select, delete, update

from quest_service.database import new_session
from quest_service.board.models import BoardOrm
from quest_service.board.schemas import SBoardCreate, SBoardGet, SBoardSearch, SBoardUpdate


class BoardRepository:
    @classmethod
    async def create(cls, data: SBoardCreate) -> int:
        async with new_session() as session:
            board = BoardOrm(**data.model_dump())
            session.add(board)
            await session.commit()
            return board.id

    @classmethod
    async def get_by_id(cls, board_id: int) -> Optional[SBoardGet]:
        async with new_session() as session:
            result = await session.execute(
                select(BoardOrm)
                .where(BoardOrm.id == board_id)
            )
            board_model = result.scalars().one_or_none()
            if board_model:
                return SBoardGet.model_validate(board_model)

    @classmethod
    async def get(cls, data: SBoardSearch) -> list[SBoardGet]:
        query = select(BoardOrm)

        if data.name:
            query = query.where(BoardOrm.name == data.name)
        if data.adventure_id:
            query = query.where(BoardOrm.adventure_id == data.adventure_id)
        if data.party_id:
            query = query.where(BoardOrm.party_id == data.party_id)

        async with new_session() as session:
            result = await session.execute(query)
            board_models = result.scalars().all()
            return [SBoardGet.model_validate(board_model) for board_model in board_models]

    @classmethod
    async def delete_by_id(cls, board_id: int):
        async with new_session() as session:
            await session.execute(
                delete(BoardOrm)
                .where(BoardOrm.id == board_id)
            )
            await session.commit()

    @classmethod
    async def delete(cls, data: SBoardSearch):
        query = delete(BoardOrm)

        if data.name:
            query = query.where(BoardOrm.name == data.name)
        if data.adventure_id:
            query = query.where(BoardOrm.adventure_id == data.adventure_id)
        if data.party_id:
            query = query.where(BoardOrm.party_id == data.party_id)

        async with new_session() as session:
            await session.execute(query)
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
