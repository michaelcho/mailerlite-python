from __future__ import absolute_import
from mailerlite.api_client import ApiClient
import re
import json


class Campaigns(object):
    base_api_url = "api/campaigns"

    def __init__(self, api_client):
        self.api_client = api_client

    def create(self, campaign):
        return self.api_client.request(
            "POST", self.base_api_url, body=campaign
        ).json()

    def update(self, campaign_id, campaign):
        return self.api_client.request(
            "PUT", '{}/{}'.format(self.base_api_url, campaign_id), body=campaign
        ).json()

    def get(self, campaign_id):
        return self.api_client.request(
            "GET", '{}/{}'.format(self.base_api_url, campaign_id)
        ).json()

    def list(self, **kwargs):
        available_params = ["filter", "page", "limit"]

        params = locals()
        query_params = {}
        for key, val in params["kwargs"].items():
            if key not in available_params:
                raise TypeError("Got an unknown argument '%s'" % key)
            query_params[key] = val

        return self.api_client.request(
            "GET", self.base_api_url, query_params
        ).json()

    def schedule(self, campaign_id, schedule):
        return self.api_client.request(
            "POST", '{}/{}/schedule'.format(self.base_api_url, campaign_id), body=schedule
        ).json()

    def cancel(self, campaign_id):
        return self.api_client.request(
            "POST", '{}/{}/cancel'.format(self.base_api_url, campaign_id)
        ).json()

    def delete(self, campaign_id):
        response =  self.api_client.request(
            "DELETE", '{}/{}'.format(self.base_api_url, campaign_id)
        )

        return True if response.status_code == 204 else False

    def activity(self, campaign_id):
        return self.api_client.request(
            "POST", '{}/{}/reports/subscriber-activity'.format(self.base_api_url, campaign_id)
        ).json()

    def languages(self):
        return self.api_client.request(
            "GET", '{}/languages'.format(self.base_api_url)
        ).json()