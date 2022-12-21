import pytest
import os
import vcr
import mailerlite as MailerLite
import mailerlite.sdk.fields as Fields
import random
import string

from dotenv import load_dotenv
from pytest import fixture


@fixture
def field_keys():
    return ['id', 'name', 'key', 'type']


class TestFields:

    @classmethod
    def setup_class(self):
        load_dotenv()

        self.client = MailerLite.Client({
            'api_key': os.getenv('API_KEY')
        })
    
    def test_api_url_is_properly_set(self):
        assert self.client.fields.base_api_url == "api/fields"

    def test_creating_field_will_fail_if_attributes_are_incorrect(self):
        name = ''.join(random.choices(string.ascii_letters, k=300))
        type = 'text'

        with pytest.raises(ValueError):
            self.client.fields.create(name, type)

        type = 'unknown'
        with pytest.raises(ValueError):
            self.client.fields.create(name, type)

    @vcr.use_cassette('tests/vcr_cassettes/fields-create.yml', filter_headers=['Authorization'])
    def test_create_field(self, field_keys):
        """Tests an API call for creating a field"""

        name = "My Field"        
        type = "text"
        response = self.client.fields.create(name, type)

        pytest.entity_id = response['data']['id']

        assert isinstance(response, dict)
        assert isinstance(response['data'], dict)
        assert set(field_keys).issubset(response['data'].keys())

    @vcr.use_cassette('tests/vcr_cassettes/fields-list.yml', filter_headers=['Authorization'])
    def test_list_all_fields(self, field_keys):
        """Tests an API call for getting information about all fields"""
        
        response = self.client.fields.list(limit=10, page=1, sort="name")

        assert isinstance(response, dict)
        assert isinstance(response['data'], list)
        assert isinstance(response['data'][0], dict)
        assert set(field_keys).issubset(response['data'][0].keys())

    @vcr.use_cassette('tests/vcr_cassettes/fields-update.yml', filter_headers=['Authorization'])
    def test_update_field(self, field_keys):
        """Tests an API call for updating the field"""

        name = "My New Field Name"        
        response = self.client.fields.update(field_id=pytest.entity_id, name=name)

        assert isinstance(response, dict)
        assert isinstance(response['data'], dict)
        assert set(field_keys).issubset(response['data'].keys())

    @vcr.use_cassette('tests/vcr_cassettes/fields-delete.yml', filter_headers=['Authorization'])
    def test_delete_field(self, field_keys):
        """Tests an API call for deleting the field"""

        response = self.client.fields.delete(pytest.entity_id)
        assert response is True

        response = self.client.fields.delete(121212)
        assert response is False