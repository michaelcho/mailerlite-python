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

    @vcr.use_cassette('tests/vcr_cassettes/automations-list.yml', filter_headers=['Authorization'])
    def test_list_of_all_automations_should_be_returned(self, automation_keys):
        response = self.client.automations.list()

        assert isinstance(response, dict)
        assert isinstance(response['data'], list)
        assert isinstance(response['data'][0], dict)
        assert set(automation_keys).issubset(response['data'][0].keys())

    @vcr.use_cassette('tests/vcr_cassettes/automations-get.yml', filter_headers=['Authorization'])
    def test_automation_information_should_be_returned_when_valid_automation_id_is_provided(self, automation_keys):
        response = self.client.automations.get(75040845299975641)

        assert isinstance(response, dict)
        assert isinstance(response['data'], dict)
        assert set(automation_keys).issubset(response['data'].keys())

    @vcr.use_cassette('tests/vcr_cassettes/automations-activity.yml', filter_headers=['Authorization'])
    def test_automation_activity_information_should_be_returned_when_valid_automation_id_is_provided(self):
        response = self.client.automations.activity(75040845299975641, filter={"filter[status]": "active"})

        assert isinstance(response, dict)
        assert isinstance(response['data'], list)
