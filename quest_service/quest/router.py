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
        data: Annotated[SQuestCreate, Depends()],
) -> SQuestCreateResult:
    quest_id = await QuestRepository.create(data)
    return SQuestCreateResult(
        ok=True,
        id=quest_id,
    )


@router.get("/{quest_id}")
async def get_quest_by_id(
        quest_id: int,
) -> SQuestGet:
    quest = await QuestRepository.get_one(quest_id)
    if quest is None:
        raise HTTPException(status_code=404)
    return quest


@router.get("")
async def get_quests(
        data: Annotated[SQuestSearch, Depends()],
) -> list[SQuestGet]:
    quests = await QuestRepository.get(data)
    return quests


@router.delete("/{quest_id}")
async def delete_quest_by_id(
        quest_id: int,
) -> SQuestResult:
    await QuestRepository.delete_one(quest_id)
    return SQuestResult(
        ok=True,
    )


@router.delete("")
async def delete_quests(
    data: Annotated[SQuestSearch, Depends()],
) -> SQuestResult:
    await QuestRepository.delete(data)
    return SQuestResult(
        ok=True,
    )


@router.put("/{quest_id}")
async def update_quest(
        quest_id: int,
        data: Annotated[SQuestUpdate, Depends()],
) -> SQuestResult:
    await QuestRepository.put(quest_id, data)
    return SQuestResult(
        ok=True,
    )


@router.patch("/{quest_id}")
async def update_quest(
        quest_id: int,
        data: Annotated[SQuestUpdate, Depends()],
) -> SQuestResult:
    await QuestRepository.patch(quest_id, data)
    return SQuestResult(
        ok=True,
    )
