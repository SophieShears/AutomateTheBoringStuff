#! python3.6
# textDelay.py - Takes a phone number, time, and message. And sends a text at that time to the number.
# Format is: phone number, time delay(hours), text body
# Example: +17633249497 5 This is an example text

import time, datetime, sys
from twilio.rest import Client

# Set current time and time you want text sent.
now = datetime.datetime.now()
delay = datetime.timedelta(hours=int(sys.argv[2]))
sleepUntil = now + delay

# Wait until set time.
while datetime.datetime.now() < sleepUntil:
    time.sleep(1)

# Preset twilio values:
accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
twilioNumber = '+17633249497'
sendToNumber = str(sys.argv[1])  # Entered phone number

# Send text message.
twilioCli = Client(accountSID, authToken)
twilioCli.messages.create(body=' '.join(sys.argv[3:]), from_=twilioNumber, to=sendToNumber)
print('Message sent successfully.')
