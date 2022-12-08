from __future__ import absolute_import

import datetime
import json

class ApiClient(object):
    def __init__(self, config = {}):
        """Contructor"""
        
        # Base URL of the API
        self.host = "https://connect.mailerlite.com/"
        # Base headers
        self.default_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'MailerLite-Python-SDK-Client'
        }
        self.set_config(config)
    
    def set_config(self, config = {}):
        """API Client Configuration Setter"""

        # Authentication
        self.api_key = config['api_key'] if 'api_key' in config.keys() else ''
        self.default_headers['Authorization'] = 'Bearer ' + self.api_key

        # API version
        if 'api_version' in config.keys():
            self.api_version = config['api_version']
            self.default_headers['X-Version'] = self.api_version
        
    def request(self, method, url, query_params=None, header_params=None):
        pass