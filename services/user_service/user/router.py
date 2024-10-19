from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from services.user_service.user.repository import UserRepository
from services.common.schemas.user_service.user_schemas import SUserCreate, SUserCreateResult, SUserResult, SUserGet, \
    SUserSearch, SUserPut, SUserPatch, SUserCreateResult

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("", status_code=201)
async def create_user(
        data: SUserCreate,
) -> SUserCreateResult:
    user_id = await UserRepository.create(data)
    return SUserCreateResult(
        ok=True,
        id=user_id,
    )


@router.get("/{user_id}", status_code=200)
async def get_user(
        user_id: int,
) -> SUserGet:
    user = await UserRepository.get_one(user_id)
    if user is None:
        raise HTTPException(status_code=404)
    return user


@router.get("", status_code=200)
async def get_users(
        data: Annotated[SUserSearch, Depends()],
) -> list[SUserGet]:
    users = await UserRepository.get(data)
    return users


@router.delete("/{user_id}", status_code=200)
async def delete_user(
        user_id: int,
) -> SUserResult:
    await UserRepository.delete_one(user_id)
    return SUserResult(
        ok=True,
    )


@router.delete("", status_code=200)
async def delete_users(
        data: Annotated[SUserSearch, Depends()],
) -> SUserResult:
    await UserRepository.delete(data)
    return SUserResult(
        ok=True,
    )


@router.put("/{user_id}", status_code=200)
async def update_user(
        user_id: int,
        data: SUserPut,
) -> SUserResult:
    await UserRepository.put(user_id, data)
    return SUserResult(
        ok=True,
    )


@router.patch("/{user_id}", status_code=200)
async def update_user(
        user_id: int,
        data: SUserPatch,
) -> SUserResult:
    await UserRepository.patch(user_id, data)
    return SUserResult(
        ok=True,
    )
