# Файл `utils.py`
Этот модуль содержит общий репозиторий `Repository` для работы с базой данных через SQLAlchemy.

## Класс `Repository`
Класс-репозиторий, предоставляющий методы для работы с БД. Выделен в отдельный модуль для избежания дублирования кода, т.к. используется во всех микросервисах.

### Методы

#### `create` — создание записи
  ```python
  async def create(cls, new_session, orm, data) -> int
  ```
  Создаёт новую запись в таблице и возвращает её ID.

---

#### `get` — получение записей по фильтрам
  ```python
  async def get(cls, new_session, orm, filters, output_type) -> list[OutputType]
  ```
  Выполняет `SELECT` с фильтрацией и возвращает объекты Pydantic.

---

#### `delete` — удаление записей
  ```python
  async def delete(cls, new_session, orm, filters)
  ```
  Выполняет `DELETE` по заданным фильтрам.

---

#### `put` — полное обновление записей
  ```python
  async def put(cls, new_session, orm, filters, values)
  ```
  Обновляет все значения в записях, удовлетворяющих фильтру.

---

#### `patch` — частичное обновление записей
  ```python
  async def patch(cls, new_session, orm, filters, values)
  ```
  Обновляет только переданные значения в записях, удовлетворяющих фильтру.