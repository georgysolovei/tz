FROM python:3.12-slim

# Set environment variables to optimize Python output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN useradd --create-home appuser && chown -R appuser:appuser /app

USER appuser

COPY . .

EXPOSE 8080

CMD ["python", "app.py"]

