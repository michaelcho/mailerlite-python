from __future__ import absolute_import
from mailerlite.api_client import ApiClient
import re
import json
import urllib


class Groups(object):
    base_api_url = "api/groups"

    def __init__(self, api_client):
        self.api_client = api_client

    def list(self, **kwargs):
        """
        List all groups

        Get all groups in an account.

        :param list[str] filter[name]: Returns partial matches.
        :param int limit: Number of results per page, defaults to 25
        :param int page: Page number, defaults to 1
        :param str sort: Can be one of: name, total, open_rate, click_rate, created_at. Defaults to ascending order; prepend -, e.g. -total for descending order
        """

        available_params = ["list", "limit", "page", "sort"]

        params = locals()
        query_params = {}
        for key, val in params["kwargs"].items():
            if key not in available_params:
                raise TypeError("Got an unknown argument '%s'" % key)
            query_params[key] = val

        return self.api_client.request("GET", self.base_api_url, query_params).json()

    def create(self, name):
        if len(name) > 255:
            raise ValueError("Group name cannot exceed 255 characters.")

        params = locals()
        body_params = {"name": name}

        return self.api_client.request(
            "POST", self.base_api_url, body=body_params
        ).json()

    def update(self, group_id, name):
        if len(name) > 255:
            raise ValueError("Group name cannot exceed 255 characters.")

        params = locals()
        body_params = {"name": name}

        return self.api_client.request(
            "PUT", "{}/{}".format(self.base_api_url, group_id), body=body_params
        ).json()

    def delete(self, group_id):
        response = self.api_client.request(
            "DELETE", "{}/{}".format(self.base_api_url, group_id)
        )

        return True if response.status_code == 204 else False

    def get_group_subscribers(self, group_id, **kwargs):
        available_params = ["filter", "limit", "page"]

        params = locals()
        query_params = {}
        for key, val in params["kwargs"].items():
            if key not in available_params:
                raise TypeError("Got an unknown argument '%s'" % key)
            query_params[key] = val

        return self.api_client.request(
            "GET",
            "{}/{}/{}".format(self.base_api_url, group_id, "subscribers"),
            query_params,
        ).json()
