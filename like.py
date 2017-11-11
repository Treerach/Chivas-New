# -*- coding: utf-8 -*-
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,base64
cl = LINETCR.LINE()
cl.login(qr=True)
cl.loginResult()
ks = ki = kk = kc = cl 
print u"login success"
reload(sys)
sys.setdefaultencoding('utf-8')
i = 0
c_text = """Auto Like"""
while True:
    try:
        for posts in cl.activity(1)["result"]["posts"]:
            if posts["postInfo"]["liked"] is False:
                cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1002)
                cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
                print u"liked" + str(i)
                i += 1
    except Exception as e:
            print e