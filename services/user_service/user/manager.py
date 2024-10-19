import os
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin

from services.user_service.user.models import UserOrm, get_user_db


class UserManager(IntegerIDMixin, BaseUserManager[UserOrm, int]):
    reset_password_token_secret = os.getenv("SECRET")
    verification_token_secret = os.getenv("SECRET")

    async def on_after_register(self, user: UserOrm, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: UserOrm, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: UserOrm, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
