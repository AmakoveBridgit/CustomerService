FROM python:3.11-slim

# my working directory
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=orderservice.settings

# runserver
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

