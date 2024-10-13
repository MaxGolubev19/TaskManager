from typing import Optional

from sqlalchemy import select, delete, update

from quest_service.database import new_session
from quest_service.party.models import PartyOrm
from quest_service.party.schemas import SPartyCreate, SPartyGet, SPartySearch, SPartyUpdate


class PartyRepository:
    @classmethod
    async def create(cls, data: SPartyCreate) -> int:
        async with new_session() as session:
            party = PartyOrm(**data.model_dump())
            session.add(party)
            await session.commit()
            return party.id

    @classmethod
    async def get_by_id(cls, party_id: int) -> Optional[SPartyGet]:
        async with new_session() as session:
            result = await session.execute(
                select(PartyOrm)
                .where(PartyOrm.id == party_id)
            )
            party_model = result.scalars().one_or_none()
            if party_model:
                return SPartyGet.model_validate(party_model)

    @classmethod
    async def get(cls, data: SPartySearch) -> list[SPartyGet]:
        query = select(PartyOrm)

        if data.name:
            query = query.where(PartyOrm.name == data.name)

        async with new_session() as session:
            result = await session.execute(query)
            party_models = result.scalars().all()
            return [SPartyGet.model_validate(party_model) for party_model in party_models]

    @classmethod
    async def delete_by_id(cls, party_id: int):
        async with new_session() as session:
            await session.execute(
                delete(PartyOrm)
                .where(PartyOrm.id == party_id)
            )
            await session.commit()

    @classmethod
    async def delete(cls, data: SPartySearch):
        query = delete(PartyOrm)

        if data.name:
            query = query.where(PartyOrm.name == data.name)

        async with new_session() as session:
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, data: SPartyUpdate):
        query = update(PartyOrm).where(PartyOrm.id == data.id)

        if data.name:
            query = query.values(name=data.name)

        async with new_session() as session:
            await session.execute(query)
            await session.commit()
