# `quest/`

Модуль `quest/` отвечает за управление задачами (`Quest`). Он включает в себя:
- Определение ORM-модели `QuestOrm`.
- Реализацию функций работы с базой данных в `repository.py`.
- API-маршруты в `router.py`.

## Структура модуля

```
quest/
│── models.py       # ORM-модель для таблицы `quest`
│── repository.py   # Функции для работы с базой данных
│── router.py       # API-маршруты для работы с задачами
│── __init__.py     # Инициализация модуля
```

## `models.py`

Определяет ORM-модель `QuestOrm`, представляющую таблицу `quest` в базе данных.

```python
class QuestOrm(Model):
    __tablename__ = "quest"

    id: Mapped[int_pk]                     # первичный ключ
    name: Mapped[str]                      # название задачи
    description: Mapped[Optional[str]]     # описание задачи
    category_id: Mapped[int]               # категория задачи
    column_id: Mapped[int]                 # идентификатор колонки
    board_id: Mapped[int]                  # идентификатор доски
    adventure_id: Mapped[int]              # идентификатор приключения
    party_id: Mapped[int]                  # идентификатор команды
    user_id: Mapped[Optional[int]]         # ответственный пользователь
    deadline: Mapped[Optional[datetime]]   # дедлайн
    created_at: Mapped[created_at]         # автоматически устанавливаемая дата создания
    updated_at: Mapped[updated_at]         # автоматически устанавливаемая дата последнего обновления
```

## `repository.py`

Определяет функции для работы с таблицей `quest`. Использует схемы для взаимодействия с базой данных и шаблонный `Repository` для работы с БД.

### **Функции:**

#### **`get_filters(data: SQuestSearch) -> List[bool]`**
Формирует фильтры для поиска записей по `name`, `description`, `category_id`, `column_id`, `board_id`, `adventure_id`, `party_id`, `user_id` и `deadline`.

---

#### **`create(data: SQuestCreate) -> int`**
Создаёт новую задачу и возвращает её `id`.

---

#### **`get_one(quest_id: int) -> Optional[SQuestGet]`**
Возвращает задачу по `quest_id`.

---

#### **`get(data: SQuestSearch) -> list[SQuestGet]`**
Возвращает список задач по фильтрам.

---

#### **`delete_one(quest_id: int)`**
Удаляет задачу по `quest_id`.

---

#### **`delete(data: SQuestSearch)`**
Удаляет задачи по фильтрам.

---

#### **`put(quest_id: int, data: SQuestPut)`**
Полностью обновляет запись в БД.

---

#### **`patch(quest_id: int, data: SQuestPatch)`**
Частично обновляет запись в БД (например, меняет только `name` или `description`).

## `router.py`

Определяет API-маршруты для работы с задачами.

### **Маршруты:**
#### **`POST /quests`** — создание задачи.
#### **`GET /quests/{quest_id}`** — получение задачи по `id`.
#### **`GET /quests`** — получение задач по фильтрам.
#### **`DELETE /quests/{quest_id}`** — удаление задачи по `id`.
#### **`DELETE /quests`** — удаление задач по фильтрам.
#### **`PUT /quests/{quest_id}`** — полное обновление задачи.
#### **`PATCH /quests/{quest_id}`** — частичное обновление задачи.

