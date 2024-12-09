# tests/routes/test_todos.py

def test_get_todos(client):
    """Test GET /api/todos/ endpoint."""
    response = client.get('/api/todos/')  # Added trailing slash to match route
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_create_todo(client):
    """Test POST /api/todos/ endpoint."""
    response = client.post('/api/todos/', json={"title": "New Todo"})  # Added trailing slash
    assert response.status_code == 201
    assert response.json["message"] == "Todo created"
    assert "id" in response.json["todo"]
    assert response.json["todo"]["title"] == "New Todo"
