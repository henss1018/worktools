#! python3
#-*-coding:utf-8
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Baiduing...') # display text while downloading the Google page
res = requests.get('http://www.baidu.com/s?wd=' + ' '.join(sys.argv[1:]))
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'}
payload = {'wd': u'程序员'}

url = 'http://www.baidu.com/s?wd=程序员'

#res = requests.get(url, params=payload, headers=headers, timeout=5)
#res = requests.get(url)
#res = requests.get('https://www.baidu.com/s')
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "lxml")

# Open a browser tab for each result.
linkElems = soup.select('.t a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open(linkElems[i].get('href'))
