# `dependency/`

Модуль `dependency/` отвечает за управление зависимостями (`Dependency`) между задачами (`Quest`). Он включает в себя:
- Определение ORM-модели `DependencyOrm`.
- Реализацию функций работы с базой данных в `repository.py`.
- API-маршруты в `router.py`.

## Структура модуля

```
dependency/
│── models.py       # ORM-модель для таблицы `dependency`
│── repository.py   # Функции для работы с базой данных
│── router.py       # API-маршруты для работы с зависимостями
│── __init__.py     # Инициализация модуля
```

## `models.py`

Определяет ORM-модель `DependencyOrm`, представляющую таблицу `dependency` в базе данных.

```python
class DependencyOrm(Model):
    __tablename__ = "dependency"

    parent_id: Mapped[int]  # Идентификатор родительской задачи
    child_id: Mapped[int]   # Идентификатор зависимой (дочерней) задачи
    created_at: Mapped[created_at]  # Дата создания зависимости
    updated_at: Mapped[updated_at]  # Дата последнего обновления зависимости

    __table_args__ = (
        PrimaryKeyConstraint('parent_id', 'child_id'),  # Составной первичный ключ
    )
```

## `repository.py`

Определяет функции для работы с таблицей `dependency`. Использует схемы для взаимодействия с базой данных и шаблонный `Repository` для работы с БД.

### **Функции:**

#### **`get_filters(data: SDependencySearch) -> List[bool]`**
Формирует фильтры для поиска зависимостей по `parent_id` и `child_id`.

---

#### **`create(data: SDependencyCreate)`**
Создаёт новую зависимость между задачами.

---

#### **`get(data: SDependencySearch) -> list[SDependencyGet]`**
Возвращает список зависимостей по фильтрам.

---

#### **`delete(data: SDependencySearch)`**
Удаляет зависимости по фильтрам.

## `router.py`

Определяет API-маршруты для работы с зависимостями.

### **Маршруты:**
#### **`POST /dependencies`** — создание зависимости между задачами.
#### **`GET /dependencies`** — получение списка зависимостей.
#### **`DELETE /dependencies`** — удаление зависимостей по фильтрам.

