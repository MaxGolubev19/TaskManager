from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from quest_service.quest.repository import QuestRepository
from quest_service.quest.schemas import SQuestCreate, SQuestGet, SQuestResult, SQuestSearch, SQuestUpdate, SQuestCreateResult

router = APIRouter(
    prefix="/quests",
    tags=["Quests"],
)


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
