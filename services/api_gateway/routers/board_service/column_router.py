import os
from typing import Annotated

from fastapi import APIRouter, Depends

from services.api_gateway.routers.router import create, get_one, get, delete_one, delete, put, patch
from services.common.schemas.board_service.column_schemas import SColumnCreate, SColumnCreateResult, SColumnGet, \
    SColumnResult, SColumnSearch, SColumnPut, SColumnPatch
from services.common.utils.api import check_api_key

router = APIRouter(
    prefix="/columns",
    tags=["Columns"],
)


@router.post("")
async def create_column(
        data: SColumnCreate,
        api_key: str = Depends(check_api_key),
) -> SColumnCreateResult:
    return await create(
        url=f"""{os.getenv("BOARD_SERVICE_URL")}/columns""",
        data=data,
        output_type=SColumnCreateResult,
    )


@router.get("/{column_id}")
async def get_column(
        column_id: int,
        api_key: str = Depends(check_api_key),
) -> SColumnGet:
    return await get_one(
        url=f"""{os.getenv("BOARD_SERVICE_URL")}/columns/{column_id}""",
        output_type=SColumnGet,
    )


@router.get("")
async def get_columns(
        data: Annotated[SColumnSearch, Depends()],
        api_key: str = Depends(check_api_key),
) -> list[SColumnGet]:
    return await get(
        url=f"""{os.getenv("BOARD_SERVICE_URL")}/columns""",
        data=data,
        output_type=SColumnGet,
    )


@router.delete("/{column_id}")
async def delete_column(
        column_id: int,
        api_key: str = Depends(check_api_key),
) -> SColumnResult:
    return await delete_one(
        url=f"""{os.getenv("BOARD_SERVICE_URL")}/columns/{column_id}""",
        output_type=SColumnResult,
    )


@router.delete("")
async def delete_columns(
        data: Annotated[SColumnSearch, Depends()],
        api_key: str = Depends(check_api_key),
) -> SColumnResult:
    return await delete(
        url=f"""{os.getenv("BOARD_SERVICE_URL")}/columns""",
        data=data,
        output_type=SColumnResult,
    )


@router.put("/{column_id}")
async def update_column(
        column_id: int,
        data: SColumnPut,
        api_key: str = Depends(check_api_key),
) -> SColumnResult:
    return await put(
        url=f"""{os.getenv("BOARD_SERVICE_URL")}/columns/{column_id}""",
        data=data,
        output_type=SColumnResult,
    )


@router.patch("/{column_id}")
async def update_column(
        column_id: int,
        data: SColumnPatch,
        api_key: str = Depends(check_api_key),
) -> SColumnResult:
    return await patch(
        url=f"""{os.getenv("BOARD_SERVICE_URL")}/columns/{column_id}""",
        data=data,
        output_type=SColumnResult,
    )
