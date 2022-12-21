from __future__ import absolute_import
from mailerlite.api_client import ApiClient
import json


class Automations(object):
    base_api_url = "api/automations"

    def __init__(self, api_client):
        self.api_client = api_client

    def list(self):
        """
        List all automations
        """

        return self.api_client.request("GET", self.base_api_url).json()

    def get(self, automation_id):
        return self.api_client.request(
            "GET", "{}/{}".format(self.base_api_url, automation_id)
        ).json()

    def activity(self, automation_id, **kwargs):

        available_params = ["filter", "page", "limit"]

        params = locals()
        query_params = {}
        for key, val in params["kwargs"].items():
            if key not in available_params:
                raise TypeError("Got an unknown argument '%s'" % key)

            if key == "filter":
                for filter_key, filter_value in val.items():
                    query_params[filter_key] = filter_value
            else:
                query_params[key] = val

        return self.api_client.request(
            "GET",
            "{}/{}/activity".format(self.base_api_url, automation_id),
            query_params,
        ).json()
