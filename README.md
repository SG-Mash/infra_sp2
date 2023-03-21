<h1 align="center">API_YaMDB</h1>

## Описание проекта
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.<br/>
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).<br/>
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.<br/>

## Используемые технологии:<br/>
- Django - 2.2.16
- Django Rest Framework - 3.12.4
- Python 3.7
- Docker
- Gunicorn
- Nginx
## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:LuckyPoRus/infra_sp2.git
```
Переход в директорию с проектом:
```
cd api_yamdb
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
Активировать виртуальное окружение:
```
source venv/scripts/activate
```
Оновление PIP:
```
python -m pip install --upgrade pip
```
Установка зависимостей используемых в проекте:
```
pip install -r requirements.txt
```
Переходим в папку с файлом docker-compose.yaml:
```
cd ..
cd infra
```
Шаблон наполнения env-файла:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=< имя базы данных>
POSTGRES_USER=<логин для подключения к базе данных>
POSTGRES_PASSWORD=<пароль для подключения к БД (установите свой)>
DB_HOST=< название сервиса (контейнера)>
DB_PORT=5432 # порт для подключения к БД
```
Поднимаем контейнеры (infra_db_1, infra_web_1, infra_nginx_1):
```
docker-compose up -d --build
```
Выполняем миграции:
```
docker-compose exec web python manage.py makemigrations
```
```
docker-compose exec web python manage.py migrate
```
Создаем суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```
Собираем статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```
Создаем дамп базы данных:
```
docker-compose exec web python manage.py dumpdata > fixtures.json
```
Останавливаем контейнеры:
```
docker-compose down -v
```

## Регистрация нового пользователя
- POST
```
http://127.0.0.1:8000/api/v1/auth/signup/
{
  "email": "user@example.com",
  "username": "string"
}
```
## Примеры запросов:
**Получение JWT-токена:**
- POST
```
http://127.0.0.1:8000/api/v1/auth/create/
```
**Получить список всех публикаций:**
- GET
```
http://127.0.0.1:8000/api/v1/posts/
{
  "username": "string",
  "confirmation_code": "string"
}
```
**Добавление нового произведения(администратор):**
- POST
```
http://127.0.0.1:8000/api/v1/titles/
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```
**Получение списка всех отзывов:**
- GET
```
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
```
**Получение всех комментариев к отзыву:**
- GET
```
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
**Подробная документация к проекту доступная по адресу:**
```
http://127.0.0.1:8000/redoc/
```
