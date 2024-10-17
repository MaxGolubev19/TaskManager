import os
from typing import Annotated

import httpx
from fastapi import APIRouter, Depends, HTTPException

from services.common.schemas.quest_service.dependency_schemas import SDependencyCreate, SDependencyResult, \
    SDependencyGet, SDependencySearch, SDependencyResult

router = APIRouter(
    prefix="/dependencies",
    tags=["Dependencies"],
)


@router.post("")
async def create_dependency(
        data: SDependencyCreate,
) -> SDependencyResult:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=f"""{os.getenv("QUEST_SERVICE_URL")}/dependencies""",
            json=data.dict(),
        )
    if response.status_code == 201:
        return SDependencyResult.model_validate(response.json())
    raise HTTPException(status_code=500)


@router.get("")
async def get_dependencies(
        data: Annotated[SDependencySearch, Depends()],
) -> list[SDependencyGet]:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=f"""{os.getenv("QUEST_SERVICE_URL")}/dependencies""",
            params=data.dict(exclude_none=True),
        )
    return [SDependencyGet.model_validate(dependency, from_attributes=True) for dependency in response.json()]


@router.delete("")
async def delete_dependencies(
        data: Annotated[SDependencySearch, Depends()],
) -> SDependencyResult:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            url=f"""{os.getenv("QUEST_SERVICE_URL")}/dependencies""",
            params=data.dict(exclude_none=True),
        )
    return SDependencyResult.model_validate(response.json())
