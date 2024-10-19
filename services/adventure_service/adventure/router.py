from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from services.adventure_service.adventure.repository import AdventureRepository
from services.common.schemas.adventure_service.adventure_schemas import SAdventureCreate, SAdventureResult, \
    SAdventureGet, SAdventureSearch, SAdventurePatch, SAdventureCreateResult, SAdventurePut

router = APIRouter(
    prefix="/adventures",
    tags=["Adventures"],
)


@router.post("", status_code=201)
async def create_adventure(
        data: SAdventureCreate,
) -> SAdventureCreateResult:
    adventure_id = await AdventureRepository.create(data)
    return SAdventureCreateResult(
        ok=True,
        id=adventure_id,
    )


@router.get("/{adventure_id}", status_code=200)
async def get_adventure(
        adventure_id: int,
) -> SAdventureGet:
    adventure = await AdventureRepository.get_one(adventure_id)
    if adventure is None:
        raise HTTPException(status_code=404)
    return adventure


@router.get("", status_code=200)
async def get_adventures(
        data: Annotated[SAdventureSearch, Depends()],
) -> list[SAdventureGet]:
    adventures = await AdventureRepository.get(data)
    return adventures


@router.delete("/{adventure_id}", status_code=200)
async def delete_adventure(
        adventure_id: int,
) -> SAdventureResult:
    await AdventureRepository.delete_one(adventure_id)
    return SAdventureResult(
        ok=True,
    )


@router.delete("", status_code=200)
async def delete_adventures(
        data: Annotated[SAdventureSearch, Depends()],
) -> SAdventureResult:
    await AdventureRepository.delete(data)
    return SAdventureResult(
        ok=True,
    )


@router.put("/{adventure_id}", status_code=200)
async def update_adventure(
        adventure_id: int,
        data: SAdventurePut,
) -> SAdventureResult:
    await AdventureRepository.put(adventure_id, data)
    return SAdventureResult(
        ok=True,
    )


@router.patch("/{adventure_id}", status_code=200)
async def update_adventure(
        adventure_id: int,
        data: SAdventurePatch,
) -> SAdventureResult:
    await AdventureRepository.patch(adventure_id, data)
    return SAdventureResult(
        ok=True,
    )
