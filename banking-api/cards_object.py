import requests
import os
import json

base_url = 'https://sandbox.root.co.za/v1/'


class Cards:
    route = "/cards/"
    api_url = base_url
    card_id = ""
    card_name = ""
    secure_code = ""
    pin = ""

    def __init__(self):
        pass

    def list_cards(self):
        url = self.api_url + self.route
        r = requests.get(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data

    def archive_card(self):
        url = self.api_url + self.route + self.card_id
        r = requests.delete(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data

    def retrieve_card(self):
        url = self.api_url + self.route + self.card_id
        r = requests.get(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data

    def retrieve_card_details(self):
        url = self.api_url + self.route + self.card_id + "/sensitive"
        r = requests.get(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data

    def create_virtual_card(self):
        payload = [
            ("name", self.card_name),
            ("secure_code", self.secure_code)
        ]
        url = self.api_url + self.route + "/create-virtual"
        r = requests.post(url, auth=(os.environ['TEST_API_KEY'], ''), data=payload)
        data = json.loads(r.text)

        return data

    def lock_card(self):
        url = self.api_url + self.route + self.card_id + "/lock"
        r = requests.post(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data

    def unlock_card(self):
        url = self.api_url + self.route + self.card_id + "/unlock"
        r = requests.post(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data

    def set_pin(self):
        payload = [
            ("pin", self.pin)
        ]
        url = self.api_url + self.route + self.card_id + "/set-pin"
        r = requests.post(url, auth=(os.environ['TEST_API_KEY'], ''), data=payload)
        data = json.loads(r.text)

        return data

    def set_card_3d_secure(self):
        payload = [
            ("secure_code", self.secure_code)
        ]
        url = self.api_url + self.route + self.card_id + "/set-secure-code"
        r = requests.post(url, auth=(os.environ['TEST_API_KEY'], ''), data=payload)
        data = json.loads(r.text)

        return data

    def list_card_transactions(self):
        url = self.api_url + self.route + self.card_id + "/transactions"
        r = requests.get(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data

    def fetch_root_code(self):
        url = self.api_url + self.route + self.card_id + "/root-code"
        r = requests.get(url, auth=(os.environ['TEST_API_KEY'], ''))
        data = json.loads(r.text)

        return data

        # To Do
        # def update_root_code(self):

# =================================
# == Example invocation of class ==
# =================================
# card1 = Cards()
#
# card1.route = 'cards/'
#
# obj = card1.list_cards()
#
# print(obj[0]['card_id'])

# =================================
# == Example invocation of class ==
# =================================
# card1 = Cards()
#
# card1.route = 'cards/'
#
# card1.card_id = card1.list_cards()[0]['card_id']
#
# print(card1.retrieve_card())
#
# print(card1.retrieve_card_details())


# =================================================
# == Example iterating through json object items ==
# =================================================
# obj = get_cards()
#
# print(obj[0])
#
# for item in obj:
#
#     print(item['card_id'])

# =================================
# == Example create virtual card ==
# =================================
# card1 = Cards()
#
# card1.route = 'cards/'
# card1.card_name = "TestPythonCard"
# card1.secure_code = "12345"
#
# obj = card1.create_virtual_card()
#
# print(obj)
