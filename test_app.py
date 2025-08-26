import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Malik Muhammad Babar Khan" in response.data
    assert b"AI Engineer at Systems Limited" in response.data

def test_projects_route(client):
    response = client.get('/projects')
    assert response.status_code == 200
    assert b"Image Classifier" in response.data
    assert b"House Price Prediction" in response.data
    assert b"Attan Dance Classification" in response.data

def test_about_route(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b"Malik Muhammad Babar Khan" in response.data
    assert b"AI engineer" in response.data
