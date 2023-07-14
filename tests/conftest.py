import pytest
from http_client import HTTPClient


@pytest.fixture()
def new_user(request):
    def new_client(user_data):
        client = HTTPClient(user_data)

        def delete_user():
            client.delete_user()

        request.addfinalizer(delete_user)
        return client

    return new_client
