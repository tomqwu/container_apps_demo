import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_create_order():
    response = client.get("/create-order")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Order created successfully",
        "data": {"order_id": 123, "item": "Widget", "quantity": 2}
    }

def test_check_backend():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Backend check successful"}
