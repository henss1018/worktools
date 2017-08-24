#! python3
# madlibs.py - Saves and loads pieces of text to the clipboard.


import sys,re

test = 'aa bb cc dd'

libfile = open('tianci.txt','r')
libcontent = libfile.read()
#lib_regex = re.compile(r'ADJECTIVE|NOUN|VERB')
lib_result = re.findall(r'ADJECTIVE|NOUN|VERB',libcontent)
for i in lib_result:
    print ("Enter an %s" % i.lower())
    newword = input()
    libcontent = re.sub(i, newword, libcontent, 1)
print (libcontent)
newfile = open('newtianci.txt', 'w')
newfile.write(libcontent)
newfile.close()
libfile.close()