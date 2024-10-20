from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from services.user_service.user.auth import auth_backend
from services.user_service.user.manager import get_user_manager
from services.user_service.user.models import UserOrm
from services.common.schemas.user_service.user_schemas import SUserCreate, SUserGet

fastapi_users = FastAPIUsers[UserOrm, int](
    get_user_manager,
    [auth_backend],
)


router = APIRouter(
    tags=["Auth"],
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
)

router.include_router(
    fastapi_users.get_register_router(SUserGet, SUserCreate),
    prefix="/auth",
)

router.include_router(
    fastapi_users.get_verify_router(SUserGet),
    prefix="/auth",
)

router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
)
