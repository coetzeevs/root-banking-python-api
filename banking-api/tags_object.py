import requests
import os
import json

base_url = 'https://sandbox.root.co.za/v1/'


class Tags:
    route = "/tags/"
    api_url = base_url
    tag_id = ""
    name = ""
    tag_limit = ""
    created_at = ""

    def __init__(self):
        pass

    def list_all_tags(self):
        url = self.api_url + self.route
        r = requests.get(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data

    def retrieve_a_tag(self):
        url = self.api_url + self.route + self.tag_id
        r = requests.get(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data

    def create_tag(self):
        payload = json.dumps({
            "name": self.name,
            "tag_limit": self.tag_limit
        })
        url = self.api_url + self.route
        r = requests.post(url, auth=(os.environ['TEST_API_KEY'], ''), data=payload)
        data = json.loads(r.text)

        return data

    def update_tag(self):
        payload = json.dumps({
            "name": self.name,
            "tag_limit": self.tag_limit
        })
        url = self.api_url + self.route + self.tag_id
        r = requests.patch(url, auth=(os.environ['TEST_API_KEY'], ''), data=payload)
        data = json.loads(r.text)

        return data

    def delete_tag(self):
        url = self.api_url + self.route + self.tag_id
        r = requests.delete(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data

    def list_tag_transactions(self):
        url = self.api_url + self.route + self.tag_id + "/transactions"
        r = requests.patch(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data
