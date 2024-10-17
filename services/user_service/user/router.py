from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

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


@router.get("/{user_name}")
async def get_user(
        user_name: str,
) -> SUserGet:
    user = await UserRepository.get_one(user_name)
    if user is None:
        raise HTTPException(status_code=404)
    return user


@router.get("")
async def get_users(
        data: Annotated[SUserSearch, Depends()],
) -> list[SUserGet]:
    users = await UserRepository.get(data)
    return users


@router.delete("/{user_name}")
async def delete_user(
        user_name: str,
) -> SUserResult:
    await UserRepository.delete_one(user_name)
    return SUserResult(
        ok=True,
    )


@router.delete("")
async def delete_users(
        data: Annotated[SUserSearch, Depends()],
) -> SUserResult:
    await UserRepository.delete(data)
    return SUserResult(
        ok=True,
    )


@router.put("/{user_name}")
async def update_user(
        user_name: str,
        data: SUserPut,
) -> SUserResult:
    await UserRepository.put(user_name, data)
    return SUserResult(
        ok=True,
    )


@router.patch("/{user_name}")
async def update_user(
        user_name: str,
        data: SUserPatch,
) -> SUserResult:
    await UserRepository.patch(user_name, data)
    return SUserResult(
        ok=True,
    )
