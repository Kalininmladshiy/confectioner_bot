# Сервис confectioner_bot
Чатбот, в котором можно купить готовый торт, а можно заказать кастомный.

## Запуск:

### 1. Копируем содержимое проекта себе в рабочую директорию
```
git clone <метод копирования>
```

### 2. Разворачиваем внутри скопированного проекта виртуальное окружение:
```
python -m venv <название виртуального окружения>
```

### 3. Устанавливаем библиотеки:
```
pip install -r requirements.txt
```

### 4. Для хранения переменных окружения создаем файл .env:
```
touch .env
```
Генерируем секретный ключ DJANGO в интерактивном режиме python:
* `python`
* `import django`
* `from django.core.management.utils import get_random_secret_key`
* `print(get_random_secret_key())`
    
Копируем строку в `.env` файл: `DJANGO_KEY='ваш ключ'` 

Для тестирования бота добавляем токен в `.env` файл: `TG_BOT_TOKEN='токен вашего бота'`

### 5. Запускаем модуль бота:
```
python manage.py bot
```
На комманду `/start` должен отреагировать, значит проект развернулся, все ок
![изображение](https://user-images.githubusercontent.com/106922768/203391673-972ae093-0d8f-43fd-a3e0-f74ae38d2915.png)


 
