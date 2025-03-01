# TaskManager

Микросервисный таск-менеджер с фэнтези-тематикой, разработанный на FastAPI. В проекте реализован микросервисный бэкенд, а также планируется реализация фронтенда и поддержка WebSockets и командной работы.

## 🛠 Технологии
- **Python 3.x**
- **FastAPI**, **FastAPI-users**, **FastAPI-cache**
- **SQLAlchemy**
- **PostgreSQL**
- **Redis**
- **Docker**, **Docker Compose**

## ⚔️ Основные сущности
- **Party** — команда (например, проект).
- **Adventure** — подкоманда (например, бэкенд или фронтенд).
- **Board** — доска с задачами.
- **Quest** — задача.
- **User** — пользователь.

## 🏰 Архитектура
Проект реализован как набор микросервисов:
- `api-gateway` — шлюз API.
- `user-service` — сервис пользователей и ролей.
- `quest-service` — сервис задач.
- `board-service` — сервис досок и колонок.
- `adventure-service` — сервис подкоманд.
- `party-service` — сервис команд.
- `common` — общие схемы и утилиты.

Каждый сервис включает в себя:
- `service/` — бизнес-логика сервиса.
- `module/` — набор модулей для работы с сущностями.
- `database.py` — управление базой данных.
- `main.py` — точка входа.
- `requirements.txt` — зависимости.
- `Dockerfile` — конфигурация контейнера.

## 🔗 Взаимодействие
Фронтенд будет взаимодействовать с бэкендом исключительно через **API Gateway**, который управляет маршрутизацией и проверкой доступа. Вся бизнес-логика реализована в микросервисах, а API Gateway обеспечивает единую точку входа.

**Принцип работы:**
1. Клиент отправляет запрос в API Gateway.
2. API Gateway проверяет API-ключ и находит нужный сервис.
3. Запрос перенаправляется в соответствующий микросервис.
4. Микросервис обрабатывает запрос и возвращает данные через API Gateway.

## ⚙️ Развёртывание
1. Склонируйте репозиторий:
   ```sh
   git clone https://github.com/MaxGolubev19/TaskManager.git
   cd TaskManager
   ```
2. Создайте `.env`-файл с необходимыми переменными окружения в корне проекта.
   ```
   DB_PORT=db_port
   DB_USER=db_user
   DB_PASS=db_pass
   DB_NAME=db_name
   
   REDIS_NAME=redis_name
   REDIS_PORT=redis_port
   
   API_KEY=api_key
   INSIDE_API_KEY=inside_api_key
   SECRET=secret
   PUBLIC_KEY=public_key
   PRIVATE_KEY=private_key
   ```
3. Запустите сервисы:
   ```sh
   docker-compose up --build
   ```

## 📚 API-документация
После запуска можно открыть Swagger-документацию по адресу:
```
http://localhost:8080/docs
```

Каждый микросервис содержит собственную документацию, доступную в соответствующих директориях.

### 📄 OpenAPI JSON
Swagger-документация также доступна в файле `openapi.json`, который находится в `docs/`. Можно открыть его без запуска сервиса с помощью [Swagger Editor](https://editor-next.swagger.io/):
1. Перейдите на [https://editor-next.swagger.io/](https://editor-next.swagger.io/).
2. Нажмите `File` → `Import File`.
3. Выберите `docs/openapi.json`.

## 📜 Лицензия
Проект лицензирован под [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](http://creativecommons.org/licenses/by-nc-nd/4.0/).
