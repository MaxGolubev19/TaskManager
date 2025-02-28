# TaskManager

Микросервисный таск-менеджер с фэнтези-тематикой, разработанный на FastAPI. В проекте реализован микросервисный бэкенд, а так же планируется реализация фронтенда и поддержка WebSockets и командной работы.

## 🛠 Технологии
- **Python 3.x**
- **FastAPI**, **FastAPI-users**, **FastAPI-cache**
- **SQLALchemy**
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

## ⚙️ Развёртывание
1. Склонируйте репозиторий:
   ```sh
   git clone https://github.com/MaxGolubev19/TaskManager.git
   cd TaskQuest
   ```
3. Создайте `.env`-файл с необходимыми переменными окружения в корне проекта.
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
4. Запустите сервисы:
   ```sh
   docker-compose up --build
   ```

## 📚 API-документация
После запуска можно открыть Swagger-документацию по адресу:
```
http://localhost:8080/docs
```

## 📜 Лицензия
Проект лицензирован под [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](http://creativecommons.org/licenses/by-nc-nd/4.0/).
