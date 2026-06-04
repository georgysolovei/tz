FROM python:3.12-alpine

# Set environment variables to optimize Python output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN adduser -D appuser && chown -R appuser:appuser /app

USER appuser

COPY . .

EXPOSE 8080

CMD ["python", "app.py"]

