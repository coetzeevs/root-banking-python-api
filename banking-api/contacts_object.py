import requests
import os
import json

base_url = 'https://sandbox.root.co.za/v1/'


class Contact:
    route = "/contacts/"
    api_url = base_url
    contact_id = ""
    name = ""
    bank_account_number = ""
    bank_name = ""
    email = ""
    created_at = ""

    def __init__(self):
        pass

    def list_all_contacts(self):
        url = self.api_url + self.route
        r = requests.get(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data

    def retrieve_a_contact(self):
        url = self.api_url + self.route + self.contact_id
        r = requests.get(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data

    def create_contact(self):
        payload = json.dumps({
            "name": self.name,
            "bank_number": self.bank_account_number,
            "bank_name": self.bank_name,
            "email": self.email
        })
        url = self.api_url + self.route
        r = requests.post(url, auth=(os.environ['TEST_API_KEY'], ''), data=payload)
        data = json.loads(r.text)

        return data

    def update_contact(self):
        payload = json.dumps({
            "name": self.name,
            "bank_number": self.bank_account_number,
            "bank_name": self.bank_name,
            "email": self.email
        })
        url = self.api_url + self.route + self.contact_id
        r = requests.patch(url, auth=(os.environ['TEST_API_KEY'], ''), data=payload)
        data = json.loads(r.text)

        return data

    def archive_contact(self):
        url = self.api_url + self.route + self.contact_id
        r = requests.delete(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data

    def list_contact_transactions(self):
        url = self.api_url + self.route + self.contact_id + "/transactions"
        r = requests.get(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data
