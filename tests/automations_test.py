import pytest
import os
import vcr
import mailerlite as MailerLite

from dotenv import load_dotenv
from pytest import fixture


@fixture
def automation_keys():
    return ['id', 'name', 'enabled', 'trigger_data', 'steps', 'triggers', 'complete', 'broken', 'warnings', 'stats']


class TestAutomations:

    @classmethod
    def setup_class(self):
        load_dotenv()

        self.client = MailerLite.Client({
            'api_key': os.getenv('API_KEY')
        })
    
    def test_api_url_is_properly_set(self):
        assert self.client.automations.base_api_url == "api/automations"

    @vcr.use_cassette('tests/vcr_cassettes/automations-list.yml', remove_headers=['Authorization'])
    def test_list_all_automations(self, automation_keys):
        """Tests an API call for getting information about all automations"""
        
        response = self.client.automations.list()

        assert isinstance(response, dict)
        assert isinstance(response['data'], list)
        assert isinstance(response['data'][0], dict)
        assert set(automation_keys).issubset(response['data'][0].keys())

    @vcr.use_cassette('tests/vcr_cassettes/automations-get.yml', remove_headers=['Authorization'])
    def test_get_automation(self, automation_keys):
        """Tests an API call for getting information about one automation"""
        
        response = self.client.automations.get(75040845299975641)

        assert isinstance(response, dict)
        assert isinstance(response['data'], dict)
        assert set(automation_keys).issubset(response['data'].keys())

    @vcr.use_cassette('tests/vcr_cassettes/automations-activity.yml', remove_headers=['Authorization'])
    def test_get_automation_activity(self, automation_keys):
        """Tests an API call for getting activity information of automation"""
        
        response = self.client.automations.activity(75040845299975641, filter={"filter[status]": "active"})

        assert isinstance(response, dict)
        assert isinstance(response['data'], list)