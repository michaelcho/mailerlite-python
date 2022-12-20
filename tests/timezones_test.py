import pytest
import os
import vcr
import mailerlite as MailerLite

from dotenv import load_dotenv
from pytest import fixture

@fixture
def timezone_keys():
    return ['id', 'name', 'name_for_humans', 'offset_name', 'offset']


class TestTimezones:
    @classmethod
    def setup_class(self):
        load_dotenv()

        self.client = MailerLite.Client({
            'api_key': os.getenv('API_KEY')
        })
    
    def test_api_url_is_properly_set(self):
        assert self.client.timezones.base_api_url == "api/timezones"

    @vcr.use_cassette('tests/vcr_cassettes/timezones-list.yml', remove_headers=['Authorization'])
    def test_list_all_timezones(self, timezone_keys):
        response = self.client.timezones.list()

        assert isinstance(response, dict)
        assert isinstance(response['data'], list)
        assert isinstance(response['data'][0], dict)
        assert set(timezone_keys).issubset(response['data'][0].keys())