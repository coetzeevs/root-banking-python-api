import requests
import os
import json

base_url = 'https://sandbox.root.co.za/v1/'


class Account:
    route = "/account/"
    api_url = base_url

    def __init__(self):
        pass

    def fetch_account(self):
        url = self.api_url + self.route
        r = requests.get(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data
