from pytest import fixture
from faker import Faker

fake = Faker()


@fixture
def mock_requests_get(mocker):
    return mocker.patch("requests.get", autospec=True)
