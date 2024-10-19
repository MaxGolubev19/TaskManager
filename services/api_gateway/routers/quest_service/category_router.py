import os
from typing import Annotated

from fastapi import APIRouter, Depends

from services.api_gateway.routers.router import create, get_one, get, delete_one, delete, put, patch
from services.common.schemas.quest_service.category_schemas import SCategoryCreate, SCategoryCreateResult, \
    SCategoryGet, SCategorySearch, SCategoryResult, SCategoryPut, SCategoryPatch

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.post("")
async def create_category(
        data: SCategoryCreate,
) -> SCategoryCreateResult:
    return await create(
        url=f"""{os.getenv("QUEST_SERVICE_URL")}/categories""",
        data=data,
        output_type=SCategoryCreateResult,
    )


@router.get("/{category_id}")
async def get_quest(
        category_id: int,
) -> SCategoryGet:
    return await get_one(
        url=f"""{os.getenv("QUEST_SERVICE_URL")}/categories/{category_id}""",
        output_type=SCategoryGet,
    )


@router.get("")
async def get_categories(
        data: Annotated[SCategorySearch, Depends()],
) -> list[SCategoryGet]:
    return await get(
        url=f"""{os.getenv("QUEST_SERVICE_URL")}/categories""",
        data=data,
        output_type=SCategoryGet,
    )


@router.delete("/{category_id}")
async def delete_category(
        category_id: int,
) -> SCategoryResult:
    return await delete_one(
        url=f"""{os.getenv("QUEST_SERVICE_URL")}/categories/{category_id}""",
        output_type=SCategoryResult,
    )


@router.delete("")
async def delete_categories(
        data: Annotated[SCategorySearch, Depends()],
) -> SCategoryResult:
    return await delete(
        url=f"""{os.getenv("QUEST_SERVICE_URL")}/categories""",
        data=data,
        output_type=SCategoryResult,
    )


@router.put("/{category_id_id}")
async def update_category_id(
        category_id: int,
        data: SCategoryPut,
) -> SCategoryResult:
    return await put(
        url=f"""{os.getenv("QUEST_SERVICE_URL")}/categories/{category_id}""",
        data=data,
        output_type=SCategoryResult,
    )


@router.patch("/{category_id}")
async def update_category(
        category_id: int,
        data: SCategoryPatch,
) -> SCategoryResult:
    return await patch(
        url=f"""{os.getenv("QUEST_SERVICE_URL")}/categories/{category_id}""",
        data=data,
        output_type=SCategoryResult,
    )
