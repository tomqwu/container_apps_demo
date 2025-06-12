FROM python:3.11-slim

WORKDIR /app

COPY app.py .

# install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
    apt-get install -y gcc g++ unixodbc-dev

EXPOSE 4000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "4000"]
