from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_notify_sales():
    response = client.post("/notify", json={"topic": "sales", "description": "Need help with sales"})
    assert response.status_code == 200
    assert "Notification sent" in response.json()["message"]

def test_notify_pricing():
    response = client.post("/notify", json={"topic": "pricing", "description": "Pricing question"})
    assert response.status_code == 200

def test_notify_invalid_topic():
    response = client.post("/notify", json={"topic": "support", "description": "Unknown topic"})
    assert response.status_code == 422  # schema validation
