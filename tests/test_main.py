from app.main import app


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_hello():
    client = app.test_client()
    response = client.get("/hello?name=Naina")
    assert response.status_code == 200
    assert response.json["message"] == "Hello, Naina!"
