import requests
import os
import json

base_url = 'https://sandbox.root.co.za/v1/'


class Transactional:
    route = "/transact/eft/"
    api_url = base_url
    contact_id = ""
    amount = ""
    description = ""
    their_reference = ""
    category_id = ""
    emails = ""
    bank_name = ""
    bank_account_number = ""
    contact_name = ""
    contact_email = ""
    save_contact = ""

    def __init__(self):
        pass

    def eft_a_contact(self):
        payload = json.dumps({
            "amount": self.amount,
            "description": self.description,
            "their_reference": self.their_reference,
            "category_id": self.category_id,
            "emails": [self.emails]
        })
        url = self.api_url + self.route + self.contact_id
        r = requests.post(url, auth=(os.environ['TEST_API_KEY'], ''), data=payload)
        data = json.loads(r.text)

        return data

    def once_off_eft(self):
        payload = json.dumps({
            "bank_name": self.bank_name,
            "bank_number": self.bank_account_number,
            "contact_number": self.contact_name,
            "amount": self.amount,
            "contact_email": self.contact_email,
            "description": self.description,
            "their_reference": self.their_reference,
            "category_id": self.category_id,
            "save_contact": self.save_contact,
            "emails": [self.emails]
        })
        url = self.api_url + self.route + self.contact_id
        r = requests.post(url, auth=(os.environ['TEST_API_KEY'], ''), data=payload)
        data = json.loads(r.text)

        return data
