from typing import Type, TypeVar, List

from pydantic import BaseModel
from sqlalchemy import select, and_, delete, update, BinaryExpression
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

OrmType = TypeVar('OrmType', bound=DeclarativeBase)
InputType = TypeVar('InputType', bound=BaseModel)
OutputType = TypeVar('OutputType', bound=BaseModel)


class Repository:
    @classmethod
    async def create(
            cls,
            new_session: async_sessionmaker[AsyncSession],
            orm: Type[OrmType],
            data: InputType,
    ) -> int:
        async with new_session() as session:
            model = orm(**data.model_dump())
            session.add(model)
            await session.commit()
            return model.id

    @classmethod
    async def get(
            cls,
            new_session: async_sessionmaker[AsyncSession],
            orm: Type[OrmType],
            filters: List[bool],
            output_type: Type[OutputType],
    ) -> list[OutputType]:
        async with new_session() as session:
            result = await session.execute(
                select(orm)
                .filter(and_(*filters))
            )
            return [output_type.model_validate(model, from_attributes=True) for model in result.scalars().all()]

    @classmethod
    async def delete(
            cls,
            new_session: async_sessionmaker[AsyncSession],
            orm: Type[OrmType],
            filters: List[bool],
    ):
        async with new_session() as session:
            await session.execute(
                delete(orm)
                .filter(and_(*filters))
            )
            await session.commit()

    @classmethod
    async def put(
            cls,
            new_session: async_sessionmaker[AsyncSession],
            orm: Type[OrmType],
            filters: List[bool],
            values: dict,
    ):
        async with new_session() as session:
            await session.execute(
                update(orm)
                .where(*filters)
                .values(**values)
            )
            await session.commit()

    @classmethod
    async def patch(
            cls,
            new_session: async_sessionmaker[AsyncSession],
            orm: Type[OrmType],
            filters: List[BinaryExpression],
            values: dict,
    ):
        async with new_session() as session:
            await session.execute(
                update(orm)
                .where(*filters)
                .values(**values)
            )
            await session.commit()
