# `board/`

Модуль `board/` отвечает за управление досками (`Board`). Он включает в себя:
- Определение ORM-модели `BoardOrm`.
- Реализацию функций работы с базой данных в `repository.py`.
- API-маршруты в `router.py`.

## Структура модуля

```
board/
│── models.py       # ORM-модель для таблицы `board`
│── repository.py   # Функции для работы с базой данных
│── router.py       # API-маршруты для работы с досками
│── __init__.py     # Инициализация модуля
```

## `models.py`

Определяет ORM-модель `BoardOrm`, представляющую таблицу `board` в базе данных.

```python
class BoardOrm(Model):
    __tablename__ = "board"

    id: Mapped[int_pk]               # первичный ключ
    name: Mapped[str]                # название доски
    adventure_id: Mapped[int]        # идентификатор приключения
    party_id: Mapped[int]            # идентификатор команды
    created_at: Mapped[created_at]   # автоматически устанавливаемая дата создания
    updated_at: Mapped[updated_at]   # автоматически устанавливаемая дата последнего обновления
```

## `repository.py`

Определяет функции для работы с таблицей `board`. Использует схемы для взаимодействия с базой данных и шаблонный `Repository` для работы с БД.

### **Функции:**

#### **`get_filters(data: SBoardSearch) -> List[bool]`**
Формирует фильтры для поиска записей по `name`, `adventure_id` и `party_id`.

---

#### **`create(data: SBoardCreate) -> int`**
Создаёт новую доску и возвращает её `id`.

---

#### **`get_one(board_id: int) -> Optional[SBoardGet]`**
Возвращает доску по `board_id`.

---

#### **`get(data: SBoardSearch) -> list[SBoardGet]`**
Возвращает список досок по фильтрам.

---

#### **`delete_one(board_id: int)`**
Удаляет доску по `board_id`.

---

#### **`delete(data: SBoardSearch)`**
Удаляет доски по фильтрам.

---

#### **`put(board_id: int, data: SBoardPut)`**
Полностью обновляет запись в БД.

---

#### **`patch(board_id: int, data: SBoardPatch)`**
Частично обновляет запись в БД (например, меняет только `name`).

## `router.py`

Определяет API-маршруты для работы с досками.

### **Маршруты:**
#### **`POST /boards`** — создание доски.
#### **`GET /boards/{board_id}`** — получение доски по `id`.
#### **`GET /boards`** — получение досок по фильтрам.
#### **`DELETE /boards/{board_id}`** — удаление доски по `id`.
#### **`DELETE /boards`** — удаление досок по фильтрам.
#### **`PUT /boards/{board_id}`** — полное обновление доски.
#### **`PATCH /boards/{board_id}`** — частичное обновление доски.

