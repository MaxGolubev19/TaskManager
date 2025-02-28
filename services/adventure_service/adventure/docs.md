# `adventures/`

Модуль `adventures/` отвечает за управление подкомандами (`Adventures`). Он включает в себя:
- Определение ORM-модели `AdventureOrm`.
- Реализацию функций работы с базой данных в `repository.py`.
- API-маршруты в `router.py`.

## Структура модуля

```
adventures/
│── models.py       # ORM-модель для таблицы `adventures`
│── repository.py   # Функции для работы с базой данных
│── router.py       # API-маршруты для работы с подкомандами
│── __init__.py     # Инициализация модуля
```

## `models.py`

Определяет ORM-модель `AdventureOrm`, представляющую таблицу `adventures` в базе данных.

```python
class AdventureOrm(Model):
    __tablename__ = "adventures"

    id: Mapped[int_pk]               # первичный ключ
    name: Mapped[str]                # название подкоманды
    party_id: Mapped[int]            # идентификатор основной команды (Party)
    created_at: Mapped[created_at]   # автоматически устанавливаемая дата создания
    updated_at: Mapped[updated_at]   # автоматически устанавливаемая дата последнего обновления
```

## `repository.py`

Определяет функции для работы с таблицей `adventures`. Использует схемы для взаимодействия с базой данных и шаблонный `Repository` для взаимодействия с базой данных из модуля `common`.

### **Функции:**

#### **`get_filters(data: SAdventureSearch) -> List[bool]`**
Формирует фильтры для поиска записей по критериям `SAdventureSearch`. В текущей реализации поддерживается фильтр по `name` и `party_id`.

---

#### **`create(data: SAdventureCreate) -> int`**
Создаёт новую запись и возвращает её `id`.

---

#### **`get_one(adventure_id: int) -> Optional[SAdventureGet]`**
Возвращает запись по `adventure_id`.

---

#### **`get(data: SAdventureSearch) -> list[SAdventureGet]`**
Возвращает список записей по фильтрам.

---

#### **`delete_one(adventure_id: int)`**
Удаляет запись по `adventure_id`.

---

#### **`delete(cls, data: SAdventureSearch)`**
Удаляет записи по фильтрам.

---

#### **`put(adventure_id: int, data: SAdventurePut)`**
Полностью обновляет запись в БД.

---

#### **`patch(adventure_id: int, data: SAdventurePatch)`**
Частично обновляет запись в БД (например, меняет только `name`).

## `router.py`

Определяет API-маршруты для работы с подкомандами. Использует схемы для взаимодействия с базой данных из модуля `common`.

### **Маршруты:**
#### **`POST /adventures`** — создание подкоманды.
#### **`GET /adventures/{adventure_id}`** — получение подкоманды по `id`.
#### **`GET /adventures`** — получение подкоманд по фильтрам.
#### **`DELETE /adventures/{adventure_id}`** — удаление подкоманды по `id`.
#### **`DELETE /adventures`** — удаление подкоманд по фильтрам.
#### **`PUT /adventures/{adventure_id}`** — полное обновление подкоманды.
#### **`PATCH /adventures/{adventure_id}`** — частичное обновление подкоманды.

