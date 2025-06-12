import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_create_order():
    payload = {"order_id": 123, "item": "Widget", "quantity": 2}
    response = client.post("/orders", json=payload)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}, Response: {response.json()}"
    assert response.json() == {
        "message": "Order created successfully",
        "data": payload
    }, f"Unexpected response: {response.json()}"

def test_example_endpoint():
    response = client.get("/api/v1/example")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}, Response: {response.json()}"
    assert response.json() == {"message": "success"}, f"Unexpected response: {response.json()}"
