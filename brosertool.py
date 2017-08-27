#! python3

from selenium import webdriver
browser = webdriver.Ie()
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read It Online')
#linkElem.click() # follows the "Read It Online" link
"""
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
"""
