from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "application": "CloudBackup Manager",
        "version": "0.1.0",
        "status": "running",
    }


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_docs_endpoint():
    response = client.get("/docs")

    assert response.status_code == 200
