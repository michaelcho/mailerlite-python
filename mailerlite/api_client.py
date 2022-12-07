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
            'User-Agent': 'MailerLite-Python-SDK-Client/version'
        }
        self.set_config(config)
    
    def set_config(self, config = {}):
        """API Client Configuration Setter"""

        # Authentication
        self.api_key = config['api_key'] if 'api_key' in config.keys() else ''