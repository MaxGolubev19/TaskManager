from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from services.quest_service.category.repository import CategoryRepository
from services.common.schemas.quest_service.category_schemas import SCategoryCreate, SCategoryResult, SCategoryGet, \
    SCategorySearch, SCategoryPatch, SCategoryCreateResult, SCategoryPut

router = APIRouter(
    prefix='/categories',
    tags=["Categories"],
)


@router.post("", status_code=201)
async def create_category(
        data: SCategoryCreate,
) -> SCategoryCreateResult:
    category_id = await CategoryRepository.create(data)
    return SCategoryCreateResult(
        ok=True,
        id=category_id,
    )


@router.get("/{category_id}")
async def get_category_by_id(
        category_id: int,
) -> SCategoryGet:
    category = await CategoryRepository.get_one(category_id)
    if category is None:
        raise HTTPException(status_code=404)
    return category


@router.get("")
async def get_categories(
        data: Annotated[SCategorySearch, Depends()],
) -> list[SCategoryGet]:
    categories = await CategoryRepository.get(data)
    return categories


@router.delete("/{category_id}")
async def delete_category_by_id(
        category_id: int,
) -> SCategoryResult:
    await CategoryRepository.delete_one(category_id)
    return SCategoryResult(
        ok=True,
    )


@router.delete("")
async def delete_categories(
        data: Annotated[SCategorySearch, Depends()],
) -> SCategoryResult:
    await CategoryRepository.delete(data)
    return SCategoryResult(
        ok=True,
    )


@router.put("/{category_id}")
async def update_category(
        category_id: int,
        data: SCategoryPut,
) -> SCategoryResult:
    await CategoryRepository.put(category_id, data)
    return SCategoryResult(
        ok=True,
    )


@router.patch("/{category_id}")
async def update_category(
        category_id: int,
        data: SCategoryPatch,
) -> SCategoryResult:
    await CategoryRepository.patch(category_id, data)
    return SCategoryResult(
        ok=True,
    )
