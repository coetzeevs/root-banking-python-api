# Facebook Messenger Bot
This is a simple python template that uses Flask to build a webhook for Facebook's Messenger Bot API.

Read more: [tutorial that uses this repository](https://blog.hartleybrody.com/fb-messenger-bot/).

## "Root Banking API"

The Root API functions are wrapped into their own classes to make access easier. 

Areas of the API already written:

- Cards Object
- Accounts Object
- Transactions Object (WIP)

## "NLP"

Basic NLP has been implemented to recognise a greeting intent sent from Wit.ai. The idea is to scrap this and move to Dialogflow.