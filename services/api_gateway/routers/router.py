import os
from typing import TypeVar, Type

import httpx
from fastapi import HTTPException
from pydantic import BaseModel

InputType = TypeVar('InputType', bound=BaseModel)
OutputType = TypeVar('OutputType', bound=BaseModel)


async def create(
        url: str,
        data: InputType,
        output_type: Type[OutputType],
) -> OutputType:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=url,
            json=data.dict(),
            headers={
                "x-api-key": os.getenv("INSIDE_API_KEY"),
            },
        )
    if response.status_code == 201:
        return output_type.model_validate(response.json())
    raise HTTPException(status_code=response.status_code, detail=response.text)


async def get_one(
        url: str,
        output_type: Type[OutputType],
) -> OutputType:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=url,
            headers={
                "x-api-key": os.getenv("INSIDE_API_KEY"),
            },
        )
    if response.status_code == 200:
        return output_type.model_validate(response.json(), from_attributes=True)
    raise HTTPException(status_code=response.status_code, detail=response.text)


async def get(
        url: str,
        data: InputType,
        output_type: Type[OutputType],
) -> list[OutputType]:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=url,
            params=data.dict(exclude_none=True),
            headers={
                "x-api-key": os.getenv("INSIDE_API_KEY"),
            },
        )
    if response.status_code == 200:
        return [output_type.model_validate(el, from_attributes=True) for el in response.json()]
    raise HTTPException(status_code=response.status_code, detail=response.text)


async def delete_one(
        url: str,
        output_type: Type[OutputType],
) -> OutputType:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            url=url,
            headers={
                "x-api-key": os.getenv("INSIDE_API_KEY"),
            },
        )
    if response.status_code == 200:
        return output_type.model_validate(response.json())
    raise HTTPException(status_code=response.status_code, detail=response.text)


async def delete(
        url: str,
        data: InputType,
        output_type: Type[OutputType],
) -> OutputType:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            url=url,
            params=data.dict(exclude_none=True),
            headers={
                "x-api-key": os.getenv("INSIDE_API_KEY"),
            },
        )
    if response.status_code == 200:
        return output_type.model_validate(response.json())
    raise HTTPException(status_code=response.status_code, detail=response.text)


async def put(
        url: str,
        data: InputType,
        output_type: Type[OutputType],
) -> OutputType:
    async with httpx.AsyncClient() as client:
        response = await client.put(
            url=url,
            json=data.dict(),
            headers={
                "x-api-key": os.getenv("INSIDE_API_KEY"),
            },
        )
    if response.status_code == 200:
        return output_type.model_validate(response.json())
    raise HTTPException(status_code=response.status_code, detail=response.text)


async def patch(
        url: str,
        data: InputType,
        output_type: Type[OutputType],
) -> OutputType:
    async with httpx.AsyncClient() as client:
        response = await client.patch(
            url=url,
            json=data.dict(),
            headers={
                "x-api-key": os.getenv("INSIDE_API_KEY"),
            },
        )
    if response.status_code == 200:
        return output_type.model_validate(response.json())
    raise HTTPException(status_code=response.status_code, detail=response.text)
