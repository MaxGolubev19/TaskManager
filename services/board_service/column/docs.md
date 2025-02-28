# `column/`

Модуль `column/` отвечает за управление колонками (`Column`). Он включает в себя:
- Определение ORM-модели `ColumnOrm`.
- Реализацию функций работы с базой данных в `repository.py`.
- API-маршруты в `router.py`.

## Структура модуля

```
column/
│── models.py       # ORM-модель для таблицы `column`
│── repository.py   # Функции для работы с базой данных
│── router.py       # API-маршруты для работы с колонками
│── __init__.py     # Инициализация модуля
```

## `models.py`

Определяет ORM-модель `ColumnOrm`, представляющую таблицу `column` в базе данных.

```python
class ColumnOrm(Model):
    __tablename__ = "column"

    id: Mapped[int_pk]                    # первичный ключ
    space_id: Mapped[int]                 # идентификатор пространства (Party, Adventure или Board)
    space_type: Mapped[ColumnSpaceType]   # тип пространства (Party, Adventure или Board)
    order: Mapped[int]                    # положение колонки в таблице
    name: Mapped[str]                     # название колонки
    created_at: Mapped[created_at]        # автоматически устанавливаемая дата создания
    updated_at: Mapped[updated_at]        # автоматически устанавливаемая дата последнего обновления
```

## `repository.py`

Определяет функции для работы с таблицей `column`. Использует схемы для взаимодействия с базой данных и шаблонный `Repository` для работы с БД.

### **Функции:**

#### **`get_filters(data: SColumnSearch) -> List[bool]`**
Формирует фильтры для поиска записей по `space_id`, `space_type`, `order` и `name`.

---

#### **`create(data: SColumnCreate) -> int`**
Создаёт новую колонку и возвращает её `id`.

---

#### **`create_many(data: list[SColumnCreate]) -> list[int]`**
Создаёт сразу несколько колонок и возвращает их `id`.

---

#### **`create_for_board(adventure_id: int, board_id: int)`**
Создаёт колонки для новой доски (`board`), копируя их из приключения (`adventure`).

---

#### **`get_one(column_id: int) -> Optional[SColumnGet]`**
Возвращает колонку по `column_id`.

---

#### **`get(data: SColumnSearch) -> list[SColumnGet]`**
Возвращает список колонок по фильтрам.

---

#### **`delete_one(column_id: int)`**
Удаляет колонку по `column_id`.

---

#### **`delete(data: SColumnSearch)`**
Удаляет колонки по фильтрам.

---

#### **`delete_for_board(board_id: int)`**
Удаляет все колонки, относящиеся к `board_id`.

---

#### **`delete_for_boards(board_ids: list[int])`**
Удаляет все колонки, относящиеся к списку `board_ids`.

---

#### **`put(column_id: int, data: SColumnPut)`**
Полностью обновляет запись в БД.

---

#### **`patch(column_id: int, data: SColumnPatch)`**
Частично обновляет запись в БД (например, меняет только `name`).

## `router.py`

Определяет API-маршруты для работы с колонками.

### **Маршруты:**
#### **`POST /columns`** — создание колонки.
#### **`GET /columns/{column_id}`** — получение колонки по `id`.
#### **`GET /columns`** — получение колонок по фильтрам.
#### **`DELETE /columns/{column_id}`** — удаление колонки по `id`.
#### **`DELETE /columns`** — удаление колонок по фильтрам.
#### **`PUT /columns/{column_id}`** — полное обновление колонки.
#### **`PATCH /columns/{column_id}`** — частичное обновление колонки.

