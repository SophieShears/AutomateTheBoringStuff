#! python3.6
# Command Line Emailer
# A program that takes an email of your choice and sends a email with your message via command line.
import sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

# Get email address
email = input('Enter email you want to send a message to: ')

# Get text from command line
message = ' '.join(sys.argv[1:])

# Login my email
browser.get('http://gmail.com')

emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('testsophie15@gmail.com')
emailElem.send_keys(Keys.ENTER)

print('Waiting a second...')
time.sleep(5)
passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys(input('enter your password: '))
passwordElem.send_keys(Keys.ENTER)

# Open new email and send cmd line text to given email address
print('Waiting for gmail to open...')
time.sleep(5)
composeElem = browser.find_element_by_class_name('z0')
composeElem.click()

print('Waiting for "new message" window to open...')
time.sleep(3)
recipentElem = browser.find_element_by_class_name('vO')
recipentElem.send_keys(email)

subjectElem = browser.find_element_by_class_name('aoT')
subjectElem.send_keys('Automated Email')

textElem = browser.find_element_by_class_name('Am.Al.editable.LW-avf')
textElem.send_keys(message)

textElem.send_keys(Keys.CONTROL,Keys.ENTER)
