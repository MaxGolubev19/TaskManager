# `api.py`

Этот модуль реализует проверку API-ключа для защиты эндпоинтов.

## Функции

### `check_api_key`
```python
check_api_key(api_key: str = Depends(APIKeyHeader(name="x-api-key", auto_error=False)))
```
- Используется `fastapi.security.APIKeyHeader` для обработки заголовка API-ключа.
- Проверяет наличие заголовка `x-api-key` в запросе.
- Если ключ отсутствует, возвращает **401 Unauthorized**.
- Если ключ не совпадает с переменной окружения `API_KEY`, возвращает **403 Forbidden**.
- В случае успешной проверки возвращает переданный API-ключ.

### Пример использования
```python
from fastapi import APIRouter, Depends
from services.common.utils.api import check_api_key

router = APIRouter(prefix="/example", dependencies=[Depends(check_api_key)])

@router.get("/")
def protected_route():
    return {"message": "Access granted"}
```
