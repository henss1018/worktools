#! python3
# coding=utf-8

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
    #browser.implicitly_wait(5)
    #打开主页
    browser.get('http://mail.10086.cn')
    browser.maximize_window()
    #time.sleep(5)
    #获取用户名
    linkElemUser = browser.find_element_by_id('txtUser')
    linkElemUser.clear()
    linkElemUser.send_keys('henss')
    #获取密码
    linkElemPwd = browser.find_element_by_id('txtPass')
    linkElemPwd.send_keys('***')
    #获取登录按钮
    linkElemSubmit = browser.find_element_by_id('loginBtn')
    linkElemSubmit.click()
    #time.sleep(5)
    #获取写信按钮
    linkElemWrite = browser.find_element_by_id('btn_compose')
    linkElemWrite.click()
    #time.sleep(2)
    #browser.implicitly_wait(2)
    #获取所有iframe
    iframes = browser.find_elements_by_tag_name('iframe')
    print(len(iframes))
    for i in iframes:
        print(i.get_attribute('class') +'  ' + i.get_attribute('name')  + '  ' +i.get_attribute('id'))
    #切换到内容iframe
    browser.switch_to.frame(iframes[2])
    #获取内容iframe的所有子iframe
    subiframes = browser.find_elements_by_tag_name('iframe')
    print(len(subiframes))
    for i in subiframes:
        print(i.get_attribute('class') + '  ' + i.get_attribute('name'))
        # print(subiframes[1].get_attribute('tabindex'))
    #切换到编辑器的iframe，并添加内容
    browser.switch_to.frame(subiframes[1])
    linkElemCont = browser.find_element_by_tag_name('body')
    linkElemCont.send_keys('测试邮件，自动发送')
    #   time.sleep(5)
    #切回内容iframe
    browser.switch_to.default_content()
    browser.switch_to.frame(iframes[2])
    #获取主题
    linkElemSubj = browser.find_element_by_id('txtSubject')
    linkElemSubj.send_keys('setestmail')
    #获取收件人地址控件
    linkElemAddr = browser.find_element_by_class_name('addrText-input')
    linkElemAddr.send_keys('henss@139.com')
  #  time.sleep(5)
  #  同步等待加载成功后再执行
  #  locator = (By.ID, 'txtSubject')
  #  try:
    #WebDriverWait(browser, 10, 0.5).until(EC.presence_of_element_located(locator))

      #  time.sleep(5)
   # finally:
   #     print('done')
   # time.sleep(6)
    #获取发送信件按钮
    linkElemSend = browser.find_element_by_id('topSend')
    time.sleep(2)
    linkElemSend.click()
 #   time.sleep(5)
    browser.close()

mailTo('a', 'a')