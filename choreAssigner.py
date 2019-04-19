#! python3.6
# choreAssigner.py - Randomly assign chores and email them to people from a set list.

import random, smtplib, sys

exmpEmails = ['test@yahoo.com','fakeemail@gmail.com', 'genericEmail@spore.net', 'trashaccount@comcast.potato']
chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']

# Login to smtp
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('mpirkl12@gmail.com', sys.argv[1])

# Send an email to everyone on the list and assign a random chore.
for email in exmpEmails:
    randomChore = random.choice(chores)
    body = "Subject: Chores. \nYour assigned chore for this month is: %s. " % randomChore
    chores.remove(randomChore)
    print('Sending email to %s...' % email)
    sendmailStatus = smtpObj.sendmail('mpirkl12@gmail.com', email, body)

    # If sendmail was unable to send, list who didn't get an email.
    if sendmailStatus != {}:
        print('There was a problem sending email to %s: %s' % (email, sendmailStatus))
smtpObj.quit()
