import pytest
import requests
from mailerlite.api_client import ApiClient
from pytest_mock import mocker


class TestApiClient:
    def test_config_api_key_is_set_properly(self):
        """Tests if API key is properly set in configuration"""

        config = {"api_key": "1234567890"}
        client = ApiClient(config)

        assert client.api_key == config["api_key"]
        assert "Authorization" in client.default_headers
        assert client.default_headers["Authorization"] == "Bearer " + config["api_key"]

    def test_config_api_version_is_set_properly(self):
        """Tets if API version is properly set in configuration"""

        config = {"api_version": "2038-01-19"}
        client = ApiClient(config)

        assert client.api_version == config["api_version"]
        assert "X-Version" in client.default_headers
        assert client.default_headers["X-Version"] == config["api_version"]

        config = {}
        client = ApiClient(config)

        assert "X-Version" not in client.default_headers

    def test_config_default_headers_are_set_properly(self):
        """Tests if default headers are properly set in configuration"""

        config = {}
        client = ApiClient(config)

        assert type(client.default_headers) == dict
        assert "Content-Type" in client.default_headers
        assert "Accept" in client.default_headers
        assert "User-Agent" in client.default_headers

        assert client.default_headers["Content-Type"] == "application/json"
        assert client.default_headers["Accept"] == "application/json"
        assert client.default_headers["User-Agent"] == "MailerLite-Python-SDK-Client"

    def test_it_will_return_error_if_request_method_is_not_supported(self):
        """Tests if error is going to be returned in case of incorrect http method"""

        client = ApiClient({})
        with pytest.raises(ValueError):
            response = client.request("PPOST", "some-url")
