from typing import Optional

from sqlalchemy import select, delete, update, and_

from adventure_service.database import new_session
from adventure_service.adventure.models import AdventureOrm
from adventure_service.adventure.schemas import SAdventureCreate, SAdventureGet, SAdventureSearch, SAdventureUpdate


class AdventureRepository:
    @classmethod
    async def create(cls, data: SAdventureCreate) -> int:
        async with new_session() as session:
            adventure = AdventureOrm(**data.model_dump())
            session.add(adventure)
            await session.commit()
            return adventure.id

    @classmethod
    async def get_one(cls, adventure_id: int) -> Optional[SAdventureGet]:
        async with new_session() as session:
            adventure = session.get(AdventureOrm, adventure_id)
            if adventure:
                return SAdventureGet.model_validate(adventure, from_attributes=True)

    @classmethod
    async def get(cls, data: SAdventureSearch) -> list[SAdventureGet]:
        filters = []

        if data.name:
            filters.append(AdventureOrm.name == data.name)
        if data.party_id:
            filters.append(AdventureOrm.party_id == data.party_id)

        async with new_session() as session:
            result = await session.execute(
                select(AdventureOrm)
                .filter(and_(*filters))
            )
            adventure_models = result.scalars().all()
            return [SAdventureGet.model_validate(adventure_model, from_attributes=True) for adventure_model in adventure_models]

    @classmethod
    async def delete_one(cls, adventure_id: int):
        async with new_session() as session:
            await session.execute(
                delete(AdventureOrm)
                .where(AdventureOrm.id == adventure_id)
            )
            await session.commit()

    @classmethod
    async def delete(cls, data: SAdventureSearch):
        filters = []

        if data.name:
            filters.append(AdventureOrm.name == data.name)
        if data.party_id:
            filters.append(AdventureOrm.party_id == data.party_id)

        async with new_session() as session:
            await session.execute(
                delete(AdventureOrm)
                .filter(and_(*filters))
            )
            await session.commit()

    @classmethod
    async def put(cls, adventure_id: int, data: SAdventureUpdate):
        async with new_session() as session:
            await session.execute(
                update(AdventureOrm)
                .where(AdventureOrm.id == adventure_id)
                .values(
                    name=data.name,
                    party_id=data.party_id
                )
            )
            await session.commit()

    @classmethod
    async def patch(cls, adventure_id: int, data: SAdventureUpdate):
        values = {}

        if data.name:
            values['name'] = data.name
        if data.party_id:
            values['party_id'] = data.party_id

        async with new_session() as session:
            await session.execute(
                update(AdventureOrm)
                .where(AdventureOrm.id == adventure_id)
                .values(**values)
            )
            await session.commit()
