from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from services.board_service.board.repository import BoardRepository
from services.common.schemas.board_service.board_schemas import SBoardCreate, SBoardResult, SBoardGet, SBoardSearch, \
    SBoardPatch, SBoardCreateResult, SBoardPut

router = APIRouter(
    prefix="/boards",
    tags=["Boards"],
)


@router.post("", status_code=201)
async def create_board(
        data: SBoardCreate,
) -> SBoardCreateResult:
    board_id = await BoardRepository.create(data)
    return SBoardCreateResult(
        ok=True,
        id=board_id,
    )


@router.get("/{board_id}")
async def get_board_by_id(
        board_id: int,
) -> SBoardGet:
    board = await BoardRepository.get_one(board_id)
    if board is None:
        raise HTTPException(status_code=404)
    return board


@router.get("")
async def get_boards(
        data: Annotated[SBoardSearch, Depends()],
) -> list[SBoardGet]:
    boards = await BoardRepository.get(data)
    return boards


@router.delete("/{board_id}")
async def delete_board_by_id(
        board_id: int,
) -> SBoardResult:
    await BoardRepository.delete_one(board_id)
    return SBoardResult(
        ok=True,
    )


@router.delete("")
async def delete_boards(
        data: Annotated[SBoardSearch, Depends()],
) -> SBoardResult:
    await BoardRepository.delete(data)
    return SBoardResult(
        ok=True,
    )


@router.put("/{board_id}")
async def update_board(
        board_id: int,
        data: SBoardPut,
) -> SBoardResult:
    await BoardRepository.put(board_id, data)
    return SBoardResult(
        ok=True,
    )


@router.patch("/{board_id}")
async def update_board(
        board_id: int,
        data: SBoardPatch,
) -> SBoardResult:
    await BoardRepository.patch(board_id, data)
    return SBoardResult(
        ok=True,
    )
