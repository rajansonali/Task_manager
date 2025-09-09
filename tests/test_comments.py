import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from run import app
import pytest

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_add_comment(client):
    response = client.post("/api/tasks/2/comments", json={"content": "Test", "author": "Tester"})
    assert response.status_code == 201
    assert response.get_json()["comment"]["content"] == "Test"

def test_get_comments(client):
    client.post("/api/tasks/2/comments", json={"content": "Test2", "author": "Tester"})
    response = client.get("/api/tasks/2/comments")
    assert response.status_code == 200
    assert len(response.get_json()) > 0

def test_update_comment(client):
    client.post("/api/tasks/2/comments", json={"content": "Old", "author": "Tester"})
    response = client.put("/api/tasks/2/comments/1", json={"content": "Updated"})
    assert response.status_code == 200
    assert response.get_json()["content"] == "Updated"

def test_delete_comment(client):
    client.post("/api/tasks/2/comments", json={"content": "ToDelete", "author": "Tester"})
    response = client.delete("/api/tasks/2/comments/1")
    assert response.status_code == 200
