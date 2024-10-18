from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends

from services.common.utils import check_api_key
from services.party_service.party.repository import PartyRepository
from services.common.schemas.party_service.party_schemas import SPartyCreate, SPartyResult, SPartyGet, SPartySearch, \
    SPartyPatch, SPartyCreateResult, SPartyPut

router = APIRouter(
    prefix="/parties",
    tags=["Parties"],
)


@router.post("", status_code=201)
async def create_party(
        data: SPartyCreate,
        api_key=Depends(check_api_key),
) -> SPartyCreateResult:
    party_id = await PartyRepository.create(data)
    return SPartyCreateResult(
        ok=True,
        id=party_id,
    )


@router.get("/{party_id}", status_code=200)
async def get_party_by_id(
        party_id: int,
        api_key=Depends(check_api_key),
) -> SPartyGet:
    party = await PartyRepository.get_one(party_id)
    if party is None:
        raise HTTPException(status_code=404)
    return party


@router.get("", status_code=200)
async def get_parties(
        data: Annotated[SPartySearch, Depends()],
        api_key=Depends(check_api_key),
) -> list[SPartyGet]:
    parties = await PartyRepository.get(data)
    return parties


@router.delete("/{party_id}", status_code=200)
async def delete_party_by_id(
        party_id: int,
        api_key=Depends(check_api_key),
) -> SPartyResult:
    await PartyRepository.delete_one(party_id)
    return SPartyResult(
        ok=True,
    )


@router.delete("", status_code=200)
async def delete_parties(
        data: Annotated[SPartySearch, Depends()],
        api_key=Depends(check_api_key),
) -> SPartyResult:
    await PartyRepository.delete(data)
    return SPartyResult(
        ok=True,
    )


@router.put("/{party_id}", status_code=200)
async def update_party(
        party_id: int,
        data: SPartyPut,
        api_key=Depends(check_api_key),
) -> SPartyResult:
    await PartyRepository.put(party_id, data)
    return SPartyResult(
        ok=True,
    )


@router.patch("/{party_id}", status_code=200)
async def update_party(
        party_id: int,
        data: SPartyPatch,
        api_key=Depends(check_api_key),
) -> SPartyResult:
    await PartyRepository.patch(party_id, data)
    return SPartyResult(
        ok=True,
    )
