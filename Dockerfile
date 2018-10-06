FROM python:3.5

RUN mkdir /app
WORKDIR /app

ADD requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

ENV DJANGO_SECRET_KEY="SUPERSECRETKEY"
ENV DJANGO_DB_PATH="/app/db.sqlite3"
ENV DJANGO_LOG_FILE="/app/django.log"
ENV DJANGO_LOG_LEVEL="INFO"
ENV DJANGO_STATIC_ROOT="/app/static/"
ENV DJANGO_MEDIA_ROOT="/app/media/"

ADD . .

WORKDIR /app/src
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
