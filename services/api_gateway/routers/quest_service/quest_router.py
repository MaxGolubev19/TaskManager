import os
from typing import Annotated

import httpx
from fastapi import APIRouter, Depends, HTTPException

from services.common.schemas.quest_service.quest_schemas import SQuestCreate, SQuestCreateResult, \
    SQuestGet, SQuestSearch, SQuestResult, SQuestPut, SQuestPatch

router = APIRouter(
    prefix="/quests",
    tags=["Quests"],
)


@router.post("")
async def create_quest(
        data: SQuestCreate,
) -> SQuestCreateResult:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=f"""{os.getenv("QUEST_SERVICE_URL")}/quests""",
            json=data.dict(),
        )
    if response.status_code == 201:
        return SQuestCreateResult.model_validate(response.json())
    raise HTTPException(status_code=500)


@router.get("/{quest_id}")
async def get_quest(
        quest_id: int,
) -> SQuestGet:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=f"""{os.getenv("QUEST_SERVICE_URL")}/quests/{quest_id}""",
        )
    if response.status_code == 404:
        raise HTTPException(status_code=404)
    return SQuestGet.model_validate(response.json(), from_attributes=True)


@router.get("")
async def get_quests(
        data: Annotated[SQuestSearch, Depends()],
) -> list[SQuestGet]:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=f"""{os.getenv("QUEST_SERVICE_URL")}/quests""",
            params=data.dict(exclude_none=True),
        )
    return [SQuestGet.model_validate(quest, from_attributes=True) for quest in response.json()]


@router.delete("/{quest_id}")
async def delete_quest(
        quest_id: int,
) -> SQuestResult:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            url=f"""{os.getenv("QUEST_SERVICE_URL")}/quests/{quest_id}""",
        )
    return SQuestResult.model_validate(response.json())


@router.delete("")
async def delete_quests(
        data: Annotated[SQuestSearch, Depends()],
) -> SQuestResult:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            url=f"""{os.getenv("QUEST_SERVICE_URL")}/quests""",
            params=data.dict(exclude_none=True),
        )
    return SQuestResult.model_validate(response.json())


@router.put("/{quest_id}")
async def update_quest(
        quest_id: int,
        data: SQuestPut,
) -> SQuestResult:
    async with httpx.AsyncClient() as client:
        response = await client.put(
            url=f"""{os.getenv("QUEST_SERVICE_URL")}/quests/{quest_id}""",
            json=data.dict(),
        )
    return SQuestResult.model_validate(response.json())


@router.patch("/{quest_id}")
async def update_quest(
        quest_id: int,
        data: SQuestPatch,
) -> SQuestResult:
    async with httpx.AsyncClient() as client:
        response = await client.patch(
            url=f"""{os.getenv("QUEST_SERVICE_URL")}/quests/{quest_id}""",
            json=data.dict(),
        )
    return SQuestResult.model_validate(response.json())
