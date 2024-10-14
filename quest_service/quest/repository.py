from typing import Optional

from sqlalchemy import select, delete, update

from quest_service.database import new_session
from quest_service.quest.models import QuestOrm
from quest_service.quest.schemas import SQuestCreate, SQuestGet, SQuestSearch, SQuestUpdate


class QuestRepository:
    @classmethod
    async def create_quest(cls, data: SQuestCreate) -> int:
        async with new_session() as session:
            quest = QuestOrm(**data.model_dump())
            session.add(quest)
            await session.commit()
            return quest.id

    @classmethod
    async def get_quest_by_id(cls, quest_id: int) -> Optional[SQuestGet]:
        async with new_session() as session:
            result = await session.execute(
                select(QuestOrm)
                .where(QuestOrm.id == quest_id)
            )

            quest_model = result.scalars().one_or_none()
            if quest_model:
                return SQuestGet.model_validate(quest_model)

    @classmethod
    async def get_quests(cls, data: SQuestSearch) -> list[SQuestGet]:
        query = select(QuestOrm)

        if data.name:
            query = query.where(QuestOrm.name == data.name)
        if data.category_id:
            query = query.where(QuestOrm.category_id == data.category_id)
        if data.column_id:
            query = query.where(QuestOrm.column_id == data.column_id)
        if data.board_id:
            query = query.where(QuestOrm.board_id == data.board_id)
        if data.adventure_id:
            query = query.where(QuestOrm.adventure_id == data.adventure_id)
        if data.party_id:
            query = query.where(QuestOrm.party_id == data.party_id)
        if data.user_id:
            query = query.where(QuestOrm.user_id == data.user_id)
        if data.deadline:
            query = query.where(QuestOrm.deadline == data.deadline)

        async with new_session() as session:
            result = await session.execute(query)
            quest_models = result.scalars().all()
            return [SQuestGet.model_validate(quest_model) for quest_model in quest_models]

    @classmethod
    async def delete_quest_by_id(cls, quest_id: int):
        async with new_session() as session:
            await session.execute(
                delete(QuestOrm)
                .filter_by(id=quest_id)
            )
            await session.commit()

    @classmethod
    async def delete_quests(cls, data: SQuestSearch):
        query = delete(QuestOrm)

        if data.name:
            query = query.where(QuestOrm.name == data.name)
        if data.category_id:
            query = query.where(QuestOrm.category_id == data.category_id)
        if data.column_id:
            query = query.where(QuestOrm.column_id == data.column_id)
        if data.board_id:
            query = query.where(QuestOrm.board_id == data.board_id)
        if data.adventure_id:
            query = query.where(QuestOrm.adventure_id == data.adventure_id)
        if data.party_id:
            query = query.where(QuestOrm.party_id == data.party_id)
        if data.user_id:
            query = query.where(QuestOrm.user_id == data.user_id)
        if data.deadline:
            query = query.where(QuestOrm.deadline == data.deadline)

        async with new_session() as session:
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update_quest(cls, data: SQuestUpdate):
        query = update(QuestOrm).where(QuestOrm.id == data.id)

        if data.name:
            query = query.values(name=data.name)
        if data.category_id:
            query = query.values(category_id=data.category_id)
        if data.column_id:
            query = query.values(column_id=data.column_id)
        if data.board_id:
            query = query.values(board_id=data.board_id)
        if data.adventure_id:
            query = query.values(adventure_id=data.adventure_id)
        if data.party_id:
            query = query.values(party_id=data.party_id)
        if data.user_id:
            query = query.values(user_id=data.user_id)
        if data.deadline:
            query = query.values(deadline=data.deadline)

        async with new_session() as session:
            await session.execute(query)
            await session.commit()
