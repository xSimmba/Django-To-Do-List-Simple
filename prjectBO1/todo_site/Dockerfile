FROM python:3.12-slim

RUN pip install poetry

WORKDIR /app

COPY . .

RUN poetry install 

EXPOSE 8000

CMD poetry run python manage.py runserver 0.0.0.0:8000