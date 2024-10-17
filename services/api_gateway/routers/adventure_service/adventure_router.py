import os
from typing import Annotated

import httpx
from fastapi import APIRouter, Depends, HTTPException

from services.common.schemas.adventure_service.adventure_schemas import SAdventureCreate, SAdventureCreateResult, \
    SAdventureGet, SAdventureSearch, SAdventureResult, SAdventurePut, SAdventurePatch
from services.common.utils import check_api_key

router = APIRouter(
    prefix="/adventures",
    tags=["Adventures"],
)


@router.post("")
async def create_adventure(
        data: SAdventureCreate,
        api_key: str = Depends(check_api_key),
) -> SAdventureCreateResult:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=f"""{os.getenv("ADVENTURE_SERVICE_URL")}/adventures""",
            json=data.dict(),
        )
    if response.status_code == 201:
        return SAdventureCreateResult.model_validate(response.json())
    raise HTTPException(status_code=500)


@router.get("/{adventure_id}")
async def get_adventure(
        adventure_id: int,
) -> SAdventureGet:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=f"""{os.getenv("ADVENTURE_SERVICE_URL")}/adventures/{adventure_id}""",
        )
    if response.status_code == 404:
        raise HTTPException(status_code=404)
    return SAdventureGet.model_validate(response.json(), from_attributes=True)


@router.get("")
async def get_adventures(
        data: Annotated[SAdventureSearch, Depends()],
) -> list[SAdventureGet]:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=f"""{os.getenv("ADVENTURE_SERVICE_URL")}/adventures""",
            params=data.dict(exclude_none=True),
        )
    return [SAdventureGet.model_validate(adventure, from_attributes=True) for adventure in response.json()]


@router.delete("/{adventure_id}")
async def delete_adventure(
        adventure_id: int,
) -> SAdventureResult:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            url=f"""{os.getenv("ADVENTURE_SERVICE_URL")}/adventures/{adventure_id}""",
        )
    return SAdventureResult.model_validate(response.json())


@router.delete("")
async def delete_adventures(
        data: Annotated[SAdventureSearch, Depends()],
) -> SAdventureResult:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            url=f"""{os.getenv("ADVENTURE_SERVICE_URL")}/adventures""",
            params=data.dict(exclude_none=True),
        )
    return SAdventureResult.model_validate(response.json())


@router.put("/{adventure_id}")
async def update_adventure(
        adventure_id: int,
        data: SAdventurePut,
) -> SAdventureResult:
    async with httpx.AsyncClient() as client:
        response = await client.put(
            url=f"""{os.getenv("ADVENTURE_SERVICE_URL")}/adventures/{adventure_id}""",
            json=data.dict(),
        )
    return SAdventureResult.model_validate(response.json())


@router.patch("/{adventure_id}")
async def update_adventure(
        adventure_id: int,
        data: SAdventurePatch,
) -> SAdventureResult:
    async with httpx.AsyncClient() as client:
        response = await client.patch(
            url=f"""{os.getenv("ADVENTURE_SERVICE_URL")}/adventures/{adventure_id}""",
            json=data.dict(),
        )
    return SAdventureResult.model_validate(response.json())
