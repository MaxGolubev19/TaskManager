from typing import Optional, List

from services.board_service.database import new_session
from services.board_service.board.models import BoardOrm
from services.common.schemas.board_service.board_schemas import SBoardCreate, SBoardGet, SBoardSearch, SBoardPatch, \
    SBoardPut
from services.common.utils.repository import Repository


class BoardRepository:
    @classmethod
    def get_filters(cls, data: SBoardSearch) -> List[bool]:
        filters = []

        if data.name:
            filters.append(BoardOrm.name == data.name)
        if data.adventure_id:
            filters.append(BoardOrm.adventure_id == data.adventure_id)
        if data.party_id:
            filters.append(BoardOrm.party_id == data.party_id)

        return filters

    @classmethod
    async def create(cls, data: SBoardCreate) -> int:
        return await Repository.create(
            new_session,
            BoardOrm,
            data,
        )

    @classmethod
    async def get_one(cls, board_id: int) -> Optional[SBoardGet]:
        board = await Repository.get(
            new_session,
            BoardOrm,
            [BoardOrm.id == board_id],
            SBoardGet,
        )
        if len(board):
            return board[0]

    @classmethod
    async def get(cls, data: SBoardSearch) -> list[SBoardGet]:
        return await Repository.get(
            new_session,
            BoardOrm,
            BoardRepository.get_filters(data),
            SBoardGet,
        )

    @classmethod
    async def delete_one(cls, board_id: int):
        await Repository.delete(
            new_session,
            BoardOrm,
            [BoardOrm.id == board_id],
        )

    @classmethod
    async def delete(cls, data: SBoardSearch):
        await Repository.delete(
            new_session,
            BoardOrm,
            BoardRepository.get_filters(data),
        )

    @classmethod
    async def put(cls, board_id: int, data: SBoardPut):
        await Repository.put(
            new_session,
            BoardOrm,
            [BoardOrm.id == board_id],
            data.dict(),
        )

    @classmethod
    async def patch(cls, board_id: int, data: SBoardPatch):
        await Repository.patch(
            new_session,
            BoardOrm,
            [BoardOrm.id == board_id],
            data.dict(exclude_none=True),
        )
