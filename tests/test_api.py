from fastapi.testclient import TestClient
from main import app
from core.config import settings

client = TestClient(app)

def test_manifest_upload_requires_auth():
    response = client.post("/api/v1/manifests/process", files={"file": ("test.txt", b"dummy content")})
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}

def test_manifest_upload_success():
    headers = {"x-api-key": settings.EXTRACTOR_API_KEY}
    response = client.post(
        "/api/v1/manifests/process", 
        headers=headers,
        files={"file": ("manifest.txt", b"FEDEX 123456 arriving tomorrow.")}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "success"
