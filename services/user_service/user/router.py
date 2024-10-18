from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from services.common.utils import check_api_key
from services.user_service.user.repository import UserRepository
from services.common.schemas.user_service.user_schemas import SUserCreate, SUserResult, SUserGet, SUserSearch, \
    SUserPatch, SUserPut

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("", status_code=201)
async def create_user(
        data: SUserCreate,
) -> SUserResult:
    await UserRepository.create(data)
    return SUserResult(
        ok=True,
    )


@router.get("/{user_name}", status_code=200)
async def get_user(
        user_name: str,
        api_key=Depends(check_api_key),
) -> SUserGet:
    user = await UserRepository.get_one(user_name)
    if user is None:
        raise HTTPException(status_code=404)
    return user


@router.get("", status_code=200)
async def get_users(
        data: Annotated[SUserSearch, Depends()],
        api_key=Depends(check_api_key),
) -> list[SUserGet]:
    users = await UserRepository.get(data)
    return users


@router.delete("/{user_name}", status_code=200)
async def delete_user(
        user_name: str,
        api_key=Depends(check_api_key),
) -> SUserResult:
    await UserRepository.delete_one(user_name)
    return SUserResult(
        ok=True,
    )


@router.delete("", status_code=200)
async def delete_users(
        data: Annotated[SUserSearch, Depends()],
        api_key=Depends(check_api_key),
) -> SUserResult:
    await UserRepository.delete(data)
    return SUserResult(
        ok=True,
    )


@router.put("/{user_name}", status_code=200)
async def update_user(
        user_name: str,
        data: SUserPut,
        api_key=Depends(check_api_key),
) -> SUserResult:
    await UserRepository.put(user_name, data)
    return SUserResult(
        ok=True,
    )


@router.patch("/{user_name}", status_code=200)
async def update_user(
        user_name: str,
        data: SUserPatch,
        api_key=Depends(check_api_key),
) -> SUserResult:
    await UserRepository.patch(user_name, data)
    return SUserResult(
        ok=True,
    )
