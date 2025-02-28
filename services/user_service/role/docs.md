# `role/`

Модуль `role/` отвечает за управление ролями (`Role`). Он включает в себя:
- Определение ORM-модели `RoleOrm`.
- Реализацию функций работы с базой данных в `repository.py`.
- API-маршруты в `router.py`.

## Структура модуля

```
role/
│── models.py       # ORM-модель для таблицы `role`
│── repository.py   # Функции для работы с базой данных
│── router.py       # API-маршруты для работы с ролями
│── __init__.py     # Инициализация модуля
```

## `models.py`

Определяет ORM-модель `RoleOrm`, представляющую таблицу `role` в базе данных.

```python
class RoleOrm(Model):
    __tablename__ = "role"

    id: Mapped[int_pk]               # первичный ключ
    name: Mapped[str]                # название роли
    space_id: Mapped[Optional[int]]  # идентификатор пространства (например, группы или организации)
    space_type: Mapped[RoleSpaceType]  # тип пространства (например, группа, организация)
    created_at: Mapped[created_at]   # автоматически устанавливаемая дата создания
    updated_at: Mapped[updated_at]   # автоматически устанавливаемая дата последнего обновления
```

## `repository.py`

Определяет функции для работы с таблицей `role`. Использует схемы для взаимодействия с базой данных и шаблонный `Repository` для работы с БД.

### **Функции:**

#### **`get_filters(data: SRoleSearch) -> List[bool]`**
Формирует фильтры для поиска записей по `name`, `space_id` и `space_type`.

---

#### **`create(data: SRoleCreate) -> int`**
Создаёт новую роль и возвращает её `id`.

---

#### **`get_one(role_id: int) -> Optional[SRoleGet]`**
Возвращает роль по `role_id`.

---

#### **`get(data: SRoleSearch) -> list[SRoleGet]`**
Возвращает список ролей по фильтрам.

---

#### **`delete_one(role_id: int)`**
Удаляет роль по `role_id`.

---

#### **`delete(data: SRoleSearch)`**
Удаляет роли по фильтрам.

---

#### **`put(role_id: int, data: SRolePut)`**
Полностью обновляет запись в БД.

---

#### **`patch(role_id: int, data: SRolePatch)`**
Частично обновляет запись в БД (например, меняет только `name`).

## `router.py`

Определяет API-маршруты для работы с ролями.

### **Маршруты:**
#### **`POST /roles`** — создание роли.
#### **`GET /roles/{role_id}`** — получение роли по `id`.
#### **`GET /roles`** — получение списка ролей по фильтрам.
#### **`DELETE /roles/{role_id}`** — удаление роли по `id`.
#### **`DELETE /roles`** — удаление ролей по фильтрам.
#### **`PUT /roles/{role_id}`** — полное обновление роли.
#### **`PATCH /roles/{role_id}`** — частичное обновление роли.
