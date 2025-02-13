#! python3
# text_myself.py - Defines the textmyself() function that texts a message
# passed to it as a string.

# Preset values:
account_SID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token  = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
my_number = '+15559998888'
twilio_number = '+15552225678'
from twilio.rest import Client

def textmyself(message):
    twilio_Cli = Client(account_SID, auth_token)
    twilio_Cli.messages.create(body=message, from_=twilio_number, to=my_number)