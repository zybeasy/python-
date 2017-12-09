import eventlet
from eventlet import event
from datetime import datetime as dt

evt = event.Event()

def func():
    print "BEFORE", dt.now()
    print evt.wait()
    print "END", dt.now()

a = eventlet.spawn(func)
print "MAIN", dt.now()
eventlet.sleep(0)
print "MAIN", dt.now()
evt.send('a')
eventlet.sleep(0)
