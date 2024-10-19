from typing import Optional

from services.common.utils.repository import Repository
from services.quest_service.database import new_session
from services.quest_service.quest.models import QuestOrm
from services.common.schemas.quest_service.quest_schemas import SQuestCreate, SQuestGet, SQuestSearch, SQuestPatch, \
    SQuestPut


class QuestRepository:
    @classmethod
    def get_filters(cls, data: SQuestSearch) -> list:
        filters = []

        if data.name:
            filters.append(QuestOrm.name == data.name)
        if data.description:
            filters.append(QuestOrm.description == data.description)
        if data.category_id:
            filters.append(QuestOrm.category_id == data.category_id)
        if data.column_id:
            filters.append(QuestOrm.column_id == data.column_id)
        if data.board_id:
            filters.append(QuestOrm.board_id == data.board_id)
        if data.adventure_id:
            filters.append(QuestOrm.adventure_id == data.adventure_id)
        if data.party_id:
            filters.append(QuestOrm.party_id == data.party_id)
        if data.user_id:
            filters.append(QuestOrm.user_id == data.user_id)
        if data.deadline:
            filters.append(QuestOrm.deadline == data.deadline)

        return filters

    @classmethod
    async def create(cls, data: SQuestCreate) -> int:
        return await Repository.create(
            new_session,
            QuestOrm,
            data,
        )

    @classmethod
    async def get_one(cls, quest_id: int) -> Optional[SQuestGet]:
        quest = await Repository.get(
            new_session,
            QuestOrm,
            [QuestOrm.id == quest_id],
            SQuestGet,
        )
        if len(quest):
            return quest[0]

    @classmethod
    async def get(cls, data: SQuestSearch) -> list[SQuestGet]:
        return await Repository.get(
            new_session,
            QuestOrm,
            QuestRepository.get_filters(data),
            SQuestGet,
        )

    @classmethod
    async def delete_one(cls, quest_id: int):
        await Repository.delete(
            new_session,
            QuestOrm,
            [QuestOrm.id == quest_id],
        )

    @classmethod
    async def delete(cls, data: SQuestSearch):
        await Repository.delete(
            new_session,
            QuestOrm,
            QuestRepository.get_filters(data),
        )

    @classmethod
    async def put(cls, quest_id: int, data: SQuestPut):
        await Repository.put(
            new_session,
            QuestOrm,
            [QuestOrm.id == quest_id],
            data.dict(),
        )

    @classmethod
    async def patch(cls, quest_id: int, data: SQuestPatch):
        await Repository.patch(
            new_session,
            QuestOrm,
            [QuestOrm.id == quest_id],
            data.dict(exclude_none=True)
        )
