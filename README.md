# PinLog
PinLog is a powerful driver and library integrated several logging systems. It is divided into smallest independent service units and easy to use.

## Installation

PinLog can be installed with [pip](http://pypi.python.org/pypi/pip) :

    $ python -m pip install pinlog

## Get Start

#### Step 1 - Import *pinlog*

    >>> from pinlog import helper
    >>> from pinlog.log import Log
    >>> from pinlog.helper import Logger, Console, Logstash, Filters


#### Step 2 - Add *@Logger* above the class

    >>> @Logger(Log.Console, Log.Logstash)
    >>> class MyClass():
    ...     def __init__(self):
    ... 
    ... 


#### Step 3 - Use *pin(str)* function to mark an excution timestamp
Define key or unique name to *pin(str)* function

    >>> mc = MyClass()
    >>> mc.pin('marker1')


#### Step 4 - Use *latency(str1, str2)* function to find out timing in milliseconds from point to point
From below example, to find timing of execution process from *'marker1'* to *'marker2'* by calling *latency('marker1', 'marker2')*

    >>> time.sleep(3)
    >>> mc.pin('marker2')
    >>> print("--- %.8f milliseconds execution ---" % (mc.latency('marker1', 'marker2')))
    --- 3001.61195 milliseconds execution ---


#### Step 5 - Use *@Filters(...)* along with *trace(str1, data)* function
With placing *@Filters(...)* above the class and filling some attributes names you need, *trace(str1, data)* function will format data then return only attributes you declared. In additional the return value will be add *latency* attribute in milliseconds as well.

    >>> @Logger(Log.Console, Log.Logstash)
    >>> @Filters('attribute1', 'attribute2', 'attribute3', 'attribute4')
    >>> class MyClass():
    ...     def __init__(self):
    ... 
    ... data = {...}
    ... output = mc.trace('marker1', data)


#### Step 6 - Finally, use *unpin(str)* function to reset timestamp

    >>> mc.unpin('marker1')
    >>> mc.unpin('marker2')


Moreover, Excution process times is able to traced from anywhere no matter other functions, other classes, not even other applications as below examples
## Tracing over 2 applications
Below examples show how to trace times across 2 applications. By creating the first application, *class1.py* and the second application, *class2.py*
#### Declaring Class1() in *class1.py* :
    from pinlog import helper
    from pinlog.log import Log
    from pinlog.helper import Logger, Console, Logstash, Filters
    import time

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

#### Declaring Class2() in *class2.py* :
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
    output1 = c2.trace('marker1', data)
    print('Output 1 : ', output1)
    output2 = c2.trace('marker2', data)
    print('Output 2 : ', output2)

#### Output :
    Output 1 : {'username': 'admin', 'firstname': 'Tom', 'middlename': None, 'lastname': 'Cruise', 'latency': 13845.938920974731}
    Output 2 : {'username': 'admin', 'firstname': 'Tom', 'middlename': None, 'lastname': 'Cruise', 'latency': 10844.847202301025}