import requests
import os
import json

base_url = 'https://sandbox.root.co.za/v1/'


class Category:
    route = "/categories/"
    api_url = base_url
    category_id = ""
    name = ""
    icon = ""
    theme = ""
    soft_limit = ""
    created_at = ""

    def __init__(self):
        pass

    def list_all_categories(self):
        url = self.api_url + self.route
        r = requests.get(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data

    def retrieve_category(self):
        url = self.api_url + self.route + self.category_id
        r = requests.get(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data

    def create_category(self):
        payload = json.dumps({
            "name": self.name
        })
        url = self.api_url + self.route
        r = requests.post(url, auth=(os.environ['TEST_API_KEY'], ''), data=payload)
        data = json.loads(r.text)

        return data

    def update_category(self):
        payload = json.dumps({
            "name": self.name
        })
        url = self.api_url + self.route + self.category_id
        r = requests.patch(url, auth=(os.environ['TEST_API_KEY'], ''), data=payload)
        data = json.loads(r.text)

        return data

    def delete_category(self):
        url = self.api_url + self.route + self.category_id
        r = requests.delete(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data

    def list_category_transactions(self):
        url = self.api_url + self.route + self.category_id + '/transactions'
        r = requests.get(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data
