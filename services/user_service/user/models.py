from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase, SQLAlchemyBaseUserTable
from sqlalchemy import Boolean, String
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from services.user_service.database import Model, created_at, updated_at, str_pk, get_async_session, int_pk


class UserOrm(SQLAlchemyBaseUserTable[int], Model):
    __tablename__ = "user"

    id: Mapped[int_pk]

    name: Mapped[str]
    role_id: Mapped[int]
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, UserOrm)
