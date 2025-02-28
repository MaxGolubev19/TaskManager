# `party/`

Модуль `party/` отвечает за управление командами (`Party`). Он включает в себя:
- Определение ORM-модели `PartyOrm`.
- Реализацию функций работы с базой данных в `repository.py`.
- API-маршруты в `router.py`.

## Структура модуля

```
party/
│── models.py       # ORM-модель для таблицы `party`
│── repository.py   # Функции для работы с базой данных
│── router.py       # API-маршруты для работы с командами
│── __init__.py     # Инициализация модуля
```

## `models.py`

Определяет ORM-модель `PartyOrm`, представляющую таблицу `party` в базе данных.

```python
class PartyOrm(Model):
    __tablename__ = "party"

    id: Mapped[int_pk]               # первичный ключ
    name: Mapped[str]                # название команды
    created_at: Mapped[created_at]   # автоматически устанавливаемая дата создания
    updated_at: Mapped[updated_at]   # автоматически устанавливаемая дата последнего обновления
```

## `repository.py`

Определяет функции для работы с таблицей `party`. Использует схемы для взаимодействия с базой данных и шаблонный `Repository` для взаимодействия с базой данных из модуля `common`.

### **Функции:**

#### **`get_filters(data: SPartySearch) -> List[bool]`**
Формирует фильтры для поиска записей по критериям `SPartySearch`. В текущей реализации поддерживается фильтр по `name`.

---

#### **`create(data: SPartyCreate) -> int`**
Создаёт новую запись и возвращает её `id`.

---

#### **`get_one(party_id: int) -> Optional[SPartyGet]`**
Возвращает запись по `party_id`.

---

#### **`get(data: SPartySearch) -> list[SPartyGet]`**
Возвращает список записей по фильтрам.

---

#### **`delete_one(party_id: int)`**
Удаляет запись по `party_id`.

---

#### **`delete(cls, data: SPartySearch)`**
Удаляет записи по фильтрам.

---

#### **`put(party_id: int, data: SPartyPut)`**
Полностью обновляет запись в БД.

---

#### **`patch(party_id: int, data: SPartyPatch)`**
Частично обновляет запись в БД (например, меняет только `name`).


## `router.py`

Определяет API-маршруты для работы с командами. Использует схемы для взаимодействия с базой данных из модуля `common`.

### **Маршруты:**
#### **`POST /parties`** — создание команды.
#### **`GET /parties/{party_id}`** — получение команды по `id`.
#### **`GET /parties`** — получение команды по фильтрам.
#### **`DELETE /parties/{party_id}`** — удаление команды по `id`.
#### **`DELETE /parties`** — удаление команды по фильтрам.
#### **`PUT /parties/{party_id}`** — полное обновление команды.
#### **`PATCH /parties/{party_id}`** — частичное обновление команды.