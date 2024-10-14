from typing import Annotated

from fastapi import APIRouter, Depends

from quest_service.dependency.repository import DependencyRepository
from quest_service.dependency.schemas import SDependencyCreate, SDependencyGet, SDependencySearch, SDependencyResult

router = APIRouter(
    prefix="/dependencies",
    tags=["Dependencies"],
)


@router.post("")
async def create_dependency(
        data: Annotated[SDependencyCreate, Depends()]
) -> SDependencyResult:
    await DependencyRepository.create_dependency(data)
    return SDependencyResult(
        ok=True,
    )


@router.get("")
async def get_dependencies(
        data: Annotated[SDependencySearch, Depends()]
) -> list[SDependencyGet]:
    dependencies = await DependencyRepository.get_dependencies(data)
    return dependencies


@router.delete("")
async def delete_dependencies(
    data: Annotated[SDependencySearch, Depends()]
) -> SDependencyResult:
    await DependencyRepository.delete_dependencies(data)
    return SDependencyResult(
        ok=True,
    )
