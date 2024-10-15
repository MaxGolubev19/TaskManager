from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from services.adventure_service.adventure.repository import AdventureRepository
from services.adventure_service.adventure.schemas import SAdventureCreate, SAdventureResult, SAdventureGet, SAdventureSearch, SAdventureUpdate, \
    SAdventureCreateResult

router = APIRouter(
    prefix='/adventures',
    tags=["Adventures"],
)


@router.post("")
async def create_adventure(
        data: Annotated[SAdventureCreate, Depends()],
) -> SAdventureCreateResult:
    adventure_id = await AdventureRepository.create(data)
    return SAdventureCreateResult(
        ok=True,
        id=adventure_id,
    )


@router.get("/{adventure_id}")
async def get_adventure(
        adventure_id: int,
) -> SAdventureGet:
    adventure = await AdventureRepository.get_one(adventure_id)
    if adventure is None:
        raise HTTPException(status_code=404)
    return adventure


@router.get("")
async def get_adventures(
        data: Annotated[SAdventureSearch, Depends()],
) -> list[SAdventureGet]:
    adventures = await AdventureRepository.get(data)
    return adventures


@router.delete("/{adventure_id}")
async def delete_adventure(
        adventure_id: int,
) -> SAdventureResult:
    await AdventureRepository.delete_one(adventure_id)
    return SAdventureResult(
        ok=True,
    )


@router.delete("")
async def delete_adventures(
        data: Annotated[SAdventureSearch, Depends()],
) -> SAdventureResult:
    await AdventureRepository.delete(data)
    return SAdventureResult(
        ok=True,
    )


@router.put("/{adventure_id}")
async def update_adventure(
        adventure_id: int,
        data: Annotated[SAdventureUpdate, Depends()],
) -> SAdventureResult:
    await AdventureRepository.put(adventure_id, data)
    return SAdventureResult(
        ok=True,
    )


@router.patch("/{adventure_id}")
async def update_adventure(
        adventure_id: int,
        data: Annotated[SAdventureUpdate, Depends()],
) -> SAdventureResult:
    await AdventureRepository.patch(adventure_id, data)
    return SAdventureResult(
        ok=True,
    )
