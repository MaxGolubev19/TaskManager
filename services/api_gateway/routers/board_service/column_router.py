import os
from typing import Annotated

import httpx
from fastapi import APIRouter, Depends, HTTPException

from services.common.schemas.board_service.column_schemas import SColumnCreate, SColumnCreateResult, SColumnGet, \
    SColumnSearch, SColumnResult, SColumnPut, SColumnPatch

router = APIRouter(
    prefix="/columns",
    tags=["Columns"],
)


@router.post("")
async def create_column(
        data: Annotated[SColumnCreate, Depends()],
) -> SColumnCreateResult:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=f"""{os.getenv("BOARD_SERVICE_URL")}/columns""",
            json=data.dict(),
        )
    if response.status_code == 201:
        return SColumnCreateResult.model_validate(response.json())
    raise HTTPException(status_code=500)


@router.get("/{column_id}")
async def get_column(
        column_id: int,
) -> SColumnGet:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=f"""{os.getenv("BOARD_SERVICE_URL")}/columns/{column_id}""",
        )
    if response.status_code == 404:
        raise HTTPException(status_code=404)
    return SColumnGet.model_validate(response.json(), from_attributes=True)


@router.get("")
async def get_columns(
        data: Annotated[SColumnSearch, Depends()],
) -> list[SColumnGet]:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=f"""{os.getenv("BOARD_SERVICE_URL")}/columns""",
            params=data.dict(exclude_none=True),
        )
    return [SColumnGet.model_validate(column, from_attributes=True) for column in response.json()]


@router.delete("/{column_id}")
async def delete_column(
        column_id: int,
) -> SColumnResult:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            url=f"""{os.getenv("BOARD_SERVICE_URL")}/columns/{column_id}""",
        )
    return SColumnResult.model_validate(response.json())


@router.delete("")
async def delete_columns(
        data: Annotated[SColumnSearch, Depends()],
) -> SColumnResult:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            url=f"""{os.getenv("BOARD_SERVICE_URL")}/columns""",
            params=data.dict(exclude_none=True),
        )
    return SColumnResult.model_validate(response.json())


@router.put("/{column_id}")
async def update_column(
        column_id: int,
        data: Annotated[SColumnPut, Depends()],
) -> SColumnResult:
    async with httpx.AsyncClient() as client:
        response = await client.put(
            url=f"""{os.getenv("BOARD_SERVICE_URL")}/columns/{column_id}""",
            json=data.dict(),
        )
    return SColumnResult.model_validate(response.json())


@router.patch("/{column_id}")
async def update_column(
        column_id: int,
        data: Annotated[SColumnPatch, Depends()],
) -> SColumnResult:
    async with httpx.AsyncClient() as client:
        response = await client.patch(
            url=f"""{os.getenv("BOARD_SERVICE_URL")}/columns/{column_id}""",
            json=data.dict(),
        )
    return SColumnResult.model_validate(response.json())
