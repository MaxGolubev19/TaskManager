import os
from typing import Annotated

import httpx
from fastapi import APIRouter, Depends, HTTPException

from services.common.schemas.board_service.board_schemas import SBoardCreate, SBoardCreateResult, SBoardGet, \
    SBoardSearch, SBoardResult, SBoardPut, SBoardPatch

router = APIRouter(
    prefix="/boards",
    tags=["Boards"],
)


@router.post("")
async def create_board(
        data: Annotated[SBoardCreate, Depends()],
) -> SBoardCreateResult:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=f"""{os.getenv("BOARD_SERVICE_URL")}/boards""",
            json=data.dict(),
        )
    if response.status_code == 201:
        return SBoardCreateResult.model_validate(response.json())
    raise HTTPException(status_code=500)


@router.get("/{board_id}")
async def get_board(
        board_id: int,
) -> SBoardGet:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=f"""{os.getenv("BOARD_SERVICE_URL")}/boards/{board_id}""",
        )
    if response.status_code == 404:
        raise HTTPException(status_code=404)
    return SBoardGet.model_validate(response.json(), from_attributes=True)


@router.get("")
async def get_boards(
        data: Annotated[SBoardSearch, Depends()],
) -> list[SBoardGet]:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=f"""{os.getenv("BOARD_SERVICE_URL")}/boards""",
            params=data.dict(exclude_none=True),
        )
    return [SBoardGet.model_validate(board, from_attributes=True) for board in response.json()]


@router.delete("/{board_id}")
async def delete_board(
        board_id: int,
) -> SBoardResult:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            url=f"""{os.getenv("BOARD_SERVICE_URL")}/boards/{board_id}""",
        )
    return SBoardResult.model_validate(response.json())


@router.delete("")
async def delete_boards(
        data: Annotated[SBoardSearch, Depends()],
) -> SBoardResult:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            url=f"""{os.getenv("BOARD_SERVICE_URL")}/boards""",
            params=data.dict(exclude_none=True),
        )
    return SBoardResult.model_validate(response.json())


@router.put("/{board_id}")
async def update_board(
        board_id: int,
        data: Annotated[SBoardPut, Depends()],
) -> SBoardResult:
    async with httpx.AsyncClient() as client:
        response = await client.put(
            url=f"""{os.getenv("BOARD_SERVICE_URL")}/boards/{board_id}""",
            json=data.dict(),
        )
    return SBoardResult.model_validate(response.json())


@router.patch("/{board_id}")
async def update_board(
        board_id: int,
        data: Annotated[SBoardPatch, Depends()],
) -> SBoardResult:
    async with httpx.AsyncClient() as client:
        response = await client.patch(
            url=f"""{os.getenv("BOARD_SERVICE_URL")}/boards/{board_id}""",
            json=data.dict(),
        )
    return SBoardResult.model_validate(response.json())
