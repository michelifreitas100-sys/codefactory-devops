"""
Testes automatizados da API.
São executados automaticamente pelo pipeline de Integração Contínua
a cada push/pull request (ver .github/workflows/ci.yml).
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

import pytest
from main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["status"] == "online"


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_create_task(client):
    response = client.post("/tasks", json={"title": "Configurar pipeline de CI"})
    assert response.status_code == 201
    assert response.json["title"] == "Configurar pipeline de CI"
    assert response.json["done"] is False


def test_create_task_without_title(client):
    response = client.post("/tasks", json={})
    assert response.status_code == 400


def test_list_tasks(client):
    client.post("/tasks", json={"title": "Tarefa de teste"})
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_create_task_with_whitespace_title(client):
    response = client.post("/tasks", json={"title": "   "})
    assert response.status_code == 400


def test_create_task_title_too_long(client):
    response = client.post("/tasks", json={"title": "a" * 121})
    assert response.status_code == 400