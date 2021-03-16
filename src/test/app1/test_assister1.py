from pinlog import log, helper
from pinlog.log import Log
from pinlog.helper import Logger, Console, Logstash, Filters
import time

# @Logstash('username', 'role', 'department')
# @Console('username', 'firstname', 'middlename', 'lastname')
@Logger(Log.Console, Log.Logstash)
@Filters('username', 'firstname', 'middlename', 'lastname')
class Class1():
    
    def __init__(self):
        pass

    def function1(self, str):
        pass


c1 = Class1()
c1.pin('marker1')
time.sleep(3)
c1.pin('marker2')
print("--- %.8f seconds first execution ---" % (c1.latency('marker1', 'marker2')))
