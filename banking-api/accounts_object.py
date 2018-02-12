import requests
import os
import json

base_url = 'https://sandbox.root.co.za/v1/'


class Accounts:
    route = "/account/"
    api_url = base_url

    def fetch_account(self):
        url = self.api_url + self.route
        r = requests.get(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data

# acc = Accounts()
#
# acs = acc.fetch_account()
#
# print(acs)