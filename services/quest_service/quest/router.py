from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from services.quest_service.quest.repository import QuestRepository
from services.common.schemas.quest_service.quest_schemas import SQuestCreate, SQuestGet, SQuestResult, SQuestSearch, \
    SQuestPatch, SQuestCreateResult, SQuestPut

router = APIRouter(
    prefix="/quests",
    tags=["Quests"],
)


@router.post("", status_code=201)
async def create_quest(
        data: SQuestCreate,
) -> SQuestCreateResult:
    quest_id = await QuestRepository.create(data)
    return SQuestCreateResult(
        ok=True,
        id=quest_id,
    )


@router.get("/{quest_id}", status_code=200)
async def get_quest_by_id(
        quest_id: int,
) -> SQuestGet:
    quest = await QuestRepository.get_one(quest_id)
    if quest is None:
        raise HTTPException(status_code=404)
    return quest


@router.get("", status_code=200)
async def get_quests(
        data: Annotated[SQuestSearch, Depends()],
) -> list[SQuestGet]:
    quests = await QuestRepository.get(data)
    return quests


@router.delete("/{quest_id}", status_code=200)
async def delete_quest_by_id(
        quest_id: int,
) -> SQuestResult:
    await QuestRepository.delete_one(quest_id)
    return SQuestResult(
        ok=True,
    )


@router.delete("", status_code=200)
async def delete_quests(
        data: Annotated[SQuestSearch, Depends()],
) -> SQuestResult:
    await QuestRepository.delete(data)
    return SQuestResult(
        ok=True,
    )


@router.put("/{quest_id}", status_code=200)
async def update_quest(
        quest_id: int,
        data: SQuestPut,
) -> SQuestResult:
    await QuestRepository.put(quest_id, data)
    return SQuestResult(
        ok=True,
    )


@router.patch("/{quest_id}", status_code=200)
async def update_quest(
        quest_id: int,
        data: SQuestPatch,
) -> SQuestResult:
    await QuestRepository.patch(quest_id, data)
    return SQuestResult(
        ok=True,
    )
