from __future__ import absolute_import
from mailerlite.api_client import ApiClient
import re
import json


class Timezones(object):
    base_api_url = "api/timezones"

    def __init__(self, api_client):
        self.api_client = api_client

    def list(self):
        return self.api_client.request("GET", self.base_api_url).json()
