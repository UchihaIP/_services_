# Проект _notification_services_
## Описание проекта 

Простой сервис управления рассылками API администрирования и получения статистики.


## Выполнены дополнительные задания:

1. Сделать так, чтобы по адресу /docs/ открывалась страница со Swagger UI и в нём отображалось описание разработанного API. Пример: https://petstore.swagger.io
2. Реализовать администраторский Web UI для управления рассылками и получения статистики по отправленным сообщениям
3. Удаленный сервис может быть недоступен, долго отвечать на запросы или выдавать некорректные ответы. Необходимо организовать обработку ошибок и откладывание запросов при неуспехе для последующей повторной отправки. Задержки в работе внешнего сервиса никак не должны оказывать влияние на работу сервиса рассылок.
4. Реализовать дополнительную бизнес-логику: добавить в сущность "рассылка" поле "временной интервал", в котором можно задать промежуток времени, в котором клиентам можно отправлять сообщения с учётом их локального времени. Не отправлять клиенту сообщение, если его локальное время не входит в указанный интервал.
5. обеспечить подробное логирование на всех этапах обработки запросов, чтобы при эксплуатации была возможность найти в логах всю информацию по
• id рассылки - все логи по конкретной рассылке (и запросы на api и внешние запросы на отправку конкретных сообщений)
• id сообщения - по конкретному сообщению (все запросы и ответы от внешнего сервиса, вся обработка конкретного сообщения)
• id клиента - любые операции, которые связаны с конкретным клиентом (добавление/редактирование/отправка сообщения/…)

## Как запустить проект локально:
Клонировать репозиторий и перейти в него в командной строке:

```bash
  git clone https://github.com/UchihaIP/_services_.git
  cd _services_
```
Создайте файл .env в корне проекта
```
SECRET_KEY=<SECRET_KEY из settings.py>
DB_NAME=<Имя БД>
DB_PASSWORD=<Пароль БД>
DB_USER=<Имя пользователя Postgres (default=postgres)>
DB_HOST=<Адрес хоста>
DB_PORT=<Порт БД>
URL=url внешнего api
TOKEN=token для внешнего api
```

Установить пакетный менеджер poetry:
```bash
  pip install poetry
```
Установить виртуальное окружение и зависимости из файла toml :
```bash
  poetry install
```
Выполнить миграции:
```bash
  python3 manage.py migrate
```
Создать супер пользователя для админ панели:
```bash
  python manage.py createsuperuser
```
Запустить проект:
```bash
  python3 manage.py runserver
```
Запустить Celery:
```bash
celery -A _services_ worker -l info
```

## API Reference

#### Создание нового клиента

```http
  POST /api/v1/clients/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `phone_number` | `string` | **Required** Client's phone number|
| `mobile_code` | `string` | **Required** Mobile operator code|
| `tag` | `string` | Search filtering tag |
| `timezone` | `string` | Client's timezone (Can selected) |


#### Получение информации о рассылках

```http
  GET /api/v1/mailing/info/
```

| Response |
| Information data about all mailing |


#### API Docs (Swagger)
```http
  http://localhost/swagger/
```


## Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![PostgreSQL](https://a11ybadges.com/badge?logo=postgresql)
![Celery](https://a11ybadges.com/badge?logo=celery)
![Docker](https://a11ybadges.com/badge?logo=docker)
![Swagger](https://a11ybadges.com/badge?logo=swagger)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)

## Author

Рифат Хасанов
- [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/UchihaIP)
- [![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/lawlietLL)
