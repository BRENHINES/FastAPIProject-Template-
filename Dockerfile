FROM ubuntu:latest
FROM python:3.12-slim
LABEL authors="Sereina Yopa"

ENTRYPOINT ["top", "-b"]

ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml README.md /app/
RUN pip install --no-cache-dir -U pip && pip install --no-cache-dir -e .

COPY . /app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]