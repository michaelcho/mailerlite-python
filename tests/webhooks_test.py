import pytest
import os
import vcr
import mailerlite as MailerLite
import random
import string

from dotenv import load_dotenv
from pytest import fixture


@fixture
def webhook_keys():
    return ['id', 'name', 'url', 'events', 'enabled', 'secret', 'created_at', 'updated_at']


class TestWebhooks:

    @classmethod
    def setup_class(self):
        load_dotenv()

        self.client = MailerLite.Client({
            'api_key': os.getenv('API_KEY')
        })
    
    def test_api_url_is_properly_set(self):
        assert self.client.webhooks.base_api_url == "api/webhooks"

    def test_creating_field_will_fail_if_attributes_are_incorrect(self):

        with pytest.raises(TypeError):
            self.client.webhooks.create({}, "http", "Test")

    @vcr.use_cassette('tests/vcr_cassettes/webhooks-create.yml', remove_headers=['Authorization'])
    def test_create_field(self, webhook_keys):
        """Tests an API call for creating a webhook"""

        name = "My Webhooks"        
        events = [
            "subscriber.created",
            "subscriber.unsubscribed"
        ]
        url = "https://mailerlite.com"
        response = self.client.webhooks.create(events, url, name)

        pytest.entity_id = response['data']['id']

        assert isinstance(response, dict)
        assert isinstance(response['data'], dict)
        assert set(webhook_keys).issubset(response['data'].keys())

    @vcr.use_cassette('tests/vcr_cassettes/webhooks-list.yml', remove_headers=['Authorization'])
    def test_list_all_webhooks(self, webhook_keys):
        """Tests an API call for getting information about all webhooks"""
        
        response = self.client.webhooks.list()

        assert isinstance(response, dict)
        assert isinstance(response['data'], list)
        assert isinstance(response['data'][0], dict)
        assert set(webhook_keys).issubset(response['data'][0].keys())

    @vcr.use_cassette('tests/vcr_cassettes/webhooks-get.yml', remove_headers=['Authorization'])
    def test_get_webhook(self, webhook_keys):
        """Tests an API call for getting information about one webhook"""
        
        response = self.client.webhooks.get(pytest.entity_id)

        assert isinstance(response, dict)
        assert isinstance(response['data'], dict)
        assert set(webhook_keys).issubset(response['data'].keys())

    @vcr.use_cassette('tests/vcr_cassettes/webhook-update.yml', remove_headers=['Authorization'])
    def test_update_field(self, webhook_keys):
        """Tests an API call for updating the field"""

        name = "My New Webhook Name"        
        response = self.client.webhooks.update(pytest.entity_id, name=name)

        assert isinstance(response, dict)
        assert isinstance(response['data'], dict)
        assert set(webhook_keys).issubset(response['data'].keys())

    @vcr.use_cassette('tests/vcr_cassettes/webhook-delete.yml', remove_headers=['Authorization'])
    def test_delete_webhook(self):
        """Tests an API call for webhook the field"""

        response = self.client.webhooks.delete(int(pytest.entity_id))
        assert response is True

        response = self.client.webhooks.delete(121212)
        assert response is False