FROM python:3.10-alpine

RUN mkdir /Manga

WORKDIR /Manga/

# Установка зависимостей для psycopg2
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /Manga

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
