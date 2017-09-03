#!python3
#from string import maketrans

#1、通过asc表自行转换；2、通过映射表直接用string的内置函数转换
def map():
    oldstr = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. " \
             "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. " \
             "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    #print(oldstr)
    i = 0
    s = list(oldstr)
    for i in range(len(s)-1):
        if(ord(s[i])<97 or ord(s[i])>122):
            continue
        if(ord(s[i])+2>122):
            s[i] = chr(97+ord(s[i])+1-122)
        else:
            s[i] = chr(ord(s[i])+2)

    oldstr = ''.join(s)
    newstr = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. " \
             "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. " \
             "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    intab = "abcdefghijklmnopqrstuvwxyz"
    outtab = "cdefghijklmnopqrstuvwxyzab"
    trantab = str.maketrans(intab, outtab)
    print('map'.translate(trantab))

    #print(oldstr)


map()