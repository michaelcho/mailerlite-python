from __future__ import absolute_import
from mailerlite.api_client import ApiClient
import re
import json
import urllib

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

    def create(self, email, **kwargs):
        available_params = ["fields", "groups", "status", "subscribed_at", "ip_address", "opted_in_at", "optin_ip", "unsubscribed_at"]
        
        valid = re.search(r'[\w.]+\@[\w.]+', email)

        if not valid:
            raise ValueError('Email address is not valid.')

        params = locals()
        body_params = {
            'email': email
        }

        for key, val in params["kwargs"].items():
            if key not in available_params:
                raise TypeError("Got an unknown argument '%s'" % key)

            if key == 'fields' and type(val) is not dict:
                raise TypeError('Fields argument should be a dict.')

            if key == 'groups' and type(val) is not list:
                raise TypeError('Groups argument should be a list.')

            body_params[key] = val
        
        return self.api_client.request("POST", self.base_api_url, body=body_params).json()

    def update(self, email, **kwargs):
        available_params = ["fields", "groups", "status", "subscribed_at", "ip_address", "opted_in_at", "optin_ip", "unsubscribed_at"]
        
        valid = re.search(r'[\w.]+\@[\w.]+', email)

        if not valid:
            raise ValueError('Email address is not valid.')

        params = locals()
        body_params = {
            'email': email
        }

        for key, val in params["kwargs"].items():
            if key not in available_params:
                raise TypeError("Got an unknown argument '%s'" % key)

            if key == 'fields' and type(val) is not dict:
                raise TypeError('Fields argument should be a dict.')

            if key == 'groups' and type(val) is not list:
                raise TypeError('Groups argument should be a list.')

            body_params[key] = val
        
        return self.api_client.request("POST", self.base_api_url, body=body_params).json()
    
    def get(self, id):
        valid = re.search(r'[\w.]+\@[\w.]+', id)

        if not valid and not isinstance(id, int):
            raise ValueError('Email address or subscriber id are not valid.')

        return self.api_client.request("GET", '{}/{}'.format(self.base_api_url, id)).json()

    def delete(self, id):
        if not isinstance(id, int):
            raise ValueError('Subscriber ID is not valid.')

        response = self.api_client.request("DELETE", '{}/{}'.format(self.base_api_url, id))

        return response.status_code

    def get_import(self, id):
        if not isinstance(id, int):
            raise ValueError('Subscriber ID is not valid.')

        return self.api_client.request("GET", '{}/import/{}'.format(self.base_api_url, id)).json()

    def assign_subscriber_to_group(self, subscriber_id, group_id):
        if not isinstance(subscriber_id, int):
            raise ValueError('Subscriber ID is not valid.')

        if not isinstance(group_id, int):
            raise ValueError('Group ID is not valid.')

        return self.api_client.request("POST", '{}/{}/groups/{}'.format(self.base_api_url, subscriber_id, group_id)).json()

    def unassign_subscriber_from_group(self, subscriber_id, group_id):
        if not isinstance(subscriber_id, int):
            raise ValueError('Subscriber ID is not valid.')

        if not isinstance(group_id, int):
            raise ValueError('Group ID is not valid.')

        response = self.api_client.request("DELETE", '{}/{}/groups/{}'.format(self.base_api_url, subscriber_id, group_id))

        return True if response.status_code == 204 else False