# Handbook API(Тестовое задание)

## Описание

Handbook API - это REST API приложения для справочника Организаций, Зданий, Деятельности.

## Функциональность

API реализует следующие возможности:

- **Получение списка организаций по фильтрам** (GET `/organizations?`)
- **Получение организации по наименованию** (GET `/organizations/search`)
- **Получение информации об организации по ID** (GET `/organizations/{id}`)

### Бизнес-логика
    • список всех организаций находящихся в конкретном здании
    • список всех организаций, которые относятся к указанному виду деятельности
    • список организаций, которые находятся в заданном радиусе/прямоугольной области относительно указанной точки на карте. список зданий
    • вывод информации об организации по её идентификатору
    • искать организации по виду деятельности. Например, поиск по виду деятельности «Еда», которая находится на первом уровне дерева, и чтобы нашлись все организации, которые относятся к видам деятельности, лежащим внутри. Т.е. в результатах поиска должны отобразиться организации с видом деятельности Еда, Мясная продукция, Молочная продукция.
    • поиск организации по названию

## Структура проекта

```plaintext
├── alembic.ini
├── docker-compose.yaml
├── Dockerfile
├── justfile
├── postgres
│   └── data
├── pyproject.toml
├── ruff.toml
├── src
│   ├── api
│   │   ├── api_key.py
│   │   ├── controllers
│   │   │   ├── health_check.py
│   │   │   ├── __init__.py
│   │   │   └── organization.py
│   │   ├── dtos.py
│   │   ├── __init__.py
│   │   └── middlewares
│   │       ├── __init__.py
│   │       └── logging.py
│   ├── config.py
│   ├── features
│   │   ├── __init__.py
│   │   └── organization
│   │       ├── application
│   │       │   ├── dtos.py
│   │       │   ├── __init__.py
│   │       │   ├── interactors
│   │       │   │   ├── get_organization_by_id.py
│   │       │   │   ├── get_organization_by_title.py
│   │       │   │   ├── get_organizations.py
│   │       │   │   └── __init__.py
│   │       │   └── mapper.py
│   │       ├── domain
│   │       │   ├── entities
│   │       │   │   ├── activity.py
│   │       │   │   ├── __init__.py
│   │       │   │   └── organization.py
│   │       │   ├── __init__.py
│   │       │   ├── repository.py
│   │       │   └── value_objects.py
│   │       ├── exceptions.py
│   │       └── __init__.py
│   ├── infrastructure
│   │   ├── __init__.py
│   │   ├── mapper.py
│   │   ├── migrations
│   │   │   ├── env.py
│   │   │   ├── __init__.py
│   │   │   ├── script.py.mako
│   │   │   └── versions
│   │   │       ├── 2025_06_22_1100-d2ae914e2ab4_.py
│   │   │       ├── 2025_06_22_1113-2bc0514ee4a8_.py
│   │   │       ├── 2025_06_22_1115-479b7a1810bd_.py
│   │   │       ├── 2025_06_23_0854-5168e085b862_.py
│   │   │       └── __init__.py
│   │   ├── models
│   │   │   ├── activity.py
│   │   │   ├── base.py
│   │   │   ├── building.py
│   │   │   ├── __init__.py
│   │   │   ├── mixins.py
│   │   │   └── organization.py
│   │   └── repository.py
│   ├── __init__.py
│   ├── main.py
│   ├── providers
│   │   ├── adapters.py
│   │   ├── __init__.py
│   │   └── interactor_providers.py
│   ├── tests
│   │   └── __init__.py
│   └── utils
│       ├── __init__.py
│       ├── log
│       │   ├── configuration.py
│       │   ├── __init__.py
│       │   └── setup.py
│       └── seed_data.py
└── uv.lock
```

## Установка и запуск

### Локальный запуск
1. В файле`.env` для локального запуска установите параметр DB_HOST=localhost.
2. Убедитесь, что все зависимости установлены через [uv]:
   ```bash
   uv sync
   ```
3. Установите переменную окружения `PYTHONPATH` для корректной работы импортов:
   ```bash
   export PYTHONPATH=$(pwd)
   ```
4. Запустите приложение:
   ```bash
   uv run python src/main.py
   ```
5. Для запуска через `uvicorn`:
   ```bash
   uv run uvicorn src.main:create_app --reload
   ```

### Запуск с использованием Docker
1. В файле `.env`. Убедитесь, что переменная `DB_HOST` установлена на `postgres`.
2. Запустите контейнеры:
   ```bash
   docker-compose up --build
   ```

## Зависимости

Основные зависимости:
- **FastAPI**: ^0.115.13
- **SQLAlchemy**: 2.0.41
- **asyncpg**: ^0.30.0
- **Alembic**: ^1.16.2
- **Dishka**: ^1.6.0
- **Uvicorn**: ^0.34.3

Инструменты для разработки:
- **mypy**: ^1.16.1



## Документация API

После запуска приложения документация будет доступна по адресу:
- Swagger UI: [http://localhost:8000/](http://localhost:8000/)

## Дополнительно

### Миграции базы данных
- Генерация миграций:
  ```bash
  uv run alembic revision --autogenerate -m "Описание изменений"
  ```
- Применение миграций:
  ```bash
  uv run alembic upgrade head
