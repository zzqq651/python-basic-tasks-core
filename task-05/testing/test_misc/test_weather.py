from http import HTTPStatus
from unittest import mock

import pytest

from testing.conftest import fake
from misc.weather import get_weather, API_BASE_URL, FetchWeatherError


class TestGetWeather:
    @mock.patch("requests.get", autospec=True)
    def test_get_weather(self, requests_get):
        new_dict = fake.pydict(nb_elements=3)
        obj = mock.MagicMock()
        obj.status_code = HTTPStatus.OK
        obj.json.return_value = new_dict
        requests_get.return_value = obj
        city = fake.city()

        assert get_weather(city) == new_dict
        requests_get.assert_called_with(API_BASE_URL + city)

    def test_get_weather_raises(self, mock_requests_get):
        obj = mock.MagicMock()
        obj.status_code = HTTPStatus.BAD_GATEWAY
        obj.text = "Error"
        mock_requests_get.return_value = obj
        city = fake.city()
        with pytest.raises(FetchWeatherError, match=obj.text):
            get_weather(city)

