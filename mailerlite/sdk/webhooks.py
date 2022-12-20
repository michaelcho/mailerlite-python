from __future__ import absolute_import
from mailerlite.api_client import ApiClient
import re
import json

class Webhooks(object):
    base_api_url = "api/webhooks"

    def __init__(self, api_client):
        self.api_client = api_client

    def list(self):
        """
        List all webhooks
        """

        return self.api_client.request("GET", self.base_api_url).json()

    def get(self, webhook_id):
        return self.api_client.request("GET", '{}/{}'.format(self.base_api_url, webhook_id)).json()

    def update(self, webhook_id, events=None, url=None, name=None):
        if len(name) > 255:
            raise ValueError("Segment name cannot exceed 255 characters.")

        params = locals()
        body_params = {}
        for key, val in params.items():
            if val is not None and key not in ['self', 'webhook_id']:
                body_params[key] = val

        return self.api_client.request(
            "PUT", "{}/{}".format(self.base_api_url, webhook_id), body=body_params
        ).json()

    def create(self, events, url, name=None):
        if type(events) is not list:
            raise TypeError("Events should be dict.")

        body_params = {"events": events, "url": url}
        if len(name) > 0:
            body_params["name"] = name

        return self.api_client.request(
            "POST", self.base_api_url, body=body_params
        ).json()

    def delete(self, webhook_id):
        if not isinstance(webhook_id, int):
            raise ValueError("Webhook ID is not valid.")

        response = self.api_client.request(
            "DELETE", "{}/{}".format(self.base_api_url, webhook_id)
        )

        return True if response.status_code == 204 else False