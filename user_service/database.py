import os
from datetime import datetime
from typing import Annotated

from sqlalchemy import Integer, text, String
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, mapped_column


engine = create_async_engine(
    url=os.getenv("DATABASE_URL"),
)
new_session = async_sessionmaker(engine, expire_on_commit=False)


int_pk = Annotated[int, mapped_column(primary_key=True)]
str_pk = Annotated[Annotated[str, 200], mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    onupdate=datetime.utcnow()
)]


class Model(DeclarativeBase):
    type_annotation_map = {
        int_pk: Integer,
        str_pk: String(50),
    }

    def __repr__(self):
        cols = [f"{col}={getattr(self, col)}" for idx, col in enumerate(self.__table__.columns.keys())]
        return f"<{self.__class__.__name__}> {', '.join(cols)}"


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
        await conn.run_sync(Model.metadata.create_all)
