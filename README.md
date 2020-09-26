# Тестовое задание (Точка)

## Описание

Для внутренних нужд отдела разработки требуется подготовить
решение, которое позволяет :
* хранить информацию о состоянии счета абонента
* производить операции с счетом абонента
* по запросу выдавать текущие параметры счета абонента

## Инструменты

* Python3.8
* Django + Django REST Framework
* PostgreSQL 13
* RabbitMQ
* Celery
* Docker + docker-compose

## Инструкция по запуску

#### 1. Установка Docker + docker-compose

> [Инструкция](https://docs.docker.com/engine/install/)

#### 2.a Разработка и отладка

> Заполнить файл `.env` данными для подключения к БД и к RabbitMQ.

```shell
$ docker-compose up --build
```

#### 2.b Запуск в production

> Заполнить файл `.env.prod` данными для подключения к БД и к RabbitMQ.

```shell
$ ./start_service.sh
```

## Использование

Сервис отвечает на запросы с заголовком `Accept: application/json` в виде `json`, при запросе с другим заголовком сервис отвечает в `html`.

#### Структура `json` ответа:

```json
{
    "status": "<http_status>",
    "result": "<bool:operation_status>",
    "addition": {},
    "description": {}
}
```

## Список методов

### GET `/api/v1/ping/`

Проверка работоспособности сервиса.

#### Пример ответа:

```json
{  
    "status": 200,
    "result": true,
    "addition": {
        "status": "pong"
    },
    "description": {}
}
```

### GET `/api/v1/accounts/`

Список всех счетов абонентов.

#### Пример ответа:

```json
{
    "status": 200,
    "result": true,
    "addition": [
        {
            "uuid": "26c940a1-7228-4ea2-a3bc-e6460b172040",
            "fio": "Петров Иван Сергеевич",
            "balance": 1700,
            "hold": 300,
            "status": true
        },
    ...
    ],
    "description": {}
}
```

### GET `/api/v1/status/<uuid>`

Вывод информации по выбранному счету.

#### Пример ответа:

Запрос на `/api/v1/status/867f0924-a917-4711-939b-90b179a96392/`

```json
{
    "status": 200,
    "result": true,
    "addition": {
        "balance": 1000000,
        "status": false
    },
    "description": {}
}
```

### POST `/api/v1/add/<uuid>`

Пополнение баланса абонента.

#### Тело запроса:

```json
{
    "balance": 100
}
```

#### Пример ответа:
Запрос на `/api/v1/add/26c940a1-7228-4ea2-a3bc-e6460b172040/`

```json
{
    "status": 200,
    "result": true,
    "addition": {
        "balance": 1800
    },
    "description": {}
}
```

### POST `/api/v1/subtract/<uuid>`

Уменьшение баланса абонента.

#### Тело запроса:

```json
{
    "hold": 100
}
```

#### Пример ответа:
Запрос на `/api/v1/subtract/867f0924-a917-4711-939b-90b179a96392/`

```json
{
    "status": 200,
    "result": true,
    "addition": {
        "hold": 101
    },
    "description": {}
}
```

При уменьшении баланса пользователя сумма вычета добавляется к значению `холда`. После обращения к контроллеру в `celery` создается задача, которая обнуляет `холд` абонента.