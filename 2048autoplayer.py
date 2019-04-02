#! python3.6
# 2048autoplayer
# will autoplay 2048 and restart when it loses

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# launch 2048
browser = webdriver.Firefox()
browser.get('https://play2048.co/')
htmlElem = browser.find_element_by_tag_name('html')

# click play again if at game over otherwise, repeat up, down, left, right
while True:
    try:
        retryElem = browser.find_element_by_class_name('retry-button')
        retryElem.click()
    except:
        htmlElem.send_keys(Keys.ARROW_UP)
        htmlElem.send_keys(Keys.ARROW_RIGHT)
        htmlElem.send_keys(Keys.ARROW_DOWN)
        htmlElem.send_keys(Keys.ARROW_LEFT)