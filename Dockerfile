FROM python:3.10

WORKDIR /djangoProject

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN apk update \
    && apk add --virtual build-essential gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2

RUN poetry install

COPY . .

RUN adduser -D myuser
USER myuser

CMD gunicorn djangoProject.wsgi:application --bind 0.0.0.0:$PORT