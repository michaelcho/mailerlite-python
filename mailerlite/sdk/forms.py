from __future__ import absolute_import
from mailerlite.api_client import ApiClient
import re
import json


class Forms(object):
    base_api_url = "api/forms"

    def __init__(self, api_client):
        self.api_client = api_client

    def list(self, type, **kwargs):
        available_params = ["limit", "page", "filter", "sort"]

        params = locals()
        query_params = {}
        for key, val in params["kwargs"].items():
            if key not in available_params:
                raise TypeError("Got an unknown argument '%s'" % key)
            query_params[key] = val

        return self.api_client.request(
            "GET", "{}/{}".format(self.base_api_url, type), query_params
        ).json()

    def get(self, form_id):
        return self.api_client.request(
            "GET", "{}/{}".format(self.base_api_url, form_id)
        ).json()

    def update(self, form_id, name):
        body_params = {"name": name}

        return self.api_client.request(
            "PUT", "{}/{}".format(self.base_api_url, form_id), body=body_params
        ).json()

    def get_subscribers(self, form_id, **kwargs):
        available_params = ["limit", "page", "filter"]

        params = locals()
        query_params = {}
        for key, val in params["kwargs"].items():
            if key not in available_params:
                raise TypeError("Got an unknown argument '%s'" % key)
            query_params[key] = val

        return self.api_client.request(
            "GET", "{}/{}/subscribers".format(self.base_api_url, form_id), query_params
        ).json()

    def delete(self, form_id):
        response = self.api_client.request(
            "DELETE", "{}/{}".format(self.base_api_url, form_id)
        )

        return True if response.status_code == 204 else False
