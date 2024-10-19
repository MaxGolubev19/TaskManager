import os

from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader


def check_api_key(api_key: str = Depends(APIKeyHeader(name="x-api-key", auto_error=False))):
    if api_key is None:
        raise HTTPException(
            status_code=401,
            detail="API key missing",
        )
    if api_key != os.getenv("API_KEY"):
        raise HTTPException(
            status_code=403,
            detail="Invalid API key",
        )
    return api_key
