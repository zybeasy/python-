#/usr/bin/env python
#-*- utf-i -*-
import eventlet
from eventlet import event
from datetime import datetime as dt

#################################################
evt = event.Event()
def func():
    print "BEFORE", dt.now()
    print evt.wait()
    print "END", dt.now()

a = eventlet.spawn(func)
print "MAIN", dt.now()
eventlet.sleep(0)   # 主动让出运行权利，GreenThread a得以运行
print "MAIN", dt.now()
evt.send('a')       # 再次让出运行权利，GreenThread a得以运行完成
eventlet.sleep(0)

""" Output
MAIN 2017-12-09 20:05:38.468139
BEFORE 2017-12-09 20:05:38.468229
MAIN 2017-12-09 20:05:38.468266
END 2017-12-09 20:05:38.468325

Windows环境运行这段代码结果不稳定，是不是不要在Windows环境使用eventlet？
eventlet的GreenThread是主动放弃自己的运行权利的，然后hub调度可执行的GreenThread。
"""
################################################

