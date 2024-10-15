from typing import Annotated

from fastapi import APIRouter, Depends

from services.quest_service.dependency.repository import DependencyRepository
from services.quest_service.dependency.schemas import SDependencyCreate, SDependencyGet, SDependencySearch, SDependencyResult

router = APIRouter(
    prefix="/dependencies",
    tags=["Dependencies"],
)


@router.post("")
async def create_dependency(
        data: Annotated[SDependencyCreate, Depends()]
) -> SDependencyResult:
    await DependencyRepository.create(data)
    return SDependencyResult(
        ok=True,
    )


@router.get("")
async def get_dependencies(
        data: Annotated[SDependencySearch, Depends()]
) -> list[SDependencyGet]:
    dependencies = await DependencyRepository.get(data)
    return dependencies


@router.delete("")
async def delete_dependencies(
    data: Annotated[SDependencySearch, Depends()]
) -> SDependencyResult:
    await DependencyRepository.delete(data)
    return SDependencyResult(
        ok=True,
    )
