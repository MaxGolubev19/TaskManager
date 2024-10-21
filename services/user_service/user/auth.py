import os
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin
from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend

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


cookie_transport = CookieTransport(cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=os.getenv("SECRET"),
        lifetime_seconds=3600
    )


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
