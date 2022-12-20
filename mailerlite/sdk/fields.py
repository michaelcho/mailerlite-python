from __future__ import absolute_import
from mailerlite.api_client import ApiClient
import re
import json


class Fields(object):
    base_api_url = "api/fields"

    def __init__(self, api_client):
        self.api_client = api_client

    def create(self, name, type):
        allowed_types = ["text", "number", "date"]

        if type not in allowed_types:
            raise ValueError('Type be text, number or date')
        
        if len(name) > 255:
            raise ValueError("Field name cannot exceed 255 characters.")

        body_params = {"name": name, "type": type}

        return self.api_client.request(
            "POST", self.base_api_url, body=body_params
        ).json()
    
    def list(self, **kwargs):
        available_params = ["limit", "page", "filter", "sort"]

        params = locals()
        query_params = {}
        for key, val in params["kwargs"].items():
            if key not in available_params:
                raise TypeError("Got an unknown argument '%s'" % key)
            query_params[key] = val

        return self.api_client.request("GET", self.base_api_url, query_params).json()

    def update(self, field_id, name):
        if len(name) > 255:
            raise ValueError("Field name cannot exceed 255 characters.")

        body_params = {"name": name}

        return self.api_client.request(
            "PUT", '{}/{}'.format(self.base_api_url, field_id), body=body_params
        ).json()

    def delete(self, field_id):
        response =  self.api_client.request(
            "DELETE", '{}/{}'.format(self.base_api_url, field_id)
        )

        return True if response.status_code == 204 else False