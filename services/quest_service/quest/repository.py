from typing import Optional

from sqlalchemy import select, delete, update, and_

from services.quest_service.database import new_session
from services.quest_service.quest.models import QuestOrm
from services.common.schemas.quest_service.quest_schemas import SQuestCreate, SQuestGet, SQuestSearch, SQuestPatch, \
    SQuestPut


class QuestRepository:
    @classmethod
    async def create(cls, data: SQuestCreate) -> int:
        async with new_session() as session:
            quest = QuestOrm(**data.model_dump())
            session.add(quest)
            await session.commit()
            return quest.id

    @classmethod
    async def get_one(cls, quest_id: int) -> Optional[SQuestGet]:
        async with new_session() as session:
            quest = await session.get(QuestOrm, quest_id)
            if quest:
                return SQuestGet.model_validate(quest, from_attributes=True)

    @classmethod
    async def get(cls, data: SQuestSearch) -> list[SQuestGet]:
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

        async with new_session() as session:
            result = await session.execute(
                select(QuestOrm)
                .filter(and_(*filters))
            )
            quest_models = result.scalars().all()
            return [SQuestGet.model_validate(quest_model, from_attributes=True) for quest_model in quest_models]

    @classmethod
    async def delete_one(cls, quest_id: int):
        async with new_session() as session:
            await session.execute(
                delete(QuestOrm)
                .filter_by(id=quest_id)
            )
            await session.commit()

    @classmethod
    async def delete(cls, data: SQuestSearch):
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

        async with new_session() as session:
            await session.execute(
                delete(QuestOrm)
                .filter(and_(*filters))
            )
            await session.commit()

    @classmethod
    async def put(cls, quest_id: int, data: SQuestPut):
        async with new_session() as session:
            await session.execute(
                update(QuestOrm)
                .where(QuestOrm.id == quest_id)
                .values(
                    name=data.name,
                    description=data.description,
                    category_id=data.category_id,
                    column_id=data.column_id,
                    board_id=data.board_id,
                    adventure_id=data.adventure_id,
                    party_id=data.party_id,
                    user_id=data.user_id,
                    deadline=data.deadline,
                )
            )
            await session.commit()

    @classmethod
    async def patch(cls, quest_id: int, data: SQuestPatch):
        values = {}

        if data.name:
            values['name'] = data.name
        if data.description:
            values['description'] = data.description
        if data.category_id:
            values['category_id'] = data.category_id
        if data.column_id:
            values['column_id'] = data.column_id
        if data.board_id:
            values['board_id'] = data.board_id
        if data.adventure_id:
            values['adventure_id'] = data.adventure_id
        if data.party_id:
            values['party_id'] = data.party_id
        if data.user_id:
            values['user_id'] = data.user_id
        if data.deadline:
            values['deadline'] = data.deadline

        async with new_session() as session:
            await session.execute(
                update(QuestOrm)
                .where(QuestOrm.id == quest_id)
                .values(**values)
            )
            await session.commit()
