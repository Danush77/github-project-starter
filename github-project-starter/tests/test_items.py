def test_get_items(client):
    response = client.get("/api/v1/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_item(client):
    payload = {
        "title": "Test Product",
        "description": "A product for unit testing",
        "price": 49.99
    }
    response = client.post("/api/v1/items", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert "id" in data
