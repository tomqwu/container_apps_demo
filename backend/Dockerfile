FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN apt-get update && \
    apt-get install -y gcc g++ unixodbc-dev && \
    pip install fastapi uvicorn httpx pyodbc

EXPOSE 4000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "4000"]
