from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_and_get_item():
    created = client.post("/api/v1/items", json={"name": "Keyboard", "description": "Mechanical keyboard"})
    assert created.status_code == 201
    item_id = created.json()["id"]
    fetched = client.get(f"/api/v1/items/{item_id}")
    assert fetched.status_code == 200
    assert fetched.json()["name"] == "Keyboard"

def test_missing_item():
    response = client.get("/api/v1/items/999999")
    assert response.status_code == 404
