# coding: utf-8

from __future__ import absolute_import

# import all api files into api package
from mailerlite.sdk.campaigns import Campaigns
from mailerlite.sdk.fields import Fields
from mailerlite.sdk.forms import Forms
from mailerlite.sdk.groups import Groups
from mailerlite.sdk.segments import Segments
from mailerlite.sdk.stats import Stats
from mailerlite.sdk.subscribers import Subscribers

from mailerlite.api_client import ApiClient


class Client(object):
    def __init__(self, config={}):
        # Initialize ApiClient
        self.api_client = ApiClient(config)

        # Bootstrap API classes
        self.subscribers = Subscribers(self.api_client)
        self.groups = Groups(self.api_client)
        self.segments = Segments(self.api_client)
        self.fields = Fields(self.api_client)
        self.forms = Forms(self.api_client)
        self.campaigns = Campaigns(self.api_client)
