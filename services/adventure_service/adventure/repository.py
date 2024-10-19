from typing import Optional, List

from services.adventure_service.database import new_session
from services.adventure_service.adventure.models import AdventureOrm
from services.common.utils.repository import Repository
from services.common.schemas.adventure_service.adventure_schemas import SAdventureCreate, SAdventureGet, \
    SAdventureSearch, SAdventurePatch, SAdventurePut


class AdventureRepository:
    @classmethod
    def get_filters(cls, data: SAdventureSearch) -> List[bool]:
        filters = []

        if data.name:
            filters.append(AdventureOrm.name == data.name)
        if data.party_id:
            filters.append(AdventureOrm.party_id == data.party_id)

        return filters

    @classmethod
    async def create(cls, data: SAdventureCreate) -> int:
        return await Repository.create(
            new_session,
            AdventureOrm,
            data,
        )

    @classmethod
    async def get_one(cls, adventure_id: int) -> Optional[SAdventureGet]:
        adventure = await Repository.get(
            new_session,
            AdventureOrm,
            [AdventureOrm.id == adventure_id],
            SAdventureGet,
        )
        if len(adventure):
            return adventure[0]

    @classmethod
    async def get(cls, data: SAdventureSearch) -> list[SAdventureGet]:
        return await Repository.get(
            new_session,
            AdventureOrm,
            AdventureRepository.get_filters(data),
            SAdventureGet,
        )

    @classmethod
    async def delete_one(cls, adventure_id: int):
        await Repository.delete(
            new_session,
            AdventureOrm,
            [AdventureOrm.id == adventure_id],
        )

    @classmethod
    async def delete(cls, data: SAdventureSearch):
        await Repository.delete(
            new_session,
            AdventureOrm,
            AdventureRepository.get_filters(data),
        )

    @classmethod
    async def put(cls, adventure_id: int, data: SAdventurePut):
        await Repository.put(
            new_session,
            AdventureOrm,
            [AdventureOrm.id == adventure_id],
            data.dict(),
        )

    @classmethod
    async def patch(cls, adventure_id: int, data: SAdventurePatch):
        await Repository.patch(
            new_session,
            AdventureOrm,
            [AdventureOrm.id == adventure_id],
            data.dict(exclude_none=True),
        )
