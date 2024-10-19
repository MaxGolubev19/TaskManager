from typing import Annotated

from fastapi import APIRouter, Depends

from services.quest_service.dependency.repository import DependencyRepository
from services.common.schemas.quest_service.dependency_schemas import SDependencyCreate, SDependencyGet, \
    SDependencySearch, SDependencyResult

router = APIRouter(
    prefix="/dependencies",
    tags=["Dependencies"],
)


@router.post("", status_code=201)
async def create_dependency(
        data: SDependencyCreate,
) -> SDependencyResult:
    await DependencyRepository.create(data)
    return SDependencyResult(
        ok=True,
    )


@router.get("", status_code=200)
async def get_dependencies(
        data: Annotated[SDependencySearch, Depends()],
) -> list[SDependencyGet]:
    dependencies = await DependencyRepository.get(data)
    return dependencies


@router.delete("", status_code=200)
async def delete_dependencies(
        data: Annotated[SDependencySearch, Depends()],
) -> SDependencyResult:
    await DependencyRepository.delete(data)
    return SDependencyResult(
        ok=True,
    )
