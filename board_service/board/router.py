from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from board_service.board.repository import BoardRepository
from board_service.board.schemas import SBoardCreate, SBoardResult, SBoardGet, SBoardSearch, SBoardUpdate, SBoardCreateResult

router = APIRouter(
    prefix='/boards',
    tags=["Boards"],
)


@router.post("")
async def create_board(
        data: Annotated[SBoardCreate, Depends()]
) -> SBoardCreateResult:
    board_id = await BoardRepository.create(data)
    return SBoardCreateResult(
        ok=True,
        id=board_id,
    )


@router.get("/{board_id}")
async def get_board_by_id(board_id: int) -> SBoardGet:
    board = await BoardRepository.get_one(board_id)
    if board is None:
        raise HTTPException(status_code=404)
    return board


@router.get("")
async def get_boards(
        data: Annotated[SBoardSearch, Depends()]
) -> list[SBoardGet]:
    boards = await BoardRepository.get(data)
    return boards


@router.delete("/{board_id}")
async def delete_board_by_id(board_id: int) -> SBoardResult:
    await BoardRepository.delete_one(board_id)
    return SBoardResult(
        ok=True,
    )


@router.delete("")
async def delete_boards(
        data: Annotated[SBoardSearch, Depends()]
) -> SBoardResult:
    await BoardRepository.delete(data)
    return SBoardResult(
        ok=True,
    )


@router.patch("")
async def update_board(
        data: Annotated[SBoardUpdate, Depends()]
) -> SBoardResult:
    await BoardRepository.update(data)
    return SBoardResult(
        ok=True,
    )
