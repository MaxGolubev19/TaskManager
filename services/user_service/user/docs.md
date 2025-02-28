# `user/`

Модуль `user/` отвечает за управление пользователями (`User`). Он включает в себя:
- Определение ORM-модели `UserOrm`.
- Реализацию функций работы с базой данных в `repository.py`.
- Аутентификацию и управление пользователями в `auth.py`.
- API-маршруты в `router.py` и `auth_router.py`.

## Структура модуля

```
user/
│── auth.py         # Логика аутентификации
│── auth_router.py  # API-маршруты аутентификации
│── models.py       # ORM-модель для таблицы `user`
│── repository.py   # Функции для работы с базой данных
│── router.py       # API-маршруты для работы с пользователями
│── __init__.py     # Инициализация модуля
```

## `models.py`

Определяет ORM-модель `UserOrm`, представляющую таблицу `user` в базе данных.

```python
class UserOrm(SQLAlchemyBaseUserTable[int], Model):
    __tablename__ = "user"

    id: Mapped[int_pk]               # первичный ключ
    name: Mapped[str]                # имя пользователя
    role_id: Mapped[int]             # идентификатор роли пользователя
    email: Mapped[str]                # email пользователя
    hashed_password: Mapped[str]      # хешированный пароль
    created_at: Mapped[created_at]   # автоматически устанавливаемая дата создания
    updated_at: Mapped[updated_at]   # автоматически устанавливаемая дата последнего обновления
```

## `auth.py`

Определяет логику аутентификации, используя `FastAPI Users`.

### **Компоненты:**
- **`UserManager`** — управляет событиями регистрации, сброса пароля и подтверждения email.
- **`get_user_manager()`** — предоставляет `UserManager` в качестве зависимости.
- **JWT-аутентификация** через `fastapi_users.authentication.JWTStrategy`.

## `repository.py`

Определяет функции для работы с таблицей `user`. Использует схемы для взаимодействия с базой данных и шаблонный `Repository` для работы с БД.

### **Функции:**

#### **`get_filters(data: SUserSearch) -> List[bool]`**
Формирует фильтры для поиска записей по `name`, `email` и `role_id`.

---

#### **`get_one(user_id: int) -> Optional[SUserGet]`**
Возвращает пользователя по `user_id`.

---

#### **`get(data: SUserSearch) -> list[SUserGet]`**
Возвращает список пользователей по фильтрам.

---

#### **`delete_one(user_id: int)`**
Удаляет пользователя по `user_id`.

---

#### **`delete(data: SUserSearch)`**
Удаляет пользователей по фильтрам.

---

#### **`put(user_id: int, data: SUserPut)`**
Полностью обновляет запись в БД.

---

#### **`patch(user_id: int, data: SUserPatch)`**
Частично обновляет запись в БД (например, меняет только `name`).

## `auth_router.py`

Определяет API-маршруты для аутентификации.

### **Маршруты:**
#### **`POST /auth/jwt/login`** — вход в систему с email и паролем.
#### **`POST /auth/register`** — регистрация нового пользователя.
#### **`POST /auth/verify`** — подтверждение email.
#### **`POST /auth/reset-password`** — сброс пароля.

## `router.py`

Определяет API-маршруты для работы с пользователями.

### **Маршруты:**
#### **`GET /users/{user_id}`** — получение пользователя по `id`.
#### **`GET /users`** — получение списка пользователей по фильтрам.
#### **`DELETE /users/{user_id}`** — удаление пользователя по `id`.
#### **`DELETE /users`** — удаление пользователей по фильтрам.
#### **`PUT /users/{user_id}`** — полное обновление пользователя.
#### **`PATCH /users/{user_id}`** — частичное обновление пользователя.

