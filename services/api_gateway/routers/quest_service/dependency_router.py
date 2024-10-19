import os
from typing import Annotated

from fastapi import APIRouter, Depends

from services.api_gateway.routers.router import create, get, delete
from services.common.schemas.quest_service.dependency_schemas import SDependencyCreate, SDependencyResult, \
    SDependencyGet, SDependencySearch

router = APIRouter(
    prefix="/dependencies",
    tags=["Dependencies"],
)


@router.post("")
async def create_dependency(
        data: SDependencyCreate,
) -> SDependencyResult:
    return await create(
        url=f"""{os.getenv("QUEST_SERVICE_URL")}/dependencies""",
        data=data,
        output_type=SDependencyResult,
    )


@router.get("")
async def get_dependencies(
        data: Annotated[SDependencySearch, Depends()],
) -> list[SDependencyGet]:
    return await get(
        url=f"""{os.getenv("QUEST_SERVICE_URL")}/dependencies""",
        data=data,
        output_type=SDependencyGet,
    )


@router.delete("")
async def delete_dependencies(
        data: Annotated[SDependencySearch, Depends()],
) -> SDependencyResult:
    return await delete(
        url=f"""{os.getenv("QUEST_SERVICE_URL")}/dependencies""",
        data=data,
        output_type=SDependencyResult,
    )
