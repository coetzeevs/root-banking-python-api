import os
import sys
import json
import jsonify
from nlp import first_entity_message, handle_message, get_message
import requests
from flask import Flask, request

DEFAULT_REPONSE = "Sorry mate, didn't quite get that. Mind trying again?"

app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
    print('challenge fired')
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['GET', 'POST'])
def webhook():
    # endpoint for processing incoming messaging events
    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    if "object" in data:
        if data["object"] == "page":

            for entry in data["entry"]:

                for messaging_event in entry["messaging"]:

                    if messaging_event.get("delivery"):  # delivery confirmation
                        pass

                    if messaging_event.get("optin"):  # optin confirmation
                        pass

                    if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                        pass

                    if messaging_event.get("message"):  # someone sent us a message

                        message = messaging_event.get("message")

                        sender_id = messaging_event["sender"]["id"]  # the facebook ID of the person sending you the message
                        # sender_name = messaging_event["sender"]['first_name']

                        recipient_id = messaging_event["recipient"]["id"]
                        # the recipient's ID, which should be your page's facebook ID

                        message_text = messaging_event["message"]["text"]
                        # the message's text

                        sender_obj = create_response(sender_id)

                        sender_name = sender_obj['name']

                        messg = get_message(message, sender_name, message_text)

                        send_message(sender_id, messg)
    else:
        print(data)

        response = json.dumps({
            "speech": data['result']['fulfillment']['speech'],
            "displayText": data['result']['fulfillment']['speech'],
            "data": {
            }
        })
        return response

    return "ok", 200


def send_message(recipient_id, message_text):
    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": str(recipient_id)
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)


def create_response(sender_id):
    sender_url = 'https://graph.facebook.com/v2.6/%s' % sender_id
    sender_params = {"fields": "name",
                     "access_token": os.environ['PAGE_ACCESS_TOKEN']}
    sender = requests.get(sender_url, sender_params).json()

    return sender


def log(message):  # simple wrapper for logging to stdout on heroku
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True, port=8080)
