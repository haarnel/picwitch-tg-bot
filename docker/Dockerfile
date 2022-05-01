FROM python:3.9.6-slim AS python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=no

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app

CMD ["python", "run.py"]