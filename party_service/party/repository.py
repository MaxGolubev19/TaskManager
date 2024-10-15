from typing import Optional

from sqlalchemy import select, delete, update, and_

from party_service.database import new_session
from party_service.party.models import PartyOrm
from party_service.party.schemas import SPartyCreate, SPartyGet, SPartySearch, SPartyUpdate


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
            party = session.get(PartyOrm, party_id)
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
    async def update(cls, data: SPartyUpdate):
        query = update(PartyOrm).where(PartyOrm.id == data.id)

        if data.name:
            query = query.values(name=data.name)

        async with new_session() as session:
            await session.execute(query)
            await session.commit()
