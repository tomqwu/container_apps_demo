FROM python:3.11-slim

WORKDIR /app

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source files
COPY . .

EXPOSE 4000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "4000"]
