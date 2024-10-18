import os
from typing import Annotated

from fastapi import APIRouter, Depends

from services.api_gateway.routers.router import create, get_one, get, delete_one, delete, put, patch
from services.common.schemas.quest_service.quest_schemas import SQuestCreate, SQuestCreateResult, SQuestGet, \
    SQuestSearch, SQuestResult, SQuestPut, SQuestPatch
from services.common.utils import check_api_key

router = APIRouter(
    prefix="/quests",
    tags=["Quests"],
)


@router.post("")
async def create_quest(
        data: SQuestCreate,
        api_key: str = Depends(check_api_key),
) -> SQuestCreateResult:
    return await create(
        url=f"""{os.getenv("QUEST_SERVICE_URL")}/quests""",
        data=data,
        output_type=SQuestCreateResult,
    )


@router.get("/{quest_id}")
async def get_quest(
        quest_id: int,
        api_key: str = Depends(check_api_key),
) -> SQuestGet:
    return await get_one(
        url=f"""{os.getenv("QUEST_SERVICE_URL")}/quests/{quest_id}""",
        output_type=SQuestGet,
    )


@router.get("")
async def get_quests(
        data: Annotated[SQuestSearch, Depends()],
        api_key: str = Depends(check_api_key),
) -> list[SQuestGet]:
    return await get(
        url=f"""{os.getenv("QUEST_SERVICE_URL")}/quests""",
        data=data,
        output_type=SQuestGet,
    )


@router.delete("/{quest_id}")
async def delete_quest(
        quest_id: int,
        api_key: str = Depends(check_api_key),
) -> SQuestResult:
    return await delete_one(
        url=f"""{os.getenv("QUEST_SERVICE_URL")}/quests/{quest_id}""",
        output_type=SQuestResult,
    )


@router.delete("")
async def delete_quests(
        data: Annotated[SQuestSearch, Depends()],
        api_key: str = Depends(check_api_key),
) -> SQuestResult:
    return await delete(
        url=f"""{os.getenv("QUEST_SERVICE_URL")}/quests""",
        data=data,
        output_type=SQuestResult,
    )


@router.put("/{quest_id}")
async def update_quest(
        quest_id: int,
        data: SQuestPut,
        api_key: str = Depends(check_api_key),
) -> SQuestResult:
    return await put(
        url=f"""{os.getenv("QUEST_SERVICE_URL")}/quests/{quest_id}""",
        data=data,
        output_type=SQuestResult,
    )


@router.patch("/{quest_id}")
async def update_quest(
        quest_id: int,
        data: SQuestPatch,
        api_key: str = Depends(check_api_key),
) -> SQuestResult:
    return await patch(
        url=f"""{os.getenv("QUEST_SERVICE_URL")}/quests/{quest_id}""",
        data=data,
        output_type=SQuestResult,
    )
