import pytest
import os
import vcr
import mailerlite as MailerLite
import mailerlite.sdk.campaigns as Campaigns
import string
import random

from dotenv import load_dotenv
from pytest import fixture
from datetime import datetime

@fixture
def campaign_keys():
    return ['id', 'account_id', 'name', 'type', 'status', 'settings', 'filter', 'filter_for_humans', 'delivery_schedule', 'language_id', 'updated_at', 'scheduled_for', 'queued_at', 'started_at', 'finished_at', 'stopped_at', 'default_email_id', 'emails', 'used_in_automations', 'type_for_humans', 'is_stopped', 'has_winner', 'winner_version_for_human', 'winner_sending_time_for_humans', 'winner_selected_manually_at', 'uses_ecommerce', 'uses_survey', 'can_be_scheduled', 'warnings', 'is_currently_sending_out']

@fixture
def campaign_activity_keys():
    return ['id', 'opens_count', 'clicks_count', 'subscriber']

@fixture
def campaign_language_keys():
    return ['id', 'shortcode', 'iso639', 'name', 'direction']


class TestCampaigns:
    @classmethod
    def setup_class(self):
        load_dotenv()

        self.client = MailerLite.Client({
            'api_key': os.getenv('API_KEY')
        })
    
    def test_api_url_is_properly_set(self):
        assert self.client.campaigns.base_api_url == "api/campaigns"

    @vcr.use_cassette('tests/vcr_cassettes/campaign-create.yml', remove_headers=['Authorization'])
    def test_create_campaign(self, campaign_keys):
        params = {
            "name": "Test Campaign",
            "language_id": 1,
            "type": "regular",
            "emails": [{
                "subject": "This is a test campaign",
                "from_name": "Test Man",
                "from": "testuser@mailerlite.com",
                "content": "Hi there, this is a test campaign!"
            }]
        }

        response = self.client.campaigns.create(params)
        pytest.entity_id = response['data']['id']
        
        assert isinstance(response, dict)
        assert isinstance(response['data'], dict)
        assert set(campaign_keys).issubset(response['data'].keys())
        assert response['data']['name'] == params['name']
        assert int(response['data']['language']['id']) == params['language_id']
        assert response['data']['type'] == params['type']

    @vcr.use_cassette('tests/vcr_cassettes/campaign-update.yml', remove_headers=['Authorization'])
    def test_update_campaign(self, campaign_keys):
        params = {
            "name": "New Campaign Name",
            "language_id": 2,
            "emails": [{
                "subject": "This is a new test campaign",
                "from_name": "Test Man",
                "from": "testuser@mailerlite.com",
                "content": "Hi there, this is a new test campaign!"
            }]
        }

        response = self.client.campaigns.update(pytest.entity_id, params)
        
        assert isinstance(response, dict)
        assert isinstance(response['data'], dict)
        assert set(campaign_keys).issubset(response['data'].keys())
        assert response['data']['name'] == params['name']
        assert int(response['data']['language']['id']) == params['language_id']

    @vcr.use_cassette('tests/vcr_cassettes/campaign-get.yml', remove_headers=['Authorization'])
    def test_get_campaign(self, campaign_keys):
        response = self.client.campaigns.get(pytest.entity_id)
        
        assert isinstance(response, dict)
        assert isinstance(response['data'], dict)
        assert set(campaign_keys).issubset(response['data'].keys())

    @vcr.use_cassette('tests/vcr_cassettes/campaign-list.yml', remove_headers=['Authorization'])
    def test_list_campaigns(self, campaign_keys):
        response = self.client.campaigns.list(limit=10, page=1, filter={"filter[status]": "draft"})

        assert isinstance(response, dict)
        assert isinstance(response['data'], list)
        assert isinstance(response['data'][0], dict)
        assert set(campaign_keys).issubset(response['data'][0].keys())

    @vcr.use_cassette('tests/vcr_cassettes/campaign-schedule.yml', remove_headers=['Authorization'])
    def test_schedule_campaign(self, campaign_keys):
        params = {
            "delivery": "scheduled",
            "schedule": {
                "date": "2022-12-31",
                "hours": "22",
                "minutes": "00"
            }
        }
        response = self.client.campaigns.schedule(pytest.entity_id, params)

        assert isinstance(response, dict)
        assert isinstance(response['data'], dict)
        schedule_date = datetime.strptime(response['data']['scheduled_for'], '%Y-%m-%d %H:%M:%S')
        test_date = datetime.strptime(params['schedule']['date'], '%Y-%m-%d')
        assert schedule_date.date() == test_date.date()

    @vcr.use_cassette('tests/vcr_cassettes/campaign-cancel.yml', remove_headers=['Authorization'])
    def test_cancel_campaign(self):
        response = self.client.campaigns.cancel(pytest.entity_id)

        assert response['data']['status'] == 'draft'

    @vcr.use_cassette('tests/vcr_cassettes/campaign-delete.yml', remove_headers=['Authorization'])
    def test_delete_campaign(self):
        response = self.client.campaigns.delete(pytest.entity_id)

        assert response == True

        response = self.client.campaigns.delete(121212)

        assert response == False

    @vcr.use_cassette('tests/vcr_cassettes/campaign-activity.yml', remove_headers=['Authorization'])
    def test_activity_campaign(self, campaign_activity_keys):
        response = self.client.campaigns.activity(75037917434611569)

        assert isinstance(response, dict)
        assert isinstance(response['data'], list)
        assert set(campaign_activity_keys).issubset(response['data'][0].keys())

    @vcr.use_cassette('tests/vcr_cassettes/campaign-languages.yml', remove_headers=['Authorization'])
    def test_campaign_languages(self, campaign_language_keys):
        response = self.client.campaigns.languages()

        assert isinstance(response, dict)
        assert isinstance(response['data'], list)
        assert set(campaign_language_keys).issubset(response['data'][0].keys())