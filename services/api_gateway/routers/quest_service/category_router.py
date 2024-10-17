import os
from typing import Annotated

import httpx
from fastapi import APIRouter, Depends, HTTPException

from services.common.schemas.quest_service.category_schemas import SCategoryCreate, SCategoryCreateResult, \
    SCategoryGet, SCategorySearch, SCategoryResult, SCategoryPut, SCategoryPatch

router = APIRouter(
    prefix="/categoties",
    tags=["Categories"],
)


@router.post("")
async def create_category(
        data: SCategoryCreate,
) -> SCategoryCreateResult:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=f"""{os.getenv("QUEST_SERVICE_URL")}/categories""",
            json=data.dict(),
        )
    if response.status_code == 201:
        return SCategoryCreateResult.model_validate(response.json())
    raise HTTPException(status_code=500)


@router.get("/{category_id}")
async def get_quest(
        category_id: int,
) -> SCategoryGet:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=f"""{os.getenv("QUEST_SERVICE_URL")}/categories/{category_id}""",
        )
    if response.status_code == 404:
        raise HTTPException(status_code=404)
    return SCategoryGet.model_validate(response.json(), from_attributes=True)


@router.get("")
async def get_categories(
        data: Annotated[SCategorySearch, Depends()],
) -> list[SCategoryGet]:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=f"""{os.getenv("QUEST_SERVICE_URL")}/categories""",
            params=data.dict(exclude_none=True),
        )
    return [SCategoryGet.model_validate(category, from_attributes=True) for category in response.json()]


@router.delete("/{category_id}")
async def delete_category(
        category_id: int,
) -> SCategoryResult:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            url=f"""{os.getenv("QUEST_SERVICE_URL")}/categories/{category_id}""",
        )
    return SCategoryResult.model_validate(response.json())


@router.delete("")
async def delete_categories(
        data: Annotated[SCategorySearch, Depends()],
) -> SCategoryResult:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            url=f"""{os.getenv("QUEST_SERVICE_URL")}/categories""",
            params=data.dict(exclude_none=True),
        )
    return SCategoryResult.model_validate(response.json())


@router.put("/{category_id_id}")
async def update_category_id(
        category_id: int,
        data: SCategoryPut,
) -> SCategoryResult:
    async with httpx.AsyncClient() as client:
        response = await client.put(
            url=f"""{os.getenv("QUEST_SERVICE_URL")}/categories/{category_id}""",
            json=data.dict(),
        )
    return SCategoryResult.model_validate(response.json())


@router.patch("/{category_id}")
async def update_category(
        category_id: int,
        data: SCategoryPatch,
) -> SCategoryResult:
    async with httpx.AsyncClient() as client:
        response = await client.patch(
            url=f"""{os.getenv("QUEST_SERVICE_URL")}/categories/{category_id}""",
            json=data.dict(),
        )
    return SCategoryResult.model_validate(response.json())
