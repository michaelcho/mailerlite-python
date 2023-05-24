import pytest
from mailerlite.api_client import ApiClient


class TestApiClient:
    def test_config_api_key_is_set_properly(self):
        """Tests if API key is properly set in configuration"""

        config = {"api_key": "1234567890"}
        client = ApiClient(config)

        assert client.api_key == config["api_key"]
        assert "Authorization" in client.headers
        assert client.headers["Authorization"] == "Bearer " + config["api_key"]

    def test_config_api_version_is_set_properly(self):
        """Tets if API version is properly set in configuration"""

        config = {"api_version": "2038-01-19"}
        client = ApiClient(config)

        assert client.api_version == config["api_version"]
        assert "X-Version" in client.headers
        assert client.headers["X-Version"] == config["api_version"]

        config = {}
        client = ApiClient(config)

        assert "X-Version" not in client.headers

    def test_config_default_headers_are_set_properly(self):
        """Tests if default headers are properly set in configuration"""

        config = {}
        client = ApiClient(config)

        assert type(client.headers) == dict
        assert "Content-Type" in client.headers
        assert "Accept" in client.headers
        assert "User-Agent" in client.headers

        assert client.headers["Content-Type"] == "application/json"
        assert client.headers["Accept"] == "application/json"
        assert client.headers["User-Agent"] == "MailerLite-Python-SDK-Client"

    def test_it_will_return_error_if_request_method_is_not_supported(self):
        """Tests if error is going to be returned in case of incorrect http method"""

        client = ApiClient({})
        with pytest.raises(ValueError):
            client.request("PPOST", "some-url")
