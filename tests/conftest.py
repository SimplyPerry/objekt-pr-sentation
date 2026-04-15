import pytest
from api_client.cats_api import CatsClient

@pytest.fixture
def client():
    base_url = "https://dogapi.dog/api/v2"

    return CatsClient(base_url)


@pytest.fixture
def cats_client(client):
    return client