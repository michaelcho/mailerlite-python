import pytest
import os
import vcr
import mailerlite as MailerLite
import mailerlite.sdk.forms as Forms
import string
import random

from dotenv import load_dotenv
from pytest import fixture

@fixture
def form_keys():
    return ['id', 'type', 'slug', 'name', 'created_at', 'conversions_count', 'opens_count', 'conversion_rate', 'settings', 'last_registration_at', 'active', 'is_broken', 'has_content', 'can', 'used_in_automations', 'warnings', 'double_optin', 'screenshot_url']

@fixture
def subscriber_keys():
    return ['id', 'email', 'status', 'source', 'sent', 'opens_count', 'click_rate', 'ip_address', 'subscribed_at', 'unsubscribed_at', 'created_at', 'updated_at']

class TestForms:
    @classmethod
    def setup_class(self):
        load_dotenv()

        self.client = MailerLite.Client({
            'api_key': os.getenv('API_KEY')
        })
    
    def test_api_url_is_properly_set(self):
        assert self.client.forms.base_api_url == "api/forms"

    @vcr.use_cassette('tests/vcr_cassettes/forms-list.yml', filter_headers=['Authorization'])
    def test_list_all_forms(self, form_keys):
        """Tests an API call for getting information about all forms"""
        
        type = "popup"
        response = self.client.forms.list(type, limit=10, page=1, sort="name")

        pytest.entity_id = response['data'][0]['id']

        assert isinstance(response, dict)
        assert isinstance(response['data'], list)
        assert isinstance(response['data'][0], dict)
        assert set(form_keys).issubset(response['data'][0].keys())

    @vcr.use_cassette('tests/vcr_cassettes/forms-get.yml', filter_headers=['Authorization'])
    def test_get_form(self, form_keys):
        """Tests an API call for getting information about one form"""
        
        type = "popup"
        response = self.client.forms.get(pytest.entity_id)

        assert isinstance(response, dict)
        assert isinstance(response['data'], dict)
        assert set(form_keys).issubset(response['data'].keys())

    @vcr.use_cassette('tests/vcr_cassettes/forms-update.yml', filter_headers=['Authorization'])
    def test_update_form(self, form_keys):
        """Tests an API call for updating form information"""
        
        name = "New Form Name"
        response = self.client.forms.update(pytest.entity_id, name)

        assert isinstance(response, dict)
        assert isinstance(response['data'], dict)
        assert set(form_keys).issubset(response['data'].keys())
        assert response['data']['name'] == name

    @vcr.use_cassette('tests/vcr_cassettes/forms-get-subscribers.yml', filter_headers=['Authorization'])
    def test_get_form_subscribers(self, subscriber_keys):
        """Tests an API call for retrieving a list of subscribers who signed up using form"""
        
        response = self.client.forms.get_subscribers(pytest.entity_id, page=1, limit=20)

        assert isinstance(response, dict)
        assert isinstance(response['data'], list)
        assert set(subscriber_keys).issubset(response['data'][0].keys())

    @vcr.use_cassette('tests/vcr_cassettes/forms-delete.yml', filter_headers=['Authorization'])
    def test_get_form_subscribers(self):
        """Tests an API call for deleting a form"""
        
        response = self.client.forms.delete(pytest.entity_id)
        assert response is True

        response = self.client.forms.delete(111)
        assert response is False