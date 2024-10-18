import os
from typing import Annotated

from fastapi import APIRouter, Depends

from services.api_gateway.routers.router import create, get_one, get, delete_one, delete, put, patch
from services.common.schemas.adventure_service.adventure_schemas import SAdventureCreate, SAdventureCreateResult, \
    SAdventureGet, SAdventureSearch, SAdventureResult, SAdventurePut, SAdventurePatch
from services.common.utils import check_api_key

router = APIRouter(
    prefix="/adventures",
    tags=["Adventures"],
)


@router.post("")
async def create_adventure(
        data: SAdventureCreate,
        api_key: str = Depends(check_api_key),
) -> SAdventureCreateResult:
    return await create(
        url=f"""{os.getenv("ADVENTURE_SERVICE_URL")}/adventures""",
        data=data,
        output_type=SAdventureCreateResult,
    )


@router.get("/{adventure_id}")
async def get_adventure(
        adventure_id: int,
        api_key: str = Depends(check_api_key),
) -> SAdventureGet:
    return await get_one(
        url=f"""{os.getenv("ADVENTURE_SERVICE_URL")}/adventures/{adventure_id}""",
        output_type=SAdventureGet,
    )


@router.get("")
async def get_adventures(
        data: Annotated[SAdventureSearch, Depends()],
        api_key: str = Depends(check_api_key),
) -> list[SAdventureGet]:
    return await get(
        url=f"""{os.getenv("ADVENTURE_SERVICE_URL")}/adventures""",
        data=data,
        output_type=SAdventureGet,
    )


@router.delete("/{adventure_id}")
async def delete_adventure(
        adventure_id: int,
        api_key: str = Depends(check_api_key),
) -> SAdventureResult:
    return await delete_one(
        url=f"""{os.getenv("ADVENTURE_SERVICE_URL")}/adventures/{adventure_id}""",
        output_type=SAdventureResult,
    )


@router.delete("")
async def delete_adventures(
        data: Annotated[SAdventureSearch, Depends()],
        api_key: str = Depends(check_api_key),
) -> SAdventureResult:
    return await delete(
        url=f"""{os.getenv("ADVENTURE_SERVICE_URL")}/adventures""",
        data=data,
        output_type=SAdventureResult,
    )


@router.put("/{adventure_id}")
async def update_adventure(
        adventure_id: int,
        data: SAdventurePut,
        api_key: str = Depends(check_api_key),
) -> SAdventureResult:
    return await put(
        url=f"""{os.getenv("ADVENTURE_SERVICE_URL")}/adventures/{adventure_id}""",
        data=data,
        output_type=SAdventureResult,
    )


@router.patch("/{adventure_id}")
async def update_adventure(
        adventure_id: int,
        data: SAdventurePatch,
        api_key: str = Depends(check_api_key),
) -> SAdventureResult:
    return await patch(
        url=f"""{os.getenv("ADVENTURE_SERVICE_URL")}/adventures/{adventure_id}""",
        data=data,
        output_type=SAdventureResult,
    )
