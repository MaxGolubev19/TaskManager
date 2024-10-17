from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends

from services.party_service.party.repository import PartyRepository
from services.common.schemas.party_service.party_schemas import SPartyCreate, SPartyResult, SPartyGet, SPartySearch, \
    SPartyPatch, SPartyCreateResult, SPartyPut

router = APIRouter(
    prefix="/parties",
    tags=["Parties"],
)


@router.post("")
async def create_party(
        data: SPartyCreate,
) -> SPartyCreateResult:
    party_id = await PartyRepository.create(data)
    return SPartyCreateResult(
        ok=True,
        id=party_id,
    )


@router.get("/{party_id}")
async def get_party_by_id(
        party_id: int,
) -> SPartyGet:
    party = await PartyRepository.get_one(party_id)
    if party is None:
        raise HTTPException(status_code=404)
    return party


@router.get("")
async def get_parties(
        data: Annotated[SPartySearch, Depends()],
) -> list[SPartyGet]:
    parties = await PartyRepository.get(data)
    return parties


@router.delete("/{party_id}")
async def delete_party_by_id(
        party_id: int,
) -> SPartyResult:
    await PartyRepository.delete_one(party_id)
    return SPartyResult(
        ok=True,
    )


@router.delete("")
async def delete_parties(
        data: Annotated[SPartySearch, Depends()],
) -> SPartyResult:
    await PartyRepository.delete(data)
    return SPartyResult(
        ok=True,
    )


@router.put("/{party_id}")
async def update_party(
        party_id: int,
        data: SPartyPut,
) -> SPartyResult:
    await PartyRepository.put(party_id, data)
    return SPartyResult(
        ok=True,
    )


@router.patch("/{party_id}")
async def update_party(
        party_id: int,
        data: SPartyPatch,
) -> SPartyResult:
    await PartyRepository.patch(party_id, data)
    return SPartyResult(
        ok=True,
    )
