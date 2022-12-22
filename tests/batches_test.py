import pytest
import os
import vcr
import mailerlite as MailerLite

from dotenv import load_dotenv
from pytest import fixture


@fixture
def batch_keys():
    return ['total', 'successful', 'failed', 'responses']


class TestBatches:
    @classmethod
    def setup_class(self):
        load_dotenv()

        self.client = MailerLite.Client({
            'api_key': os.getenv('API_KEY')
        })

    def test_api_url_is_properly_set(self):
        assert self.client.batches.base_api_url == "api/batch"

    @vcr.use_cassette('tests/vcr_cassettes/batches-request.yml', record_mode="new_episodes", filter_headers=['Authorization'])
    def test_given_correct_request_when_calling_request_then_batch_request_is_made(self, batch_keys):
        params = [
                {
                    'method': 'GET',
                    'path': 'api/subscribers/list'
                },
                {
                    'method': 'GET',
                    'path': 'api/campaigns/list'
                },
        ]

        response = self.client.batches.request(params)
        print(response)
        assert isinstance(response, dict)
        assert set(batch_keys).issubset(response.keys())
