# Проект api приложения Yatube в рамках обучения в Яндекс Практикум
## Назначение
Проект предназначен для испольщования в качестве API для реализации соц сети yatube
Документация api : http://localhost:8000/redoc/ 

## Установка

1. Склонировать репозиторий 
```
git clone https://github.com/navydragon/api_final_yatube
```

2. Создать виртуальное окружение:
```
python -m venv venv
```

3. Установить зависимости:
```
pip install -r requirements.txt
```

4. Создать и применить миграции:
```
python manage.py makemigrations
python manage.py migrate
```

5. Запустить сервер: 
```
python manage.py runserver
```

## Примеры
Авторизация происходит по JWT-токену

1. Получить JWT-токен \
```
POST http://127.0.0.1:8000//api/v1/jwt/create/` 
```
JSON-параметры запроса
```
{
  "username": "string",
  "password": "string"
}
```
Ответ сервера
```
{
"refresh": "string",
"access": "string"
}
```
2. Посмотреть список постов
```
GET http://127.0.0.1:8000/api/v1/posts/
```

Ответ сервера:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
