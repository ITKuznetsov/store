# Store
Интернет магазин с лендингом товаров, личным кабинетом пользователей, возможностью создания и оформления заказов, RESTful API для взаимодейтсвия с корзиной и товарами.
## Технологии
* Python
* Django
* Django REST Framework
* PostgreSQL
* Redis
* Celery
## ERD
![ER-диаграмма](https://github.com/mainelink/store/assets/161898140/fe7636d9-3756-4833-86f1-8f39f22e0ea5)
## Локальный запуск (Linux)
1. Создайте и активируйте виртуальное окружение
   ```bash
   python -m venv ../venv
   source ../venv/bin/activate
   ```

2. Установите зависимости
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. Создайте файл .env и установите необходимые ключи для settings.py (PostgreSQL, Yandex SMTP)
   ```bash
   touch .env
   ```

4. Создайте и выполните миграции
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Запустите Redis
   ```bash
   redis-server
   ```

6. Запустите Celery
   ```bash
   celery -A store worker --loglevel=INFO
   ```

7. Запустите локальный сервер
   ```bash
   python manage.py runserver
   ```


