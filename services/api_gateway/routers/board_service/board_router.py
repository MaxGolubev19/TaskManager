import os
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache

from services.api_gateway.routers.router import create, get_one, get, delete_one, delete, put, patch
from services.common.schemas.board_service.board_schemas import SBoardCreate, SBoardCreateResult, SBoardGet, \
    SBoardResult, SBoardSearch, SBoardPut, SBoardPatch
from services.common.utils.api import check_api_key

router = APIRouter(
    prefix="/boards",
    tags=["Boards"],
)


@router.post("")
async def create_board(
        data: SBoardCreate,
        api_key: str = Depends(check_api_key),
) -> SBoardCreateResult:
    return await create(
        url=f"""{os.getenv("BOARD_SERVICE_URL")}/boards""",
        data=data,
        output_type=SBoardCreateResult,
    )


@router.get("/{board_id}")
@cache(expire=60)
async def get_board(
        board_id: int,
        api_key: str = Depends(check_api_key),
) -> SBoardGet:
    return await get_one(
        url=f"""{os.getenv("BOARD_SERVICE_URL")}/boards/{board_id}""",
        output_type=SBoardGet,
    )


@router.get("")
@cache(expire=60)
async def get_boards(
        data: Annotated[SBoardSearch, Depends()],
        api_key: str = Depends(check_api_key),
) -> list[SBoardGet]:
    return await get(
        url=f"""{os.getenv("BOARD_SERVICE_URL")}/boards""",
        data=data,
        output_type=SBoardGet,
    )


@router.delete("/{board_id}")
async def delete_board(
        board_id: int,
        api_key: str = Depends(check_api_key),
) -> SBoardResult:
    return await delete_one(
        url=f"""{os.getenv("BOARD_SERVICE_URL")}/boards/{board_id}""",
        output_type=SBoardResult,
    )


@router.delete("")
async def delete_boards(
        data: Annotated[SBoardSearch, Depends()],
        api_key: str = Depends(check_api_key),
) -> SBoardResult:
    return await delete(
        url=f"""{os.getenv("BOARD_SERVICE_URL")}/boards""",
        data=data,
        output_type=SBoardResult,
    )


@router.put("/{board_id}")
async def update_board(
        board_id: int,
        data: SBoardPut,
        api_key: str = Depends(check_api_key),
) -> SBoardResult:
    return await put(
        url=f"""{os.getenv("BOARD_SERVICE_URL")}/boards/{board_id}""",
        data=data,
        output_type=SBoardResult,
    )


@router.patch("/{board_id}")
async def update_board(
        board_id: int,
        data: SBoardPatch,
        api_key: str = Depends(check_api_key),
) -> SBoardResult:
    return await patch(
        url=f"""{os.getenv("BOARD_SERVICE_URL")}/boards/{board_id}""",
        data=data,
        output_type=SBoardResult,
    )
