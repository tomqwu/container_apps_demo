import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_create_order():
    response = client.post("/orders", json={"order_id": 123, "item": "Widget", "quantity": 2})
    assert response.status_code == 200
    assert response.json() == {
        "message": "Order created successfully",
        "data": {"order_id": 123, "item": "Widget", "quantity": 2}
    }

def test_example_endpoint():
    response = client.get("/api/v1/example")
    assert response.status_code == 200
    assert response.json() == {"message": "success"}
