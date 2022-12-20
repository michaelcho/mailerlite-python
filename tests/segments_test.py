import pytest
import os
import vcr
import mailerlite as MailerLite
import mailerlite.sdk.segments as Segments
import random
import string

from dotenv import load_dotenv
from pytest import fixture


@fixture
def segment_keys():
    return ['id', 'name', 'total', 'open_rate', 'click_rate', 'created_at']

@fixture
def subscriber_keys():
    return ['id', 'email', 'status', 'source', 'sent', 'opens_count', 'click_rate', 'ip_address', 'subscribed_at', 'unsubscribed_at', 'created_at', 'updated_at']

class TestSegments:
    @classmethod
    def setup_class(self):
        load_dotenv()

        self.client = MailerLite.Client({
            'api_key': os.getenv('API_KEY')
        })
    
    def test_api_url_is_properly_set(self):
        assert self.client.segments.base_api_url == "api/segments"

    @vcr.use_cassette('tests/vcr_cassettes/segments-list.yml', remove_headers=['Authorization'])
    def test_list_all_segments(self, segment_keys):
        """Tests an API call for getting information about all segments"""
        
        response = self.client.segments.list(limit=10, page=1)

        assert isinstance(response, dict)
        assert isinstance(response['data'][0], dict)
        assert set(segment_keys).issubset(response['data'][0].keys())

    @vcr.use_cassette('tests/vcr_cassettes/segments-get-subscribers.yml', remove_headers=['Authorization'])
    def test_list_all_segments(self, segment_keys):
        """Tests an API call for getting in formation about all subscribers belonging to a specific segment"""
        
        segment_id = 75015812692314029
        response = self.client.segments.get_subscribers(segment_id)

        assert isinstance(response, dict)
        assert isinstance(response['data'], dict)
        assert set(segment_keys).issubset(response['data'].keys())

    def test_updating_segment_will_fail_if_name_exceeds_max_length(self):
        name = ''.join(random.choices(string.ascii_letters, k=300))
        segment_id = 123

        with pytest.raises(ValueError):
            self.client.segments.update(segment_id, name)

    @vcr.use_cassette('tests/vcr_cassettes/segments-update.yml', remove_headers=['Authorization'])
    def test_update_segment(self, segment_keys):
        """Tests an API call for updating information about segment"""
        
        segment_id = 75015812692314029
        name = "New Test Segment Name"
        response = self.client.segments.update(segment_id, name)

        assert response is True

        segment_id = 123123
        response = self.client.segments.update(segment_id, name)

        assert response is False

    @vcr.use_cassette('tests/vcr_cassettes/segments-delete.yml', remove_headers=['Authorization'])
    def test_update_segment(self, segment_keys):
        """Tests an API call for deleting segment"""
        
        segment_id = 75015812692314029
        response = self.client.segments.delete(segment_id)

        assert response is True

        segment_id = 123123
        response = self.client.segments.delete(segment_id)

        assert response is False