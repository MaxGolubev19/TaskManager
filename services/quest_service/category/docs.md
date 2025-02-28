# `category/`

Модуль `category/` отвечает за управление категориями (`Category`). Он включает в себя:
- Определение ORM-модели `CategoryOrm`.
- Реализацию функций работы с базой данных в `repository.py`.
- API-маршруты в `router.py`.

## Структура модуля

```
category/
│── models.py       # ORM-модель для таблицы `category`
│── repository.py   # Функции для работы с базой данных
│── router.py       # API-маршруты для работы с категориями
│── __init__.py     # Инициализация модуля
```

## `models.py`

Определяет ORM-модель `CategoryOrm`, представляющую таблицу `category` в базе данных.

```python
class CategoryOrm(Model):
    __tablename__ = "category"

    id: Mapped[int_pk]                      # первичный ключ
    name: Mapped[str]                       # название категории
    space_id: Mapped[Optional[int]]         # идентификатор пространства (Board, Adventure, Party)
    space_type: Mapped[CategorySpaceType]   # тип пространства (Board, Adventure, Quest)
    created_at: Mapped[created_at]          # автоматически устанавливаемая дата создания
    updated_at: Mapped[updated_at]          # автоматически устанавливаемая дата последнего обновления
```

## `repository.py`

Определяет функции для работы с таблицей `category`. Использует схемы для взаимодействия с базой данных и шаблонный `Repository` для работы с БД.

### **Функции:**

#### **`get_filters(data: SCategorySearch) -> List[bool]`**
Формирует фильтры для поиска записей по `name`, `space_id` и `space_type`.

---

#### **`create(data: SCategoryCreate) -> int`**
Создаёт новую категорию и возвращает её `id`.

---

#### **`create_many(data: list[SCategoryCreate]) -> list[int]`**
Создаёт сразу несколько категорий и возвращает их `id`.

---

#### **`get_one(category_id: int) -> Optional[SCategoryGet]`**
Возвращает категорию по `category_id`.

---

#### **`get(data: SCategorySearch) -> list[SCategoryGet]`**
Возвращает список категорий по фильтрам.

---

#### **`delete_one(category_id: int)`**
Удаляет категорию по `category_id`.

---

#### **`delete(data: SCategorySearch)`**
Удаляет категории по фильтрам.

---

#### **`put(category_id: int, data: SCategoryPut)`**
Полностью обновляет запись в БД.

---

#### **`patch(category_id: int, data: SCategoryPatch)`**
Частично обновляет запись в БД (например, меняет только `name` или `space_type`).

## `router.py`

Определяет API-маршруты для работы с категориями.

### **Маршруты:**
#### **`POST /categories`** — создание категории.
#### **`GET /categories/{category_id}`** — получение категории по `id`.
#### **`GET /categories`** — получение категорий по фильтрам.
#### **`DELETE /categories/{category_id}`** — удаление категории по `id`.
#### **`DELETE /categories`** — удаление категорий по фильтрам.
#### **`PUT /categories/{category_id}`** — полное обновление категории.
#### **`PATCH /categories/{category_id}`** — частичное обновление категории.

