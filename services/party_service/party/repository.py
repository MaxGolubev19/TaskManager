from typing import Optional, List

from services.common.utils.repository import Repository
from services.party_service.database import new_session
from services.party_service.party.models import PartyOrm
from services.common.schemas.party_service.party_schemas import SPartyCreate, SPartyGet, SPartySearch, SPartyPatch, \
    SPartyPut


class PartyRepository:
    @classmethod
    def get_filters(cls, data: SPartySearch) -> List[bool]:
        filters = []

        if data.name:
            filters.append(PartyOrm.name == data.name)

        return filters

    @classmethod
    async def create(cls, data: SPartyCreate) -> int:
        return await Repository.create(
            new_session,
            PartyOrm,
            data,
        )

    @classmethod
    async def get_one(cls, party_id: int) -> Optional[SPartyGet]:
        party = await Repository.get(
            new_session,
            PartyOrm,
            [PartyOrm.id == party_id],
            SPartyGet,
        )
        if len(party):
            return party[0]

    @classmethod
    async def get(cls, data: SPartySearch) -> list[SPartyGet]:
        return await Repository.get(
            new_session,
            PartyOrm,
            PartyRepository.get_filters(data),
            SPartyGet,
        )

    @classmethod
    async def delete_one(cls, party_id: int):
        await Repository.delete(
            new_session,
            PartyOrm,
            [PartyOrm.id == party_id],
        )

    @classmethod
    async def delete(cls, data: SPartySearch):
        await Repository.delete(
            new_session,
            PartyOrm,
            PartyRepository.get_filters(data),
        )

    @classmethod
    async def put(cls, party_id: int, data: SPartyPut):
        await Repository.put(
            new_session,
            PartyOrm,
            [PartyOrm.id == party_id],
            data.dict(),
        )

    @classmethod
    async def patch(cls, party_id: int, data: SPartyPatch):
        values = {}

        if data.name:
            values['name'] = data.name

        await Repository.patch(
            new_session,
            PartyOrm,
            [PartyOrm.id == party_id],
            data.dict(exclude_none=True),
        )
