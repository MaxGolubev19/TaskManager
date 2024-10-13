from typing import Optional

from sqlalchemy import select, delete, update

from quest_service.database import new_session
from quest_service.quest.models import QuestOrm, DependencyOrm
from quest_service.quest.schemas import SQuestCreate, SQuestGet, SQuestSearch, SQuestUpdate, SDependencyCreate, SDependencyGet, \
    SDependencySearch


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

    @classmethod
    async def create_dependency(cls, data: SDependencyCreate) -> int:
        async with new_session() as session:
            dependency = DependencyOrm(**data.model_dump())
            session.add(dependency)
            await session.commit()
            return dependency.id

    @classmethod
    async def get_dependency_by_id(cls, dependency_id: int) -> Optional[SDependencyGet]:
        async with new_session() as session:
            result = await session.execute(
                select(DependencyOrm)
                .where(DependencyOrm.id == dependency_id)
            )

            dependency_model = result.scalars().one_or_none()
            if dependency_model:
                return SDependencyGet.model_validate(dependency_model)

    @classmethod
    async def get_dependencies(cls, data: SDependencySearch) -> list[SDependencyGet]:
        query = select(DependencyOrm)

        if data.parent_id:
            query = query.where(DependencyOrm.parent_id == data.parent_id)
        if data.child_id:
            query = query.where(DependencyOrm.child_id == data.child_id)

        async with new_session() as session:
            result = await session.execute(query)
            dependency_models = result.scalars().all()
            for dependency_model in dependency_models:
                print(dependency_model)
            return [SDependencyGet.model_validate(dependency_model) for dependency_model in dependency_models]

    @classmethod
    async def delete_dependency_by_id(cls, dependency_id: int):
        async with new_session() as session:
            await session.execute(
                delete(DependencyOrm)
                .filter_by(id=dependency_id)
            )
            await session.commit()

    @classmethod
    async def delete_dependencies(cls, data: SDependencySearch):
        query = delete(DependencyOrm)

        if data.parent_id:
            query = query.where(DependencyOrm.parent_id == data.parent_id)
        if data.child_id:
            query = query.where(DependencyOrm.child_id == data.child_id)

        async with new_session() as session:
            await session.execute(query)
            await session.commit()
