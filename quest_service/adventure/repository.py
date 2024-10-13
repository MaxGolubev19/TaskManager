from typing import Optional

from sqlalchemy import select, delete, update

from quest_service.database import new_session
from quest_service.adventure.models import AdventureOrm
from quest_service.adventure.schemas import SAdventureCreate, SAdventureGet, SAdventureSearch, SAdventureUpdate


class AdventureRepository:
    @classmethod
    async def create(cls, data: SAdventureCreate) -> int:
        async with new_session() as session:
            adventure = AdventureOrm(**data.model_dump())
            session.add(adventure)
            await session.commit()
            return adventure.id

    @classmethod
    async def get_by_id(cls, adventure_id: int) -> Optional[SAdventureGet]:
        async with new_session() as session:
            result = await session.execute(
                select(AdventureOrm)
                .where(AdventureOrm.id == adventure_id)
            )
            adventure_model = result.scalars().one_or_none()
            if adventure_model:
                return SAdventureGet.model_validate(adventure_model)

    @classmethod
    async def get(cls, data: SAdventureSearch) -> list[SAdventureGet]:
        query = select(AdventureOrm)

        if data.name:
            query = query.where(AdventureOrm.name == data.name)
        if data.party_id:
            query = query.where(AdventureOrm.party_id == data.party_id)

        async with new_session() as session:
            result = await session.execute(query)
            adventure_models = result.scalars().all()
            return [SAdventureGet.model_validate(adventure_model) for adventure_model in adventure_models]

    @classmethod
    async def delete_by_id(cls, adventure_id: int):
        async with new_session() as session:
            await session.execute(
                delete(AdventureOrm)
                .where(AdventureOrm.id == adventure_id)
            )
            await session.commit()

    @classmethod
    async def delete(cls, data: SAdventureSearch):
        query = delete(AdventureOrm)

        if data.name:
            query = query.where(AdventureOrm.name == data.name)
        if data.party_id:
            query = query.where(AdventureOrm.party_id == data.party_id)

        async with new_session() as session:
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, data: SAdventureUpdate):
        query = update(AdventureOrm).where(AdventureOrm.id == data.id)

        if data.name:
            query = query.values(name=data.name)
        if data.party_id:
            query = query.values(party_id=data.party_id)

        async with new_session() as session:
            await session.execute(query)
            await session.commit()
