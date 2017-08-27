#! python3
#-*-coding:utf-8
import requests

import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'}
payload = {'wd': u'程序员'}

url = 'http://www.baidu.com/s'

r = requests.get(url, params=payload, headers=headers, timeout=5)
print(r.url)
print(r.status_code)

fp = open('search2.html', 'wb')
for chunk in r.iter_content(10000):
    fp.write(chunk)
fp.close()  