import os
from typing import Annotated

from fastapi import APIRouter, Depends

from services.api_gateway.routers.router import create, get_one, get, delete_one, delete, put, patch
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
    return await create(
        url=f"""{os.getenv("PARTY_SERVICE_URL")}/parties""",
        data=data,
        output_type=SPartyCreateResult,
    )


@router.get("/{party_id}")
async def get_party_by_id(
        party_id: int,
) -> SPartyGet:
    return await get_one(
        url=f"""{os.getenv("PARTY_SERVICE_URL")}/parties/{party_id}""",
        output_type=SPartyGet,
    )


@router.get("")
async def get_parties(
        data: Annotated[SPartySearch, Depends()],
) -> list[SPartyGet]:
    return await get(
        url=f"""{os.getenv("PARTY_SERVICE_URL")}/parties""",
        data=data,
        output_type=SPartyGet,
    )


@router.delete("/{party_id}")
async def delete_party_by_id(
        party_id: int,
) -> SPartyResult:
    return await delete_one(
        url=f"""{os.getenv("PARTY_SERVICE_URL")}/parties/{party_id}""",
        output_type=SPartyResult,
    )


@router.delete("")
async def delete_parties(
        data: Annotated[SPartySearch, Depends()],
) -> SPartyResult:
    return await delete(
        url=f"""{os.getenv("PARTY_SERVICE_URL")}/parties""",
        data=data,
        output_type=SPartyResult,
    )


@router.put("/{party_id}")
async def update_party(
        party_id: int,
        data: SPartyPut,
) -> SPartyResult:
    return await put(
        url=f"""{os.getenv("PARTY_SERVICE_URL")}/parties/{party_id}""",
        data=data,
        output_type=SPartyResult,
    )


@router.patch("/{party_id}")
async def update_party(
        party_id: int,
        data: SPartyPatch,
) -> SPartyResult:
    return await patch(
        url=f"""{os.getenv("PARTY_SERVICE_URL")}/parties/{party_id}""",
        data=data,
        output_type=SPartyResult,
    )
