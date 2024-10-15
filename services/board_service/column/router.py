from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from services.board_service.column.repository import ColumnRepository
from services.board_service.column.schemas import SColumnCreate, SColumnResult, SColumnGet, SColumnSearch, SColumnUpdate, SColumnCreateResult

router = APIRouter(
    prefix='/columns',
    tags=["Columns"],
)


@router.post("")
async def create_column(
        data: Annotated[SColumnCreate, Depends()],
) -> SColumnCreateResult:
    column_id = await ColumnRepository.create(data)
    return SColumnCreateResult(
        ok=True,
        id=column_id,
    )


@router.get("/{column_id}")
async def get_column_by_id(
        column_id: int,
) -> SColumnGet:
    column = await ColumnRepository.get_one(column_id)
    if column is None:
        raise HTTPException(status_code=404)
    return column


@router.get("")
async def get_columns(
        data: Annotated[SColumnSearch, Depends()],
) -> list[SColumnGet]:
    columns = await ColumnRepository.get(data)
    return columns


@router.delete("/{column_id}")
async def delete_column_by_id(
        column_id: int,
) -> SColumnResult:
    await ColumnRepository.delete_one(column_id)
    return SColumnResult(
        ok=True,
    )


@router.delete("")
async def delete_columns(
        data: Annotated[SColumnSearch, Depends()],
) -> SColumnResult:
    await ColumnRepository.delete(data)
    return SColumnResult(
        ok=True,
    )


@router.put("/{column_id}")
async def update_column(
        column_id: int,
        data: Annotated[SColumnUpdate, Depends()],
) -> SColumnResult:
    await ColumnRepository.put(column_id, data)
    return SColumnResult(
        ok=True,
    )


@router.patch("/{column_id}")
async def update_column(
        column_id: int,
        data: Annotated[SColumnUpdate, Depends()],
) -> SColumnResult:
    await ColumnRepository.patch(column_id, data)
    return SColumnResult(
        ok=True,
    )
