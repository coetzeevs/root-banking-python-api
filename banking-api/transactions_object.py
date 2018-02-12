import requests
import os
import json

base_url = 'https://sandbox.root.co.za/v1/'


class Transactions:
    route = "/transactions/"
    api_url = base_url
    transaction_id = ""
    category_id = ""
    category_rule = "all"
    content_type = "application/json"
    tag_id = ""

    def __init__(self):
        pass

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

    def change_category(self):
        payload = [
            ("category_id", self.category_id),
            ("category_rule", self.category_rule)
        ]
        url = self.api_url + self.route + self.transaction_id + "/category"
        r = requests.patch(url, auth=(os.environ['TEST_API_KEY'], ''), data=payload)
        data = json.loads(r.text)

        return data

    # To do --> figure out how to handle more than one Tag ID if there are more than one tags to be assigned
    def tag_transaction(self):
        headers = {
            'Content-Type': self.content_type
        }
        payload = json.dumps({
            "tag_ids": [self.tag_id]
        })
        url = self.api_url + self.route + self.transaction_id + "/tags"
        r = requests.post(url, auth=(os.environ['TEST_API_KEY'], ''), data=payload, headers=headers)
        data = json.loads(r.text)

        return data

    # To do --> figure out how to handle more than one Tag ID if there are more than one tags to be assigned
    def remove_transaction_tag(self):
        headers = {
            'Content-Type': self.content_type
        }
        payload = json.dumps({
            "tag_ids": [self.tag_id]
        })
        url = self.api_url + self.route + self.transaction_id + "/tags"
        r = requests.delete(url, auth=(os.environ['TEST_API_KEY'], ''), data=payload, headers=headers)
        data = json.loads(r.text)

        return data
