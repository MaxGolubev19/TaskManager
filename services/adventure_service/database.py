import os
from datetime import datetime
from typing import Annotated

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, mapped_column


engine = create_async_engine(
    url=os.getenv("DATABASE_URL"),
)
new_session = async_sessionmaker(engine, expire_on_commit=False)


created_at = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
)]

updated_at = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    onupdate=datetime.utcnow(),
)]


class Model(DeclarativeBase):
    def __repr__(self):
        cols = [f"{col}={getattr(self, col)}" for idx, col in enumerate(self.__table__.columns.keys())]
        return f"<{self.__class__.__name__}> {', '.join(cols)}"


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
        await conn.run_sync(Model.metadata.create_all)
