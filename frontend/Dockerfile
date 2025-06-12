FROM python:3.11-slim

WORKDIR /app

# install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy source
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
