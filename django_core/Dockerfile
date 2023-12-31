# получаем image для нашего питона
FROM python:3.11.4-bookworm

# устанавливаем рабочую директорию
WORKDIR /django_core

# задаём переменные окружения, чтобы
# предотвратить ряд событий, а именно:
# создания .pyc файлов и использования
# питоном буффера для stdout/stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update
# ставим зависимости
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
# копируем проект
COPY . .
# Устанавливаем docker in docker...
RUN bash start_worker.sh
