#! python3

from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def brosertest():
    browser = webdriver.Ie()
    browser.get('http://inventwithpython.com')
    linkElem = browser.find_element_by_link_text('Read It Online')
    linkElem.click() # follows the "Read It Online" link
    """
    try:
        elem = browser.find_element_by_class_name('bookcover')
        print('Found <%s> element with that class name!' % (elem.tag_name))
    except:
        print('Was not able to find an element with that name.')
    """
    print('done!')


def mailTo(in_addr, in_content):
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    browser.get('http://mail.10086.cn')
    browser.maximize_window()
    #time.sleep(5)
    linkElemUser = browser.find_element_by_id('txtUser')
    linkElemUser.clear()
    linkElemUser.send_keys('henss')
    linkElemPwd = browser.find_element_by_id('txtPass')
    linkElemPwd.send_keys('huangshi1982')
    linkElemSubmit = browser.find_element_by_id('loginBtn')
    linkElemSubmit.click()
    #time.sleep(5)
    linkElemWrite = browser.find_element_by_id('btn_compose')
    linkElemWrite.click()
    #time.sleep(2)
    #browser.implicitly_wait(2)

    iframes = browser.find_elements_by_tag_name('iframe')
    print(len(iframes))
    for i in iframes:
        print(i.get_attribute('class') +'  ' + i.get_attribute('name')  + '  ' +i.get_attribute('id'))
    browser.switch_to.frame(iframes[2])
    #time.sleep(2)

    linkElemAddr = browser.find_element_by_class_name('addrText-input')
    linkElemAddr.send_keys('henss@139.com')
  #  time.sleep(5)
    locator = (By.ID, 'txtSubject')
    try:
        WebDriverWait(browser, 10, 0.5).until(EC.presence_of_element_located(locator))
        linkElemSubj = browser.find_element_by_id('txtSubject')
      #  time.sleep(5)
        linkElemSubj.send_keys('setestmail')
      #  time.sleep(5)
    finally:
        print('done')
   # time.sleep(6)
    subiframes = browser.find_elements_by_tag_name('iframe')
    print(len(subiframes))
    for i in subiframes:
        print(i.get_attribute('class') +'  ' + i.get_attribute('name'))
   # print(subiframes[1].get_attribute('tabindex'))
    browser.switch_to.frame(subiframes[1])
 #   time.sleep(5)
   # time.sleep(6)

  #  browser.switch_to.frame(browser.find_element_by_xpath("//*[@id='view_0.775335838540318']/div[3]/div[2]/iframe"))
    linkElemCont = browser.find_element_by_tag_name('body')
 #   time.sleep(5)
    linkElemCont.send_keys('测试')
 #   time.sleep(5)
    browser.switch_to.default_content()
 #   time.sleep(5)
    browser.switch_to.frame(iframes[2])
 #   time.sleep(5)
    linkElemSend = browser.find_element_by_id('topSend')
    time.sleep(2)
    linkElemSend.click()
 #   time.sleep(5)
    browser.close()

mailTo('a', 'a')