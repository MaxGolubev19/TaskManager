from typing import Optional

from sqlalchemy import select, delete, update, and_

from services.party_service.database import new_session
from services.party_service.party.models import PartyOrm
from services.common.schemas.party_service.party_schemas import SPartyCreate, SPartyGet, SPartySearch, SPartyPatch, \
    SPartyPut


class PartyRepository:
    @classmethod
    async def create(cls, data: SPartyCreate) -> int:
        async with new_session() as session:
            party = PartyOrm(**data.model_dump())
            session.add(party)
            await session.commit()
            return party.id

    @classmethod
    async def get_one(cls, party_id: int) -> Optional[SPartyGet]:
        async with new_session() as session:
            party = await session.get(PartyOrm, party_id)
            if party:
                return SPartyGet.model_validate(party, from_attributes=True)

    @classmethod
    async def get(cls, data: SPartySearch) -> list[SPartyGet]:
        filters = []

        if data.name:
            filters.append(PartyOrm.name == data.name)

        async with new_session() as session:
            result = await session.execute(
                select(PartyOrm)
                .filter(and_(*filters))
            )
            party_models = result.scalars().all()
            return [SPartyGet.model_validate(party_model, from_attributes=True) for party_model in party_models]

    @classmethod
    async def delete_one(cls, party_id: int):
        async with new_session() as session:
            await session.execute(
                delete(PartyOrm)
                .where(PartyOrm.id == party_id)
            )
            await session.commit()

    @classmethod
    async def delete(cls, data: SPartySearch):
        filters = []

        if data.name:
            filters.append(PartyOrm.name == data.name)

        async with new_session() as session:
            await session.execute(
                delete(PartyOrm)
                .filter(and_(*filters))
            )
            await session.commit()

    @classmethod
    async def put(cls, party_id: int, data: SPartyPut):
        async with new_session() as session:
            await session.execute(
                update(PartyOrm)
                .where(PartyOrm.id == party_id)
                .values(
                    name=data.name,
                )
            )
            await session.commit()

    @classmethod
    async def patch(cls, party_id: int, data: SPartyPatch):
        values = {}

        if data.name:
            values['name'] = data.name

        async with new_session() as session:
            await session.execute(
                update(PartyOrm)
                .where(PartyOrm.id == party_id)
                .values(**values)
            )
            await session.commit()
