# coding: utf-8

from __future__ import absolute_import

# import all api files into api package
from mailerlite.api.campaigns_api import CampaignsApi
from mailerlite.api.fields_api import FieldsApi
from mailerlite.api.forms_api import FormsApi
from mailerlite.api.groups_api import GroupsApi
from mailerlite.api.segments_api import SegmentsApi
from mailerlite.api.stats_api import StatsApi
from mailerlite.api.subscribers_api import SubscribersApi

from mailerlite.configuration import Configuration
from mailerlite.api_client import ApiClient