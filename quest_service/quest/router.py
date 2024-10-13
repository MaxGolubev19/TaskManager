from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException

from quest_service.quest.repository import QuestRepository
from quest_service.quest.schemas import SQuestCreate, SQuestGet, SQuestResult, SQuestSearch, SQuestUpdate, SDependencyCreate, \
    SDependencyGet, SDependencySearch, SQuestCreateResult

router = APIRouter(
    prefix="/quests",
    tags=["Quests"],
)


dependency_router = APIRouter(
    prefix="/dependencies",
)


@dependency_router.post("")
async def create_dependency(
        data: Annotated[SDependencyCreate, Depends()]
) -> SQuestCreateResult:
    dependency_id = await QuestRepository.create_dependency(data)
    return SQuestCreateResult(
        ok=True,
        id=dependency_id,
    )


@dependency_router.get("/{dependency_id}")
async def get_dependency_by_id(dependency_id: int) -> Optional[SDependencyGet]:
    dependency = await QuestRepository.get_dependency_by_id(dependency_id)
    return dependency


@dependency_router.get("")
async def get_dependencies(
        data: Annotated[SDependencySearch, Depends()]
) -> list[SDependencyGet]:
    dependencies = await QuestRepository.get_dependencies(data)
    return dependencies


@dependency_router.delete("/{dependency_id}")
async def delete_dependency_by_id(dependency_id: int) -> SQuestResult:
    await QuestRepository.delete_dependency_by_id(dependency_id)
    return SQuestResult(
        ok=True,
    )


@dependency_router.delete("")
async def delete_dependencies(
    data: Annotated[SDependencySearch, Depends()]
) -> SQuestResult:
    await QuestRepository.delete_dependencies(data)
    return SQuestResult(
        ok=True,
    )


router.include_router(dependency_router)


@router.post("")
async def create_quest(
        data: Annotated[SQuestCreate, Depends()]
) -> SQuestCreateResult:
    quest_id = await QuestRepository.create_quest(data)
    return SQuestCreateResult(
        ok=True,
        id=quest_id,
    )


@router.get("/{quest_id}")
async def get_quest_by_id(quest_id: int) -> SQuestGet:
    quest = await QuestRepository.get_quest_by_id(quest_id)
    if quest is None:
        raise HTTPException(status_code=404)
    return quest


@router.get("")
async def get_quests(
        data: Annotated[SQuestSearch, Depends()]
) -> list[SQuestGet]:
    quests = await QuestRepository.get_quests(data)
    return quests


@router.delete("/{quest_id}")
async def delete_quest_by_id(quest_id: int) -> SQuestResult:
    await QuestRepository.delete_quest_by_id(quest_id)
    return SQuestResult(
        ok=True,
    )


@router.delete("")
async def delete_quests(
    data: Annotated[SQuestSearch, Depends()]
) -> SQuestResult:
    await QuestRepository.delete_quests(data)
    return SQuestResult(
        ok=True,
    )


@router.patch("")
async def update_quest(
        data: Annotated[SQuestUpdate, Depends()],
) -> SQuestResult:
    await QuestRepository.update_quest(data)
    return SQuestResult(
        ok=True,
    )
