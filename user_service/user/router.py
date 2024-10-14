from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from user_service.user.repository import UserRepository
from user_service.user.schemas import SUserCreate, SUserResult, SUserGet, SUserSearch, SUserUpdate

router = APIRouter(
    prefix='/users',
    tags=["Users"],
)


@router.post("")
async def create_user(
        data: Annotated[SUserCreate, Depends()]
) -> SUserResult:
    await UserRepository.create(data)
    return SUserResult(
        ok=True,
    )


@router.get("/{user_name}")
async def get_user(user_name: str) -> SUserGet:
    user = await UserRepository.get_one(user_name)
    if user is None:
        raise HTTPException(status_code=404)
    return user


@router.get("")
async def get_users(
        data: Annotated[SUserSearch, Depends()]
) -> list[SUserGet]:
    users = await UserRepository.get(data)
    return users


@router.delete("/{user_name}")
async def delete_user(user_name: str) -> SUserResult:
    await UserRepository.delete_one(user_name)
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