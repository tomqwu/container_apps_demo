# Container Apps Demo

This project demonstrates a simple containerized application where a frontend service calls a backend service. The application uses FastAPI and Docker Compose for orchestration. Optionally, Dapr can be used for service-to-service communication.

## Prerequisites

- Python 3.9 or higher
- Docker and Docker Compose
- Dapr CLI (optional, for Dapr testing)

## Setup Instructions

### 1. Install Dependencies

Install Python dependencies:

```bash
pip3 install -r backend/requirements.txt
pip3 install -r frontend/requirements.txt
```

### 2. Run the Application with Docker Compose

Start the services using Docker Compose:

```bash
docker-compose up --build
```

Access the frontend at `http://localhost:3000/call-backend`.

### 3. Run Unit Tests

#### Backend Tests

Run unit tests for the backend:

```bash
pytest backend/test_backend.py
```

#### Frontend Tests

Run unit tests for the frontend:

```bash
pytest frontend/test_frontend.py
```

### 4. Test Dapr Integration (Optional)

#### Start Dapr Sidecar

Start the Dapr sidecar for the backend service:

```bash
dapr run --app-id backend --app-port 4000 -- uvicorn app:app --host 0.0.0.0 --port 4000
```

#### Test Dapr Communication

Use `curl` to test Dapr communication:

```bash
curl -X GET http://localhost:3500/v1.0/invoke/backend/method/api/v1/example
```

### 5. Debugging

#### View Logs

View logs for Docker Compose services:

```bash
docker-compose logs
```

View logs for Dapr:

```bash
dapr logs --app-id backend
```

#### Check Dapr Status

Verify Dapr status:

```bash
dapr status
```

### 6. Cleanup

Stop all services:

```bash
docker-compose down
```

Stop Dapr:

```bash
dapr stop --app-id backend
```

## Notes

- Ensure the `BACKEND_URL` environment variable is correctly set in the frontend service.
- If using Dapr, ensure the Dapr CLI is installed and initialized (`dapr init`).