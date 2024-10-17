import os
from typing import Annotated

import httpx
from fastapi import APIRouter, Depends, HTTPException

from services.common.schemas.party_service.party_schemas import SPartyCreate, SPartyCreateResult, SPartyGet, \
    SPartyResult, SPartyPatch, SPartySearch, SPartyPut

router = APIRouter(
    prefix="/parties",
    tags=["Parties"],
)


@router.post("")
async def create_party(
        data: SPartyCreate,
) -> SPartyCreateResult:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=f"""{os.getenv("PARTY_SERVICE_URL")}/parties""",
            json=data.json(),
        )
    return SPartyCreateResult.model_validate(response.json())


@router.get("/{party_id}")
async def get_party_by_id(
        party_id: int,
) -> SPartyGet:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=f"""{os.getenv("PARTY_SERVICE_URL")}/parties/{party_id}""",
        )
    if response.status_code == 404:
        raise HTTPException(status_code=404)
    return SPartyGet.model_validate(response.json(), from_attributes=True)


@router.get("")
async def get_parties(
        data: Annotated[SPartySearch, Depends()],
) -> list[SPartyGet]:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=f"""{os.getenv("PARTY_SERVICE_URL")}/parties""",
            params=data.dict(exclude_none=True),
        )
    return [SPartyGet.model_validate(party, from_attributes=True) for party in response.json()]


@router.delete("/{party_id}")
async def delete_party_by_id(
        party_id: int,
) -> SPartyResult:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            url=f"""{os.getenv("PARTY_SERVICE_URL")}/parties/{party_id}""",
        )
    return SPartyResult.model_validate(response.json())


@router.delete("")
async def delete_parties(
        data: Annotated[SPartySearch, Depends()],
) -> SPartyResult:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            url=f"""{os.getenv("PARTY_SERVICE_URL")}/parties""",
            params=data.dict(exclude_none=True),
        )
    return SPartyResult.model_validate(response.json())


@router.put("/{party_id}")
async def update_party(
        party_id: int,
        data: SPartyPut,
) -> SPartyResult:
    async with httpx.AsyncClient() as client:
        response = await client.put(
            url=f"""{os.getenv("PARTY_SERVICE_URL")}/parties/{party_id}""",
            json=data.json(),
        )
    return SPartyResult.model_validate(response.json())


@router.patch("/{party_id}")
async def update_party(
        party_id: int,
        data: SPartyPatch,
) -> SPartyResult:
    async with httpx.AsyncClient() as client:
        response = await client.patch(
            url=f"""{os.getenv("PARTY_SERVICE_URL")}/parties/{party_id}""",
            json=data.json(),
        )
    return SPartyResult.model_validate(response.json())
