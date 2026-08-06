import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page_loads(client):
    """Test that the voting app returns a 200 OK status."""
    response = client.get('/')
    assert response.status_code == 200