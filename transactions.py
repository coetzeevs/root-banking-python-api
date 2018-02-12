import requests
import os
import json

base_url = 'https://sandbox.root.co.za/v1/'


class Accounts:
    route = "/transactions/"
    api_url = base_url
    transaction_id = ""

    def list_all_transactions(self):
        url = self.api_url + self.route
        r = requests.get(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data

    def retrieve_transaction(self):
        url = self.api_url + self.route + self.transaction_id
        r = requests.get(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data


# trans = Accounts()
#
# trns_id = trans.list_all_transactions()[0]['transaction_id']
#
# trnas = trans.retrieve_transaction()
#
# print(trnas)
