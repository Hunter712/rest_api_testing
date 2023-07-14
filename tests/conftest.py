import pytest
from http_client import HTTPClient


@pytest.fixture()
def user():
    new_user = HTTPClient()
    new_user.create_user()

    yield new_user

    new_user.delete_user()




