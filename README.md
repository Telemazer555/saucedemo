# Backend API Testing Framework

Этот проект предназначен для автоматизированного тестирования backend API с использованием  **Requests**, и **Pytest**.
Он предоставляет структурированный подход к написанию тестов, валидации схем ответов.

## 🛠️ Стек технологий

- [Requests](https://pypi.org/project/requests/) – выполнение HTTP-запросов
- [Python](https://www.python.org/) – основной язык разработки фреймворка и тестов
- [Pydantic](https://docs.pydantic.dev/latest/) – валидация схем JSON

## 📁 Структура проекта

```
.
├── tests/                
│   ├── conftest/         # Конфигурации для pytest (Хелперы для URL-ов)
│   ├── test_api.py       # Сами Тесты 
├── src/
│   ├── core/             # Сессии, клиент, базовая логика 
│   ├── scenarios/        # Сценарии для тестов 
│   ├── data_models/      # Схемы для валидации ответов 
│   └── utils/            # Вспомогательные функции 
├── pyproject.toml        # Конфиг зависимостей для uv 
├── .env                  # Переменные окружения 
```

## 📦 Установка

С помощю команды **_cd /Users/_**... переходим в нужную директорию и клонируем Репозиторий

```bash

git clone <this-repo>
```

Пакетный менеджер

```bash

pip install uv
``` 

Создаём вируальное окружение

``` bash

uv venv .venv 
``` 

Ставим нужную версию python

``` bash

uv venv --python 3.10

``` 

Выбираем необходимое виртуальное окружение

``` bash

source .venv/bin/activate
``` 

Установка всех зависимостей

``` bash

uv sync
```

## ⚙️ Конфигурация

### Переменные окружения

Создайте `.env` файл в корне проекта:

```

BASE_URL = https://api.example.com
API_KEY = your-api-key
JSON_BODY = your-json_body
```

> Используйте [dotenv](https://pypi.org/project/python-dotenv/) для загрузки переменных.

## 🚀 Запуск тестов

Запуск всех тестов:

```bash

pytest -s -v
```

Запуск конкретного теста:

```bash

pytest tests/test_api.py::TestBookingScenarios::test_get_and_verify

```

## 🔗 Зависимости

```toml
[project]
name = "api-restful-booker"
version = "0.1.0"
description = "Add your description here"
requires-python = ">=3.13"
dependencies = [
    "faker>=37.8.0",
    "pytest>=8.4.2",
    "requests>=2.32.5",
    "pydantic>=2.11.9",
    "python-dotenv>=1.0.1",
]

```

## ✨ Возможности

- HTTP-клиент с общей сессией
- Валидация ответов через Pydantic
- Поддержка сценариев (scenarios)
- Повторно используемые фикстуры
- Гибкая конфигурация через `.env`

## 💡 Рекомендации

[//]: # (- Старайтесь выносить `UUID` и данные в fixtures или конфиги.)

- Используйте `BookingDates` для валидации каждого запроса.