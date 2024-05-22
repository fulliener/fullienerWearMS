FROM python:3.11-alpine

WORKDIR /app

RUN pip install --upgrade pip
RUN apk add gcc musl-dev libffi-dev
RUN pip install poetry && poetry config virtualenvs.create false

RUN mkdir static

COPY ./poetry.lock ./pyproject.toml /app/

RUN poetry install --no-interaction

COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]