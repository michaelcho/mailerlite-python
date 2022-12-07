import pytest
from mailerlite.api_client import ApiClient

class TestApiClient:
    def test_api_key(self):
        """Tests if API key is properly set in API Client"""

        config = {
            'api_key': '1234567890'
        }

        client = ApiClient(config)

        assert client.api_key == config['api_key']