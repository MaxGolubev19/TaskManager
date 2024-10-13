from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from user_service.user.repository import UserRepository
from user_service.user.schemas import SUserCreate, SUserResult, SUserGet, SUserSearch, SUserUpdate, SUserCreateResult

router = APIRouter(
    prefix='/users',
    tags=["Users"],
)


@router.post("")
async def create_user(
        data: Annotated[SUserCreate, Depends()]
) -> SUserCreateResult:
    user_id = await UserRepository.create(data)
    return SUserCreateResult(
        ok=True,
        id=user_id,
    )


@router.get("/{user_id}")
async def get_user_by_id(user_id: int) -> SUserGet:
    user = await UserRepository.get_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404)
    return user


@router.get("")
async def get_users(
        data: Annotated[SUserSearch, Depends()]
) -> list[SUserGet]:
    users = await UserRepository.get(data)
    return users


@router.delete("/{user_id}")
async def delete_user_by_id(user_id: int) -> SUserResult:
    await UserRepository.delete_by_id(user_id)
    return SUserResult(
        ok=True,
    )


@router.delete("")
async def delete_users(
        data: Annotated[SUserSearch, Depends()]
) -> SUserResult:
    await UserRepository.delete(data)
    return SUserResult(
        ok=True,
    )


@router.patch("")
async def update_user(
        data: Annotated[SUserUpdate, Depends()]
) -> SUserResult:
    await UserRepository.update(data)
    return SUserResult(
        ok=True,
    )