import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app import app  # Replace 'app' with the actual name of your FastAPI app instance
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = TestClient(app)

@patch("httpx.AsyncClient.get")
def test_check_backend(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: {"message": "success"}
    response = client.get("/")
    logger.info(f"Response from /: {response.json()}")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}, Response: {response.json()}"
    assert response.json() == {"message": "success"}, f"Unexpected response: {response.json()}"

@patch("httpx.AsyncClient.post")
def test_create_order(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json = lambda: {
        "message": "Order created successfully",
        "data": {
            "order_id": 123,
            "item": "Widget",
            "quantity": 2
        }
    }
    response = client.get("/create-order")
    logger.info(f"Response from /create-order: {response.json()}")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}, Response: {response.json()}"
    assert response.json() == {
        "message": "Order created successfully",
        "data": {
            "order_id": 123,
            "item": "Widget",
            "quantity": 2
        }
    }, f"Unexpected response: {response.json()}"
logger.info("Frontend tests completed")
