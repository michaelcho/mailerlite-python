import pytest
import os
import vcr
import mailerlite as MailerLite
import mailerlite.sdk.subscribers as Subscribers

from dotenv import load_dotenv
from pytest import fixture
from pprint import pprint

@fixture
def subscriber_keys():
    return ['id', 'email', 'status', 'source', 'sent', 'opens_count', 'click_rate', 'ip_address', 'subscribed_at', 'unsubscribed_at', 'created_at', 'updated_at']

class TestSubscribers:
    @classmethod
    def setup_class(self):
        load_dotenv()

        self.client = MailerLite.Client({
            'api_key': os.getenv('API_KEY')
        })
    
    def test_api_url_is_properly_set(self):
        assert self.client.subscribers.base_api_url == "api/subscribers"

    @vcr.use_cassette('tests/vcr_cassettes/subscribers-list.yml', remove_headers=['Authorization'])
    def test_list_all_subscribers(self, subscriber_keys):
        """Tests an API call for getting information about all subscribers"""
        
        response = self.client.subscribers.list(limit=10, page=1)

        assert isinstance(response, dict)
        assert isinstance(response['data'], list)
        assert isinstance(response['data'][0], dict)
        assert set(subscriber_keys).issubset(response['data'][0].keys())
