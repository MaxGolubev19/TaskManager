# `schemas/`
Эта папка содержит набор схем взаимодействия с базой данных, разбитых по микросервисам, для каждой сущности.

## `adventure_service/adventure_schemas.py`
Этот файл содержит схемы данных для работы с сущностью **Adventure**. Все схемы используют библиотеку Pydantic для валидации и сериализации данных.Схемы других сущностей выглядят аналогично.

## Схемы:

### `SAdventureGet`
Схема ответа на GET-запрос.

Поля:
- `id` (int): уникальный идентификатор **Adventure**.
- `name` (str): название **Adventure**.
- `party_id` (int): идентификатор команды, к которой принадлежит **Adventure**.
- `created_at` (datetime): дата и время создания записи.
- `updated_at` (datetime): дата и время последнего обновления записи.

```python
class SAdventureGet(BaseModel):
    id: int
    name: str
    party_id: int
    created_at: datetime
    updated_at: datetime
```

---

### `SAdventureCreate`
Схема параметров для POST-запроса.

Поля:
- `name` (str): название **Adventure**.
- `party_id` (int): идентификатор команды, к которой будет принадлежать **Adventure**.

```python
class SAdventureCreate(BaseModel):
    name: str
    party_id: int
```

---

### `SAdventureSearch`
Схема параметров для GET-запроса и DELETE-запроса.

Поля:
- `name` (Optional[str]): название **Adventure** (необязательное).
- `party_id` (Optional[int]): идентификатор команды (необязательное).

```python
class SAdventureSearch(BaseModel):
    name: Optional[str] = None
    party_id: Optional[int] = None
```

---

### `SAdventurePut`
Схема параметров для PUT-запроса.

Поля:
- `name` (str): новое название **Adventure**.
- `party_id` (int): новый идентификатор команды, к которой будет принадлежать **Adventure**.

```python
class SAdventurePut(BaseModel):
    name: str
    party_id: int
```

---

### `SAdventurePatch`
Схема параметров для PATCH-запроса.

Поля:
- `name` (Optional[str]): новое название **Adventure** (необязательное).
- `party_id` (Optional[int]): новый идентификатор команды (необязательное).

```python
class SAdventurePatch(BaseModel):
    name: Optional[str] = None
    party_id: Optional[int] = None
```

---

### `SAdventureResult`
Схема ответа на PUT-запрос и PATCH-запрос.

Поля:
- `ok` (bool): результат операции. По умолчанию всегда `True`.

```python
class SAdventureResult(BaseModel):
    ok: bool = True
```

---

### `SAdventureCreateResult`
Схема ответа на CREATE-запрос.

Поля:
- `ok` (bool): результат операции. По умолчанию всегда `True`.
- `id` (int): уникальный идентификатор нового **Adventure**.

```python
class SAdventureCreateResult(BaseModel):
    ok: bool = True
    id: int
```