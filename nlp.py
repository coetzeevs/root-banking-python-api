def handle_message(message):
    greeting = first_entity_message(message["nlp"], 'greetings')

    if greeting and greeting['confidence'] > 0.8:
        output = "Howdy mate."

    else:
        output = "I'm guessing hi?"

    return output


def first_entity_message(nlp, name):
    return nlp['entities'][name][0]


def get_message(message, sender_name, message_text):

    if 'nlp' in message:
        if 'greetings' in message['nlp']['entities']:
            messg = handle_message(message)

            return messg
        else:
            messg = 'Hi, Thanks for getting in touch ' + sender_name + '.' \
                    + 'You sent this: ' + message_text

            return messg
