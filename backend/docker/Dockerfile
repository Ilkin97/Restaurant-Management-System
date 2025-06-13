# backend/docker/Dockerfile

FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Sistem bağımlılıkları
RUN apt-get update \
  && apt-get install -y build-essential libpq-dev netcat gcc \
  && pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
