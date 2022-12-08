from __future__ import absolute_import
from mailerlite.api_client import ApiClient


class Subscribers(object):
    base_api_url = "api/subscribers"

    def __init__(self, api_client):
        self.api_client = api_client

    def list(self, **kwargs):
        """
        List all subscribers

        Get all subscribers in an account.

        :param list[str] filter[status]: Must be one of the possible statuses: active, unsubscribed, unconfirmed, bounced or junk.
        :param int limit: Number of results per page, defaults to 25
        :param int page: Page number, defaults to 1
        """

        available_params = ["list", "limit", "page"]

        params = locals()
        query_params = {}
        for key, val in params["kwargs"].items():
            if key not in available_params:
                raise TypeError("Got an unknown argument '%s'" % key)
            query_params[key] = val

        return self.api_client.request("GET", self.base_api_url, query_params).json()
