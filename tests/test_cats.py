import pytest

from api_client.cats_api import CatsClient

def test_hent_cats(client: CatsClient):
    response = client.get_one_fact()

    assert response is not None
    assert len(response["data"]) == 1