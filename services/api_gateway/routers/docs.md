# API Gateway: `routers/`

**Модуль `routers/`** отвечает за маршрутизацию запросов между клиентами и микросервисами. Он включает в себя:
- Общее управление маршрутами в `router.py`.
- Подмодули для каждого микросервиса (`adventure_service`, `board_service`, `party_service`, `quest_service`, `user_service`).
- Проверку API-ключей и управление доступом.

## Структура модуля `routers/`

```
routers/
│── router.py            # Основной роутер API Gateway
│── adventure_service/   # Роутеры для сервиса Adventure
│── board_service/       # Роутеры для сервиса Board
│── party_service/       # Роутеры для сервиса Party
│── quest_service/       # Роутеры для сервиса Quest
│── user_service/        # Роутеры для сервиса User
│── __init__.py          # Инициализация модуля
```

---

## `router.py`

Основной файл маршрутизации API Gateway, который управляет взаимодействием между клиентами и микросервисами.

### **Функции:**

- **`create(url: str, data: InputType, output_type: Type[OutputType])`** — отправляет `POST`-запрос для создания ресурса.
- **`get_one(url: str, output_type: Type[OutputType])`** — отправляет `GET`-запрос для получения одного ресурса.
- **`get(url: str, data: InputType, output_type: Type[OutputType])`** — отправляет `GET`-запрос с параметрами.
- **`delete_one(url: str, output_type: Type[OutputType])`** — отправляет `DELETE`-запрос для удаления одного ресурса.
- **`delete(url: str, data: InputType, output_type: Type[OutputType])`** — отправляет `DELETE`-запрос с параметрами.
- **`put(url: str, data: InputType, output_type: Type[OutputType])`** — отправляет `PUT`-запрос для полного обновления ресурса.
- **`patch(url: str, data: InputType, output_type: Type[OutputType])`** — отправляет `PATCH`-запрос для частичного обновления ресурса.

Пример использования `create()`:
```python
async def create_adventure(data: SAdventureCreate) -> SAdventureCreateResult:
    return await create(
        url=f"{os.getenv('ADVENTURE_SERVICE_URL')}/adventures",
        data=data,
        output_type=SAdventureCreateResult,
    )
```

---

## `adventure_service/`

Роутеры для сервиса **Adventure**.

Пример маршрута:
```python
@router.get("/adventures/{adventure_id}")
async def get_adventure(adventure_id: int):
    return await get_one(
        url=f"{os.getenv('ADVENTURE_SERVICE_URL')}/adventures/{adventure_id}",
        output_type=SAdventureGet,
    )
```

---

## `board_service/`

Роутеры для сервиса **Board**.

Пример маршрута:
```python
@router.post("/boards")
async def create_board(data: SBoardCreate) -> SBoardCreateResult:
    return await create(
        url=f"{os.getenv('BOARD_SERVICE_URL')}/boards",
        data=data,
        output_type=SBoardCreateResult,
    )
```

---

## `party_service/`

Роутеры для сервиса **Party**.

Пример маршрута:
```python
@router.get("/parties/{party_id}")
async def get_party(party_id: int):
    return await get_one(
        url=f"{os.getenv('PARTY_SERVICE_URL')}/parties/{party_id}",
        output_type=SPartyGet,
    )
```

---

## `quest_service/`

Роутеры для сервиса **Quest**.

Пример маршрута:
```python
@router.patch("/quests/{quest_id}")
async def update_quest(quest_id: int, data: SQuestPatch):
    return await patch(
        url=f"{os.getenv('QUEST_SERVICE_URL')}/quests/{quest_id}",
        data=data,
        output_type=SQuestResult,
    )
```

---

## `user_service/`

Роутеры для сервиса **User**.

Пример маршрута:
```python
@router.delete("/{user_id}")
async def delete_user(user_id: int) -> SUserResult:
    return await delete_one(
        url=f"""{os.getenv("USER_SERVICE_URL")}/users/{user_id}""",
        output_type=SUserResult,
    )
```