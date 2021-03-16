from pinlog import helper
from pinlog.log import Log
from pinlog.helper import Logger, Console, Logstash, Filters

@Logger(Log.Console, Log.Logstash)
class Class2():

    def __init__(self):
        pass

    def function2(self, str):
        pass

c2 = Class2()
data = {
    'username': 'admin',
    'password': '1qazxsw2',
    'firstname': 'Tom',
    'lastname': 'Cruise',
    'role': 'Administrator',
    'birthdate': 'July 3, 1962',
    'department': 'Cruise/Wagner Productions'
}
output = c2.trace('marker1', data)
print(output)
output = c2.trace('marker2', data)
print(output)
c2.unpin('marker1')

# globals()['Client']()
# print(type(x).__name__)

