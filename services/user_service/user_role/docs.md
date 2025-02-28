# `user_role/`

Модуль `user_role/` отвечает за управление привязкой пользователей к ролям. Он включает в себя:
- Определение ORM-модели `UserRoleOrm`.
- Реализацию функций работы с базой данных в `repository.py`.
- API-маршруты в `router.py`.

## Структура модуля

```
user_role/
│── models.py       # ORM-модель для таблицы `user_role`
│── repository.py   # Функции для работы с базой данных
│── router.py       # API-маршруты для работы с привязками пользователей к ролям
│── __init__.py     # Инициализация модуля
```

## `models.py`

Определяет ORM-модель `UserRoleOrm`, представляющую таблицу `user_role` в базе данных.

```python
class UserRoleOrm(Model):
    __tablename__ = "user-role"

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))  # идентификатор пользователя
    space_id: Mapped[int]  # идентификатор пространства (например, команды или организации)
    space_type: Mapped[RoleSpaceType]  # тип пространства (команда, организация и т. д.)
    role_id: Mapped[int] = mapped_column(ForeignKey("role.id", ondelete="CASCADE"))  # идентификатор роли
    created_at: Mapped[created_at]  # автоматически устанавливаемая дата создания
    updated_at: Mapped[updated_at]  # автоматически устанавливаемая дата последнего обновления

    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'space_id', 'space_type'),  # Составной первичный ключ
    )
```

## `repository.py`

Определяет функции для работы с таблицей `user_role`. Использует схемы для взаимодействия с базой данных и шаблонный `Repository` для работы с БД.

### **Функции:**

#### **`get_filters(data: SUserRoleSearch) -> List[bool]`**
Формирует фильтры для поиска записей по `user_id`, `space_id`, `space_type` и `role_id`.

---

#### **`create(data: SUserRoleCreate)`**
Создаёт новую привязку пользователя к роли.

---

#### **`get(data: SUserRoleSearch) -> list[SUserRoleGet]`**
Возвращает список привязок пользователей к ролям по фильтрам.

---

#### **`delete(data: SUserRoleSearch)`**
Удаляет привязки пользователей к ролям по фильтрам.

---

#### **`put(data: SUserRolePut)`**
Полностью обновляет запись в БД.

---

#### **`patch(data: SUserRolePatch)`**
Частично обновляет запись в БД (например, изменяет `role_id`).

## `router.py`

Определяет API-маршруты для работы с привязками пользователей к ролям.

### **Маршруты:**
#### **`POST /user-role`** — создание привязки пользователя к роли.
#### **`GET /user-role`** — получение списка привязок пользователей к ролям.
#### **`DELETE /user-role`** — удаление привязок пользователей к ролям по фильтрам.
#### **`PUT /user-role`** — полное обновление привязки.
#### **`PATCH /user-role`** — частичное обновление привязки.
